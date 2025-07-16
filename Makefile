# Makefile para ArKG-Chile-Data con UV
# Uso: make [comando]

.PHONY: help install dev-install run test format lint clean setup

help: ## Mostrar ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Configuración inicial completa del proyecto
	@echo "🚀 Configurando ArKG-Chile-Data con UV..."
	uv sync
	python setup_uv.py
	@echo "✅ Configuración completada"

install: ## Instalar dependencias principales
	uv sync

dev-install: ## Instalar dependencias de desarrollo
	uv add --dev pytest black isort flake8 mypy pre-commit
	uv run pre-commit install

run: ## Ejecutar la aplicación principal
	uv run python pdf_extractor.py

test: ## Ejecutar tests
	uv run pytest -v

format: ## Formatear código
	uv run black .
	uv run isort .

lint: ## Verificar calidad del código
	uv run flake8 .
	uv run black --check .
	uv run isort --check-only .

type-check: ## Verificar tipos con mypy
	uv run mypy pdf_extractor.py

clean: ## Limpiar archivos temporales
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	uv cache clean

update: ## Actualizar dependencias
	uv sync --upgrade

add: ## Agregar nueva dependencia (uso: make add PACKAGE=nombre_paquete)
	uv add $(PACKAGE)

add-dev: ## Agregar dependencia de desarrollo (uso: make add-dev PACKAGE=nombre_paquete)
	uv add --dev $(PACKAGE)

env-check: ## Verificar configuración del entorno
	@echo "🔍 Verificando configuración..."
	@if [ -f .env ]; then echo "✅ Archivo .env encontrado"; else echo "❌ Archivo .env no encontrado - ejecuta 'make setup'"; fi
	@uv --version
	@uv run python --version

status: ## Mostrar estado del proyecto
	@echo "📊 Estado del proyecto ArKG-Chile-Data:"
	@echo "UV: $$(uv --version)"
	@echo "Python: $$(uv run python --version)"
	@echo "Dependencias:"
	@uv pip list | head -10

# Comandos específicos del proyecto
extract: ## Ejecutar extracción de datos (alias para run)
	uv run python pdf_extractor.py

quick-start: ## Inicio rápido (setup + run)
	make setup
	make run

# Comandos de desarrollo
dev-setup: ## Configuración completa para desarrollo
	make setup
	make dev-install
	@echo "🎉 Entorno de desarrollo listo"

check-all: ## Ejecutar todas las verificaciones
	make lint
	make type-check
	make test
