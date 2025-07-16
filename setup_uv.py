#!/usr/bin/env python3
"""
Script de configuración automática para migrar ArKG-Chile-Data a UV
Ejecutar con: uv run python setup_uv.py
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description=""):
    """Ejecuta un comando y maneja errores"""
    print(f"🔄 {description}")
    print(f"   Ejecutando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} - Completado")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}:")
        print(f"   {e.stderr}")
        return None


def check_uv_installed():
    """Verifica si UV está instalado"""
    try:
        result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
        print(f"✅ UV detectado: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("❌ UV no está instalado")
        print("📝 Instala UV con:")
        print("   PowerShell: powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\"")
        print("   O visita: https://docs.astral.sh/uv/")
        return False


def create_env_template():
    """Crea un template del archivo .env si no existe"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        env_content = """# Configuración de APIs para ArKG-Chile-Data
# Obtén tu clave en: https://cloud.llamaindex.ai/
LLAMA_CLOUD_API_KEY=tu_clave_llamaparse_aqui

# Obtén tu clave en: https://platform.openai.com/api-keys
OPENAI_API_KEY=tu_clave_openai_aqui
"""
        
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ Archivo .env creado con template")
        print("📝 IMPORTANTE: Edita .env con tus claves API reales")
    else:
        print("✅ Archivo .env ya existe")
    
    # Crear también .env.example
    if not env_example.exists():
        example_content = """# Ejemplo de configuración - copia a .env y completa con tus claves reales
LLAMA_CLOUD_API_KEY=tu_clave_llamaparse_aqui
OPENAI_API_KEY=tu_clave_openai_aqui
"""
        with open(env_example, 'w') as f:
            f.write(example_content)
        print("✅ Archivo .env.example creado")


def setup_gitignore():
    """Configura .gitignore para UV"""
    gitignore_file = Path('.gitignore')
    
    uv_entries = [
        "# UV virtual environment",
        ".venv/",
        "uv.lock",
        "",
        "# Environment variables",
        ".env",
        "",
        "# Python cache",
        "__pycache__/",
        "*.pyc",
        "*.pyo",
        "",
    ]
    
    if gitignore_file.exists():
        with open(gitignore_file, 'r') as f:
            content = f.read()
        
        # Agregar entradas de UV si no existen
        needs_update = False
        for entry in [".venv/", "uv.lock"]:
            if entry not in content:
                needs_update = True
                break
        
        if needs_update:
            with open(gitignore_file, 'a') as f:
                f.write('\n' + '\n'.join(uv_entries))
            print("✅ .gitignore actualizado con entradas de UV")
        else:
            print("✅ .gitignore ya está configurado")
    else:
        with open(gitignore_file, 'w') as f:
            f.write('\n'.join(uv_entries))
        print("✅ .gitignore creado")


def main():
    """Función principal de configuración"""
    print("🚀 Configurando ArKG-Chile-Data para usar UV")
    print("=" * 50)
    
    # Verificar UV
    if not check_uv_installed():
        return
    
    # Verificar que estamos en el directorio correcto
    if not Path('pdf_extractor.py').exists():
        print("❌ No se encontró pdf_extractor.py")
        print("   ¿Estás en el directorio correcto del proyecto?")
        return
    
    print("✅ Directorio del proyecto detectado")
    
    # Crear archivo .env
    create_env_template()
    
    # Configurar .gitignore
    setup_gitignore()
    
    # Sincronizar dependencias con UV
    print("\n🔄 Instalando dependencias con UV...")
    result = run_command("uv sync", "Sincronización de dependencias")
    
    if result is not None:
        print("\n🎉 ¡Configuración completada exitosamente!")
        print("\n📋 Próximos pasos:")
        print("1. Edita el archivo .env con tus claves API reales")
        print("2. Ejecuta el proyecto con: uv run python pdf_extractor.py")
        print("3. Para agregar dependencias: uv add nombre_paquete")
        print("\n📚 Ver README_UV.md para más información")
    else:
        print("\n❌ Hubo problemas durante la configuración")
        print("   Revisa los errores arriba e intenta nuevamente")


if __name__ == "__main__":
    main()
