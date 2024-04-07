# from backend.core.utils import nlp_search
from backend.core.utils import existence_check
from backend.core.utils import spell_text
from backend.env import ML_URI
from fastapi import HTTPException
import requests

body = {
    "text": ""
}

headers = {
    "Content-Type": "application/json"
}


def processing(name):
    text = spell_text.spell_text(name)
    body["text"] = text
    if existence_check.Existence_Check(text).check_text():
        response = requests.post(ML_URI, json=body, headers=headers)
        return response.json()
    else:
        raise HTTPException(status_code=418, detail="Data isn't correct!")
