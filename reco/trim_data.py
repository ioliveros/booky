import pandas as pd
chunk_size = 10000

# title, genre, rating
chunks = pd.read_json("/kaggle/input/large-books-metadata-dataset-50-mill-entries/books.json/books.json", lines=True, chunksize=chunk_size)
df_list = []
for chunk in chunks:
    df_list.append(chunk)
    if len(df_list) >= 2:
        break

df_books = pd.concat(df_list, ignore_index=True)
df_books.to_json('books.json', orient='records', lines=True)