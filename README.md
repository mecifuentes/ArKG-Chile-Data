# ArKG-Chile-Data Pipeline

Herramienta colaborativa que extrae datos arqueológicos de PDFs escaneados usando LlamaParse y la API de OpenAI o4-mini para poblar una base de datos de grafos de conocimiento arqueológico. Transforma documentación arqueológica compleja en datasets CSV estructurados para investigación y esfuerzos de preservación.

## 🚀 Instalación Rápida con UV (Recomendado)

### Opción 1: Configuración Automática
```bash
# Clonar repositorio
git clone https://github.com/arqueomendez/ArKG-Chile-Data.git
cd ArKG-Chile-Data

# Configuración automática
uv run python setup_uv.py

# Editar .env con tus claves API reales
# Ejecutar aplicación
uv run python pdf_extractor.py
```

### Opción 2: Configuración Manual
```bash
# Instalar UV (si no lo tienes)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Clonar y configurar
git clone https://github.com/arqueomendez/ArKG-Chile-Data.git
cd ArKG-Chile-Data
uv sync

# Crear archivo .env con tus claves
# LLAMA_CLOUD_API_KEY=tu_clave
# OPENAI_API_KEY=tu_clave

# Ejecutar
uv run python pdf_extractor.py
```

## 📋 Requisitos

- Python 3.10 o superior  
- GIT
- UV (gestor de paquetes rápido de Python)
- Clave API de LlamaParse ([obtener aquí](https://cloud.llamaindex.ai/))
- Clave API de OpenAI ([obtener aquí](https://platform.openai.com/api-keys))

## 📖 Instalación Tradicional (pip)

<details>
<summary>Ver instrucciones tradicionales con pip</summary>

### Clonar repositorio
```bash
git clone https://github.com/arqueomendez/ArKG-Chile-Data.git
cd ArKG-Chile-Data
```

### Crear entorno virtual
```bash
# Windows
python3 -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configurar claves API
Crear archivo `.env`:
```
LLAMA_CLOUD_API_KEY=tu_clave_llamaparse
OPENAI_API_KEY=tu_clave_openai
```

### Actualización estándar con Git
Abre una terminal en la carpeta ArKG-Chile-Data:
```bash
# En Windows
venv\Scripts\activate
git pull

# En macOS/Linux
source venv/bin/activate
git pull
```

</details>

## 🎯 Uso

### Comando básico
```bash
uv run python pdf_extractor.py
```

### Con Makefile (opcional)
```bash
make setup      # Configuración inicial
make run        # Ejecutar aplicación
make test       # Ejecutar tests
make format     # Formatear código
make help       # Ver todos los comandos
```

## 🛠️ Desarrollo

### Instalar dependencias de desarrollo
```bash
uv add --dev pytest black isort flake8 mypy pre-commit
```

### Comandos útiles
```bash
# Agregar dependencias
uv add nombre_paquete

# Actualizar dependencias  
uv sync --upgrade

# Formatear código
uv run black .
uv run isort .

# Ejecutar tests
uv run pytest
```

## 📁 Estructura del Proyecto

```
ArKG-Chile-Data/
├── .env                        # Claves API (crear manualmente)
├── .venv/                      # Entorno virtual (creado por UV)
├── pyproject.toml              # Configuración del proyecto
├── setup_uv.py                 # Script de configuración automática
├── Makefile                    # Automatización de tareas
├── pdf_extractor.py            # Script principal
├── requirements.txt            # Dependencias legacy
├── Data/                       # Datos de entrada
├── Results/                    # Resultados procesados
├── README_UV.md                # Instrucciones detalladas UV
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
