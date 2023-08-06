import yake
import random


def extract_keywords(text, language, n):
    extractor = yake.KeywordExtractor(lan=language, n=n)
    keywords = extractor.extract_keywords(text)
    return keywords


lang = 'en'
kw_length = 1
n_words = 5

with open("input.txt", "r") as fin:
    text = fin.read()

extracted = []

for i in range(n_words):
    keywords = extract_keywords(text, lang, kw_length)
    keyword, score = random.choice(keywords)
    extracted.append((keyword, score))

for keyword, score in extracted:
    print(f"Keyword: {keyword}, Score: {score}")
