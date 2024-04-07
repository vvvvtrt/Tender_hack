import spacy
from spacy.matcher import Matcher
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import requests
import pymorphy2


NAME_MODEL = "classification_model"

tokenizer = T5Tokenizer.from_pretrained(NAME_MODEL)
model = T5ForConditionalGeneration.from_pretrained(NAME_MODEL)
morph = pymorphy2.MorphAnalyzer()

class NLP_Search:
    def __init__(self, text: str):
        self.nlp_ru = spacy.load("ru_core_news_sm")
        self.nlp_eu = spacy.load("en_core_web_sm")

        self.text = text
        self.stop_world = ["цена", "купить", "отзывы", "сколько", "характеристики", "обзор"]

    def search_all(self) -> dict:
        ans_dict = {}

        ans_dict["name"] = ""
        ans_dict["categories"] = self.classification()
        ans_dict["country"] = self.search_country()
        ans_dict["company"] = self.search_company()
        ans_dict["model"] = self.search_model(ans_dict["company"])
        ans_dict["units"] = self.search_units()

        return ans_dict

    def search_company(self) -> str:
        ans = ""

        for nlp in [self.nlp_ru, self.nlp_eu]:
            doc = nlp(self.text)

            for entity in doc.ents:
                if entity.label_ in ["PERSON", "ORG"]:
                    ans += entity.text + " "

        return ans

    def get_suggestions(self, keyword):
        url = "https://suggestqueries.google.com/complete/search"
        params = {
            "client": "firefox",
            "q": keyword
        }

        response = requests.get(url, params=params)
        suggestions = response.json()[1]  # Здесь получаем список подсказок

        return suggestions

    def recursion(self, s, ttl=2):
          if not ttl:
              return []

          for i in self.stop_world:
              if i in s:
                  return []

          suggestions = self.get_suggestions(s)
          # print(suggestions)
          ans = [s] + suggestions
          for i in suggestions:
              ans += self.recursion(i, ttl - 1)

          return ans

    def search_model(self, company: str) -> str:
          tir = [set() for i in range(15)]

          for i in self.recursion(company.lower()):
              new = i.split()

              for j in range(len(new)):
                  tir[j].add(new[j])


          text = self.text.lower()
          text_n = list(text.split())
          for i in range(len(text_n)):
              text_n.append("" if self.initial(text_n[i]) == "none" else self.initial(text_n[i]))

          ans = ""
          for level in range(len(tir)):
              for i in tir[level]:
                  sec = self.initial(i)

                  if i in text_n and i not in ans:
                      ans += i + " "
                      break
                  
                  if sec in text_n and i not in ans:
                      ans += sec + " "
                      break

          ans = ans.replace(company.lower(), "")
          return ans

    def initial(self, word):
        parsed_word = morph.parse(word)[0]
        if parsed_word.is_known:
            normal_form = parsed_word.normal_form
            return normal_form
        return "none"


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
    print(NLP_Search("""Телевизор LG 65UP81006LA.ARU 65""").search_all())
