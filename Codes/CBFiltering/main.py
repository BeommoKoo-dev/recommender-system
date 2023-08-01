import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


metadata = pd.read_csv('movies.csv', low_memory=False)
metadata['overview'] = metadata['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(metadata['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_recommendations(title, cosine_sim=cosine_sim, metadata=metadata):
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return metadata['title'].iloc[movie_indices]

recommendations = get_recommendations('The Dark Knight')
print(recommendations)
