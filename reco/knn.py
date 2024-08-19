import pickle
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import NearestNeighbors

df_books = pd.read_json('books.json', orient='records', lines=True)
filtered_df_books = df_books[['id', 'title', 'author_id', 'author_name', 'author_id', 'average_rating', 'shelves']]
filtered_df_books.rename(columns={'average_rating': 'rating', 'shelves': 'genre'}, inplace=True)

book_data = []
for index, row in filtered_df_books.iterrows():
    genres = [genre['name'] for genre in row['genre']]
    book_data.append({
        'id': row['id'],
        'title': row['title'],
        'author_id': row['author_id'],
        'author_name': row['author_name'],
        'genre': genres,
        'rating': row['rating']
    })


final_books_df = pd.DataFrame(book_data)

mlb = MultiLabelBinarizer()
genre_features = mlb.fit_transform(final_books_df['genre'])

final_books_df['scaled_rating'] = StandardScaler().fit_transform(final_books_df[['rating']])
features = np.hstack([genre_features, final_books_df[['scaled_rating']].values])

print('start training')
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(features)
print('done training')


with open('knn_model.pkl', 'wb') as f:
    pickle.dump(knn, f)

with open('mlb.pkl', 'wb') as f:
    pickle.dump(mlb, f)
