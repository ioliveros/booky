## Booky
----
booky is an app that let's you add your favorite authors and books. It has a recommendation system as you add your books to your favorite list.


It uses a naive approach of `KNN` implementation and was trained from the [large books](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download) dataset

### Overview

![Screen Shot 2024-08-20 at 2 43 44 AM](https://github.com/user-attachments/assets/e1359b4e-ad79-4a55-8537-15816052aff8)

----
#### How did I train the model?
simple, I used the `book.json` dataset and trimmed the data on google colab [here](https://www.kaggle.com/code/ioliveros/book-recommender-genre)

To train from the given data, I fit the training to just two features 
`Genres` - used `MultiLabelBinarizer` to convert the list of genres for each book into a binary feature vector, and then `Average Rating` -  (thanks ChatGPT!)

--- 
#### Running Django (Main API)

```bash
pip install > requirements.pip
python3 -m venv env
source env/bin/activate

python3 manage.py runserver
```
django server
```
❯ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
August 19, 2024 - 19:01:24
Django version 4.2.15, using settings 'booky.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---
#### Running Flask (recommender microservice) 

#### NOTE: 
there are pre-requisites to run the recommender service, you need to have the ff. metadata
```bash
knn_model.pkl
mlb.pkl
books.json
```

```bash
pip install > requirements.pip
```
If all is good, just do `flask run` and you should be good

flask server
```bash
❯ flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```