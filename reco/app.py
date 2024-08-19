from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

books_df = pd.read_json('books.json', orient='records', lines=True)

with open('models/mlb.pkl', 'rb') as f:
    mlb = pickle.load(f)

with open('models/knn_model.pkl', 'rb') as f:
    knn = pickle.load(f)

def create_query_vector(genres):
    query_genre_features = mlb.transform([genres])
    query_vector = np.hstack([query_genre_features, np.array([[0]])])
    return query_vector

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    query_genres = data.get('genres', [])
    query_title = data.get('title', None)
    
    if not query_genres:
        return jsonify({'error': 'No genres provided'}), 400
    
    query_vector = create_query_vector(query_genres)
    distances, indices = knn.kneighbors(query_vector)
    recommended_books = books_df.iloc[indices[0]]
    
    # Exclude books with the provided title
    if query_title:
        recommended_books = recommended_books[recommended_books['title'] != query_title]
    
    # Convert to list of dictionaries
    result = recommended_books[['title', 'average_rating', 'author_name']].to_dict(orient='records')
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
