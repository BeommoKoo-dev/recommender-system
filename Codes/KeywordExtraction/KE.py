from keybert import KeyBERT
import json
import csv
import spacy

# How To Use
# 1. Change user parameters
# 2. Check jsonFilePath and csvFilePath below
# 3. File will be made in current path

# User Parameters
movieCount = 200  # How many movies from .json
wordCount = 12  # How many keywords for each movie

# Data Structures and Models
movies = []
synopsis = []
rows = []
kw_model = KeyBERT()
sp_model = spacy.load("en_core_web_sm")

# Reading .json
jsonFilePath = "movie_data.json"
with open(jsonFilePath, 'r', encoding='utf-8') as jsonFile:
    movieReader = (json.loads(line) for line in jsonFile)

    count = 0
    for movieData in movieReader:
        if count >= movieCount:
            break
        if count % 10 == 0:
            print(f'Reading File.. ({count}/{movieCount})')

        movieID = movieData.get('movie_id', '')
        movies.append(movieID)

        movieSummary = movieData.get('plot_synopsis', '')
        keywords = kw_model.extract_keywords(movieSummary, top_n=wordCount)
        keyList = [keyword[0] for keyword in keywords]

        filtered_keywords = []
        for keyword in keyList:
            doc = sp_model(keyword)
            is_name = any(token.ent_type_ == "PERSON" and token.ent_iob_ != '0' for token in doc)

            if not is_name:
                filtered_keywords.append(keyword)

        keyString = ', '.join(filtered_keywords)
        synopsis.append(keyString)

        count += 1

# Writing .csv
csvFilePath = "name_remove_keywords.csv"
with open(csvFilePath, 'w', newline='', encoding='utf-8') as csvFile:
    headers = ['MovieID', "Keywords"]
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()

    for idx in range(0, movieCount):
        writer.writerow({'MovieID': movies[idx], 'Keywords': synopsis[idx]})
