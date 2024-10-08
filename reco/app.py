from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from functools import lru_cache

app = Flask(__name__)

books_df = pd.read_json('dataset/df_books_1m.json', orient='records', lines=True)

with open('models/mlb_1m.pkl', 'rb') as f:
    mlb = pickle.load(f)

with open('models/knn_model_1m.pkl', 'rb') as f:
    knn = pickle.load(f)

def create_query_vector(genres, num_features):
    query_genre_features = mlb.transform([genres])
    query_vector = np.hstack([query_genre_features, np.zeros((1, num_features - query_genre_features.shape[1]))])
    return query_vector

@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

@app.route('/suggested_books', methods=['POST'])
def recommend():

    data = request.json
    query_genres = data.get('genres', [])
    query_title = data.get('title', None)
    
    if not query_genres:
        return jsonify({'error': 'No genres provided'}), 400
    
    num_features = knn.n_features_in_

    query_vector = create_query_vector(query_genres, num_features)
    distances, indices = knn.kneighbors(query_vector)
    recommended_books = books_df.iloc[indices[0]]
    
    if query_title:
        recommended_books = recommended_books[recommended_books['title'] != query_title]

    result = recommended_books[
        [
            'title', 
            'rating', 
            'author_name',
            'genre', 
         ]
    ].to_dict(orient='records')
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
