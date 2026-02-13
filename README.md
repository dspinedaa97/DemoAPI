# Proyecto demo básico API Backend en Python

## Para el BanEnd

1. Crear un ambiente virtual: en la terminal escribir python -m venv .myenv
    -activar la venv .\.myenv\Scripts\activate

2. Hacer que github ignore el venv: crear un archivo que se llame .gitignore y escribir en él .myenv

3. Instalar fastapi en la terminal: Crear la API

4. Instalar uvicorn: Montar la API en un servidor

5. En nueva terminal: Entrar a la carpeta BackEnd: cd .\BackEnd y luego python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload