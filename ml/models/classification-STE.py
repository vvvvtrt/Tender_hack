import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

NAME_MODEL = "classification_model"

tokenizer = T5Tokenizer.from_pretrained(NAME_MODEL)
model = T5ForConditionalGeneration.from_pretrained(NAME_MODEL)

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')

    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)

    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


if __name__ == '__main__':
    print(generate("Удилище спиннинговое Kutbert Warships 2.1 м 5-25 г"))
