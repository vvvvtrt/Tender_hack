from backend.core.utils import existence_check
from backend.core.utils import nlp_search
from backend.core.utils import spell_text
from fastapi import APIRouter, HTTPException


def processing(name):
    text = spell_text.spell_text(name)
    if existence_check.Existence_Check(text).check_text():
        return nlp_search.NLP_Search(text).search_all()
    else:
        raise HTTPException(status_code=418, detail="data isn't correct")