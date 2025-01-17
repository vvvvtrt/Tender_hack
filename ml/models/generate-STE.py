# добавить свою модель

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

NAME_MODEL = "cointegrated/rut5-base-multitask"

tokenizer = T5Tokenizer.from_pretrained(NAME_MODEL)
model = T5ForConditionalGeneration.from_pretrained(NAME_MODEL)

def generate(text):
    inputs = tokenizer(text, return_tensors='pt')

    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5)

    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


if __name__ == '__main__':
    print(generate(""))
