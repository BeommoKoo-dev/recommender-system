from keybert import KeyBERT
import csv

# User Parameters
wordCount = 10  # How many keywords

# Models and Lists
kw_model = KeyBERT()
plots = []

# Reading .csv
with open("movies_test.csv", 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)
header = rows[0]
header.append("keywords")

count = 0
for row in rows[1:]:
    if count % 10 == 0:
        print("in progress..", end='')
        print(f'{count}th row read')
    count += 1

    summary = row[7]
    keywords = kw_model.extract_keywords(summary, top_n=wordCount)
    keyList = []
    for keyword in keywords:
        keyList.append(keyword[0])
    newList = ', '.join(map(str, keyList))
    row.append(newList)

# Writing .csv
with open('movies_test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Keyword extraction complete")
