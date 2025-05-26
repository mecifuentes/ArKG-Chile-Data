import asyncio
import glob
import os
import platform
import re
import subprocess
import time
import tkinter as tk
from tkinter import filedialog, messagebox

import pandas as pd
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

load_dotenv()


def LlamaParser(ruta_archivo):
    parser = LlamaParse(result_type="markdown")
    file_extractor = {".pdf": parser}
    documents = SimpleDirectoryReader(
        input_files=[ruta_archivo], file_extractor=file_extractor
    ).load_data()

    final = []
    for i in range(len(documents)):
        if "|" in documents[i].text:
            texto = documents[i].text
            tablas = re.findall(r"(?:^\|.*\n?)+", texto, re.MULTILINE)
            for i, tabla in enumerate(tablas, 1):
                final.append([tabla.strip(), i, ""])

    print(len(final), "tablas encontradas")
    return final


def extraer_tabla_de_response(response: str) -> pd.DataFrame:
    inicio = response.find("```")
    fin = response.find("```", inicio + 3)
    if inicio == -1 or fin == -1:
        raise ValueError("No se encontró un bloque de tabla en el texto.")

    tabla_texto = response[(inicio + 3) : fin].strip()
    lineas = tabla_texto.splitlines()
    filas = [line.split(",") for line in lineas]
    max_columnas = max(len(fila) for fila in filas)
    filas = [fila + [""] * (max_columnas - len(fila)) for fila in filas]
    df = pd.DataFrame(filas[1:], columns=filas[0])
    return df


def CallOpenAI(tablas):
    prompt_default = """Se te entregara una tabla en formato markdown,
        corrige posibles errores en la estructura
        y evalua una nota BAJA-MEDIA-ALTA
        dependiendo que tan correcto es el formato original de la tabla.
        <INSERT>
        El output debe ser UNICAMENTE la NOTA
        y la TABLA arreglada en formato csv.
        OUTPUT:
        Nota: <NOTA>
        <TABLA>
        """

    async def process_all_tables():
        resultados = []
        llm = OpenAI(model="gpt-4o-mini")
        cont = 0
        for tabla in tablas:
            print("Tabla", cont, "procesada")
            prompt = prompt_default.replace("<INSERT>", tabla[0])
            agent = FunctionAgent(
                llm=llm,
                tools=[],
            )
            cont += 1
            response = await agent.run(prompt)
            resultados.append(response)
        print("Todas las tablas procesadas")
        return resultados

    resultados = asyncio.run(process_all_tables())

    for coso in range(len(resultados)):
        try:
            extraido = extraer_tabla_de_response(str(resultados[coso]))
            extraido.to_csv(f"Partial_tables/tabla_{coso}.csv", index=False)
        except ValueError as e:
            print(f"Error al extraer la tabla: {coso} - {e}")
            continue


def MergeTablas(path):
    csv_files = glob.glob(os.path.join(path, "*.csv"))

    if not csv_files:
        print(f"No CSV files found in {path}")
        return None

    dfs = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not dfs:
        print("No valid CSV files could be read")
        return None

    merged_df = pd.concat(dfs, ignore_index=True, sort=False)

    merged_df = merged_df.where(pd.notnull(merged_df), None)

    output_file = "Results/merged_tables.csv"
    merged_df.to_csv(output_file, index=False)
    print(f"Merged table saved to {output_file}")
    for file in csv_files:
        # Skip the merged file if it's in the same directory
        if file == output_file:
            continue

        try:
            os.remove(file)
        except Exception as e:
            print(f"Error deleting {file}: {e}")

    return merged_df


def mostrar_bienvenida():
    limpiar_ventana()
    etiqueta_bienvenida.pack(expand=True, pady=20)
    boton_continuar_1.pack(pady=20)


def limpiar_ventana():
    for widget in root.winfo_children():
        widget.pack_forget()


def mostrar_segunda_etapa():
    limpiar_ventana()
    etiqueta_instruccion.pack(pady=(50, 10))
    boton_seleccionar.pack(pady=10)
    etiqueta_ruta.pack(pady=10)


