from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from functools import lru_cache

app = Flask(__name__)

books_df = pd.read_json('dataset/books.json', orient='records', lines=True)

with open('models/mlb.pkl', 'rb') as f:
    mlb = pickle.load(f)

with open('models/knn_model.pkl', 'rb') as f:
    knn = pickle.load(f)

# @lru_cache(maxsize=128)
def create_query_vector(genres):
    query_genre_features = mlb.transform([genres])
    query_vector = np.hstack([query_genre_features, np.array([[0]])])
    return query_vector

@app.route('/suggested_books', methods=['POST'])
def recommend():
    data = request.json
    query_genres = data.get('genres', [])
    query_title = data.get('title', None)
    
    if not query_genres:
        return jsonify({'error': 'No genres provided'}), 400
    
    query_vector = create_query_vector(query_genres)
    distances, indices = knn.kneighbors(query_vector)
    recommended_books = books_df.iloc[indices[0]]
    
    if query_title:
        recommended_books = recommended_books[recommended_books['title'] != query_title]

    result = recommended_books[
        [
            'title', 'average_rating', 'author_name', 
            'description', 'original_publication_date', 
         ]
    ].to_dict(orient='records')
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
