# Запуск приложения

## Run local

- For install all requirements after creating a virtual environment (`venv`)

    ```bash
    pip install -r requirements.txt
    ```

- For work in network

    ```bash
    uvicorn backend.main:app --reload --port 8000 --host 0.0.0.0
    ```
- For work in local machine

    ```bash
    uvicorn backend.main:app --reload --port 8000 --host localhost
    ```