def abrir_dialogo():
    global ruta_seleccionada
    ruta = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[
            ("PDF", "*.pdf"),
            ("Texto", "*.txt"),
            ("CSV", "*.csv"),
            ("Todos los archivos", "*.*"),
        ],
    )
    if ruta:
        ruta_seleccionada = ruta
        etiqueta_ruta.config(text=f"Archivo seleccionado:\n{ruta}")
        boton_continuar_2.pack(pady=20)
    else:
        messagebox.showinfo("Sin selección", "No hay selección.")


def mostrar_tercera_etapa():
    limpiar_ventana()
    etiqueta_progreso.pack(expand=True, pady=80)
    root.update()

    time.sleep(1)
    tablas = LlamaParser(ruta_seleccionada)
    CallOpenAI(tablas)

    mostrar_cuarta_etapa(len(tablas))


label_final = None
boton_revisar = None


def mostrar_cuarta_etapa(num_tablas):
    global label_final, boton_revisar
    limpiar_ventana()
    label_final = tk.Label(
        root,
        text=f"Tablas encontradas: {num_tablas}\nPor favor, revísalas",
        font=("Arial", 14),
        justify="center",
    )
    boton_revisar = tk.Button(
        root,
        text="Revisar tablas",
        font=("Arial", 12),
        width=15,
        command=primer_click_revisar,
    )
    label_final.pack(expand=True, pady=(60, 10))
    boton_revisar.pack(pady=20)


def primer_click_revisar():
    global partial_path
    partial_path = os.path.abspath("Partial_tables")
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(partial_path)
        elif system == "Darwin":
            subprocess.Popen(["open", partial_path])
        else:
            subprocess.Popen(["xdg-open", partial_path])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la carpeta:\n{e}")
        return
    boton_revisar.config(command=segundo_click_listo)


def segundo_click_listo():
    global partial_path
    cantidad = len([f for f in os.listdir(partial_path) if ".csv" in f])
    label_final.config(text=f"Programa terminado, quedaron un total de {cantidad}")
    MergeTablas(partial_path)
    mostrar_quinta_etapa(cantidad)


def mostrar_quinta_etapa(cantidad):
    limpiar_ventana()
    mensaje = tk.Label(
        root,
        text=f"Proceso completo. Tablas fusionadas.\nTotal de archivos: {cantidad}",
        font=("Arial", 14),
        justify="center",
    )
    boton_reiniciar = tk.Button(
        root,
        text="Volver al inicio",
        font=("Arial", 12),
        width=15,
        command=mostrar_bienvenida,
    )
    boton_terminar = tk.Button(
        root, text="Terminar", font=("Arial", 12), width=15, command=root.destroy
    )
    mensaje.pack(expand=True, pady=(40, 10))
    boton_reiniciar.pack(side="left", expand=True, padx=20, pady=20)
    boton_terminar.pack(side="right", expand=True, padx=20, pady=20)


root = tk.Tk()
root.title("ArKG Chile")
root.geometry("500x350")

etiqueta_bienvenida = tk.Label(
    root,
    text="Hola\nBienvenido al programa ArKG Chile",
    font=("Arial", 16),
    justify="center",
)

boton_continuar_1 = tk.Button(
    root, text="Continuar", font=("Arial", 12), width=10, command=mostrar_segunda_etapa
)

etiqueta_instruccion = tk.Label(
    root,
    text="Selecciona un archivo para trabajar",
    font=("Arial", 14),
    justify="center",
)

boton_seleccionar = tk.Button(
    root, text="Subir archivo", font=("Arial", 12), width=12, command=abrir_dialogo
)

etiqueta_ruta = tk.Label(root, text="", font=("Arial", 10), justify="center")

boton_continuar_2 = tk.Button(
    root, text="Continuar", font=("Arial", 12), width=10, command=mostrar_tercera_etapa
)

etiqueta_progreso = tk.Label(
    root,
    text="Procesando con LlamaParser y OpenAI...",
    font=("Arial", 14),
    justify="center",
)

ruta_seleccionada = None
partial_path = None

mostrar_bienvenida()

root.mainloop()
