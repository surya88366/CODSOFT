import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Movie1': [5, 4, 0, 0, 3],
    'Movie2': [0, 4, 0, 0, 1],
    'Movie3': [2, 0, 1, 4, 0],
    'Movie4': [0, 2, 0, 5, 4],
    'Movie5': [4, 0, 3, 0, 0]}

ratings_df = pd.DataFrame(data)

def collaborative_filtering_svd(ratings_df, n_components=2):
    ratings_matrix = ratings_df.iloc[:, 1:].values
    svd = TruncatedSVD(n_components=n_components, random_state=42)
    svd.fit(ratings_matrix)
    Vt = svd.components_
    user_ratings_reduced = ratings_matrix @ Vt.T
    return user_ratings_reduced
def get_recommendations(user_id, ratings_df, user_ratings_reduced, top_n=3):
    user_ratings = user_ratings_reduced[user_id]
    ranked_movies = np.argsort(user_ratings)[::-1]
    seen_movies = ratings_df.columns[1:][ratings_df.iloc[user_id, 1:] > 0]
    recommendations = [movie for movie in ratings_df.columns[1:][ranked_movies] if movie not in seen_movies][:top_n]
    return recommendations

user_ratings_reduced = collaborative_filtering_svd(ratings_df)

user_id = 3  # User4
recommendations = get_recommendations(user_id, ratings_df, user_ratings_reduced)
print(f"Recommendations for User{user_id + 1}: {recommendations}"




