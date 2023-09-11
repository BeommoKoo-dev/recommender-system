from keybert import KeyBERT
import json
import csv

# How To Use
# 1. Change user parameters
# 2. Check jsonFilePath and csvFilePath in line 21, 44
# 3. File will be made in current path

# User Parameters
movieCount = 200  # How many movies from .json
wordCount = 10  # How many keywords for each movie

# Data Structures and Models
movies = []
synopsis = []
rows = []
kw_model = KeyBERT()

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
        keyString = ', '.join(keyList)
        synopsis.append(keyString)

        count += 1

# Writing .csv
csvFilePath = "keyword_extraction.csv"
with open(csvFilePath, 'w', newline='', encoding='utf-8') as csvFile:
    headers = ['MovieID', "Keywords"]
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()

    for idx in range(0, movieCount):
        writer.writerow({'MovieID': movies[idx], 'Keywords': synopsis[idx]})
