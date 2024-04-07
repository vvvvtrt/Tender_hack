import pymorphy2
import nltk
from nltk.corpus import wordnet

morph = pymorphy2.MorphAnalyzer()
nltk.download('wordnet')


class Existence_Check:
    def __init__(self, text: str):
        self.text = text

        self.true_words = 0
        self.all = 0

    def check_text(self) -> bool:
        text = self.delete_comma(self.text).split()
        self.all = len(text)

        for i in text:

            if self.check_ru(i) or self.check_eu(i):
                self.true_words += 1

        return self.true_words / self.all >= 0.7

    def check_ru(self, word) -> bool:
        parsed_word = morph.parse(word)
        if parsed_word[0].is_known:
            return True
        else:
            return False

    def check_eu(self, word) -> bool:
        if wordnet.synsets(word):
            return True
        else:
            return False

    def delete_comma(self, text: str) -> str:
        text = text.replace(",", " ").replace("-", " ").replace('"', " ").replace(".", " ")
        return text
