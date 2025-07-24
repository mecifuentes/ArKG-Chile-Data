# ArKG-Chile-Data Pipeline

Herramienta colaborativa que extrae datos arqueológicos de PDFs escaneados usando LlamaParse y la API de OpenAI o4-mini para poblar una base de datos de grafos de conocimiento arqueológico. Transforma documentación arqueológica compleja en datasets CSV estructurados para investigación y esfuerzos de preservación.

## 📋 Requisitos

- Python 3.10 o superior  
- GIT
- UV (gestor de paquetes rápido de Python)
- Clave API de LlamaParse ([obtener aquí](https://cloud.llamaindex.ai/))
- Clave API de OpenAI ([obtener aquí](https://platform.openai.com/api-keys))

## 🚀 Instalación Rápida con UV (Recomendado)

```bash
# Instalar UV
# Abrir PowerShell en Windows y ejecutar
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Abrir consola en MAC/Linux y ejecutar
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clonar y configurar
git clone https://github.com/arqueomendez/ArKG-Chile-Data.git
cd ArKG-Chile-Data
uv init

# Instalar dependencias
uv add -r requirements.txt

# Crear archivo .env con tus claves
LLAMA_CLOUD_API_KEY=tu_clave
OPENAI_API_KEY=tu_clave

# Ejecutar
uv run pdf_extractor.py
```

### Actualización estándar con Git
Abre una terminal en la carpeta ArKG-Chile-Data:
```bash
# En Windows y macOS/Linux
git pull
```
## 🎯 Uso

### Comando básico
```bash
uv run pdf_extractor.py
```

## 📁 Estructura del Proyecto

```
ArKG-Chile-Data/
├── .env                        # Claves API (crear manualmente)
├── .venv/                      # Entorno virtual (creado por UV)
├── pyproject.toml              # Configuración del proyecto
├── pdf_extractor.py            # Script principal
├── requirements.txt            # Dependencias legacy
├── Data/                       # Datos de entrada
├── Results/                    # Resultados procesados
└── README.md                   # Este archivo
```

## 📊 Funcionalidad

Este trabajo consiste en dos pasos principales:

### 1. Extracción de datos
La lógica completa está contenida en `pdf_extractor.py`.

El script despliega una interfaz gráfica que permite al usuario seleccionar un documento (solo PDF por ahora) para extraer la información.

Luego, sigue las instrucciones:
1. Verifica que los archivos extraídos contengan información de fecha/timestamp
2. Elimina tablas no relacionadas
3. Continúa con el procesamiento

### 2. Formato de datos
Los datos extraídos se formatean para guardar en una base de datos estructurada.

## 🚀 Ventajas de UV

- **⚡ Velocidad**: 10-100x más rápido que pip
- **🔄 Gestión automática**: Crea y gestiona entornos virtuales automáticamente  
- **🔧 Resolución inteligente**: Resuelve conflictos de dependencias eficientemente
- **🔒 Bloqueo de versiones**: Genera archivos de bloqueo automáticamente
- **🔄 Compatibilidad**: Funciona con proyectos existentes de pip

## 🆘 Solución de Problemas

### UV no instalado
```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verificar
uv --version
```

### Problemas de permisos (Windows)
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Reinstalar dependencias
```bash
uv sync --reinstall
```

### Limpiar cache
```bash
uv cache clean
```

## 📚 Documentación Adicional

- [README_UV.md](README_UV.md) - Instrucciones detalladas para UV
- [Documentación de UV](https://docs.astral.sh/uv/)
- [LlamaParse Documentation](https://docs.llamaindex.ai/)

## 🤝 Contribuir

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia especificada en el repositorio original.

---

⭐ **¡Proyecto listo para usar con UV!** ⭐
