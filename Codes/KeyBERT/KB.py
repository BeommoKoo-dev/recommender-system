from keybert import KeyBERT

fin = open("test1.txt", "r")

summary = fin.readlines()

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(summary)

print(keywords)
