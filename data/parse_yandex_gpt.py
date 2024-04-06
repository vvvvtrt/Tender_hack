import requests
import os
from dotenv import load_dotenv

load_dotenv()

FOLDER_ID = os.environ.get("FOLDER_ID")
API_KEY = os.environ.get("API_KEY")

prompt = {
    "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite/latest",
    "completionOptions": {
        "stream": False,
        "temperature": 0.1,
        "maxTokens": "100"
    },
    'messages': [
        {
            'role': "system",
            'text': "перефразируй плохо"
        },
        {
            'role': "user",
            'text': "Фигурка Ника золотая на мраморе 16см с шильдом"
        }
    ]
}

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {API_KEY}"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)
