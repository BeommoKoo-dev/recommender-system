from keybert import KeyBERT

fin = open("test1.txt", "r")

summary = fin.readlines()

wordCount = 10

kw_model = KeyBERT()
keywords = kw_model.extract_keywords(summary, top_n=wordCount)

keyList = []
for keyword in keywords:
    keyList.append(keyword[0])

print(keyList)
