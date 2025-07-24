# ArKG-Chile-Data - Instrucciones con UV

Herramienta colaborativa que extrae datos arqueológicos de PDFs escaneados usando LlamaParse y la API de OpenAI para poblar una base de datos de grafos de conocimiento arqueológico. Transforma documentación arqueológica compleja en datasets CSV estructurados para investigación y esfuerzos de preservación.

## Requisitos

- Python 3.10 o superior
- UV (gestor de paquetes rápido de Python)
- Clave API de LlamaParse
- Clave API de OpenAI

## Instalación

### 1. Instalar UV (si no lo tienes)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verificar instalación:**
```powershell
uv --version
```

### 2. Clonar el repositorio

```bash
git clone https://github.com/arqueomendez/ArKG-Chile-Data.git
cd ArKG-Chile-Data
```

### 3. Configurar el proyecto con UV

**Inicializar el entorno virtual y dependencias:**
```bash
uv sync
```

Este comando:
- Crea automáticamente un entorno virtual
- Instala todas las dependencias especificadas en `pyproject.toml`
- Sincroniza el entorno con las dependencias exactas

### 4. Configurar claves API

Crea un archivo `.env` en la raíz del proyecto con tus claves API:

```bash
# Crear archivo .env
uv run python -c "
with open('.env', 'w') as f:
    f.write('LLAMA_CLOUD_API_KEY=tu_clave_llamaparse\\n')
    f.write('OPENAI_API_KEY=tu_clave_openai\\n')
"
```

O crea manualmente el archivo `.env`:
```
LLAMA_CLOUD_API_KEY=tu_clave_llamaparse
OPENAI_API_KEY=tu_clave_openai
```

## Uso

### Ejecución principal

```bash
uv run python pdf_extractor.py
```

### Comandos útiles con UV

**Agregar nuevas dependencias:**
```bash
uv add nombre_paquete
```

**Agregar dependencias de desarrollo:**
```bash
uv add --dev pytest black flake8
```

**Actualizar dependencias:**
```bash
uv sync --upgrade
```

**Ver dependencias instaladas:**
```bash
uv pip list
```

**Ejecutar comandos en el entorno:**
```bash
uv run python script.py
uv run pip list
```

**Activar el entorno manualmente (opcional):**
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux  
source .venv/bin/activate
```

### Desarrollo

**Instalar dependencias de desarrollo:**
```bash
uv add --dev pytest black isort mypy
```

**Ejecutar tests:**
```bash
uv run pytest
```

**Formatear código:**
```bash
uv run black .
uv run isort .
```

## Ventajas de UV vs pip tradicional

1. **Velocidad**: UV es 10-100x más rápido que pip
2. **Gestión automática**: Crea y gestiona entornos virtuales automáticamente
3. **Resolución de dependencias**: Resolver conflictos de manera más eficiente
4. **Bloqueo de versiones**: Genera automáticamente archivos de bloqueo
5. **Compatibilidad**: Funciona con proyectos existentes de pip/requirements.txt

## Estructura del proyecto

```
ArKG-Chile-Data/
├── .env                     # Claves API (crear manualmente)
├── .venv/                   # Entorno virtual (creado por UV)
├── pyproject.toml           # Configuración del proyecto y dependencias
├── requirements.txt         # Dependencias legacy (opcional)
├── pdf_extractor.py         # Script principal
├── Data/                    # Datos de entrada
├── Results/                 # Resultados procesados
└── README_UV.md             # Este archivo
```

## Solución de problemas

**Si UV no está instalado:**
- Sigue las instrucciones de instalación en https://docs.astral.sh/uv/

**Error de permisos en Windows:**
- Ejecuta PowerShell como administrador
- O usar: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Problemas con dependencias:**
```bash
uv sync --reinstall
```

**Limpiar cache:**
```bash
uv cache clean
```

## Flujo de trabajo recomendado

1. **Clonar repositorio**
2. **`uv sync`** - Configurar entorno
3. **Configurar .env** - Agregar claves API
4. **`uv run python pdf_extractor.py`** - Ejecutar aplicación
5. **Desarrollo continuo** con `uv add` para nuevas dependencias

¡El proyecto está listo para usar con UV!
