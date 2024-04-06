FROM python:3.12-alpine

WORKDIR /app

COPY backend/requirements.txt requirements.txt

RUN ["pip3", "install", "-r", "requirements.txt"]

COPY backend .

ENTRYPOINT ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]