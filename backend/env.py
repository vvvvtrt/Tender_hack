import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_PORT = os.environ.get("BACKEND_PORT")

ML_HOST = os.environ.get("ML_HOST")
ML_PORT = os.environ.get("ML_PORT")
ML_URI = f"http://{ML_HOST}:{ML_PORT}/get_nlp_search"

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

# driver://user:pass@localhost/dbname
POSTGRES_URI = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
