import spacy
from spacy.matcher import Matcher
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


NAME_MODEL = "classification_model"

tokenizer = T5Tokenizer.from_pretrained(NAME_MODEL)
model = T5ForConditionalGeneration.from_pretrained(NAME_MODEL)

class NLP_Search:
    def __init__(self, text: str):
        self.nlp_ru = spacy.load("ru_core_news_sm")
        self.nlp_eu = spacy.load("en_core_web_sm")

        self.text = text

    def search_all(self) -> dict:
        ans_dict = {}

        ans_dict["categories"] = self.classification()
        ans_dict["country"] = self.search_country()
        ans_dict["company"] = self.search_company()
        ans_dict["units"] = self.search_units()

        return ans_dict

    def search_company(self) -> str:
        ans = ""

        for nlp in [self.nlp_ru, self.nlp_eu]:
            doc = nlp(self.text)

            for entity in doc.ents:
                if entity.label_ == "ORG":
                    ans += entity.text + " "

        return ans

    def search_country(self) -> str:
        ans = ""

        for nlp in [self.nlp_ru, self.nlp_eu]:
            doc = nlp(self.text)

            for entity in doc.ents:
                if entity.label_ == "GPE":
                    ans += entity.text + " "

        return ans

    def search_units(self) -> list:
        matcher = Matcher(self.nlp_ru.vocab)

        # Создаем шаблоны для совпадения с различными единицами измерения
        pattern1 = [{"TEXT": {"REGEX": "[0-9]+"}}, {"TEXT": {"REGEX": "[а-яА-Я]+"}}]
        pattern2 = [{"TEXT": {"REGEX": "[0-9]+"}}, {"TEXT": {"REGEX": "[а-яА-Я]+"}}, {"LOWER": "/"},
                    {"TEXT": {"REGEX": "[0-9]+"}}]

        matcher.add("UNIT_PATTERN1", [pattern1])
        matcher.add("UNIT_PATTERN2", [pattern2])

        doc = self.nlp_ru(self.text)

        matches = matcher(doc)
        ans = []
        for match_id, start, end in matches:
            unit = doc[start:end].text
            ans.append(unit)

        return ans

    def classification(self):
        inputs = tokenizer(self.text, return_tensors='pt')

        with torch.no_grad():
            hypotheses = model.generate(**inputs, num_beams=5)

        return tokenizer.decode(hypotheses[0], skip_special_tokens=True)




if __name__ == '__main__':
    print(NLP_Search("Конверт стрип, C4, 229x324, офсет, 90 г/м2, 500 штук, белый, внутр запечатка, Ряжская печатная фабрика (упак)").search_all())
