## Booky
----
booky is an app that let's you add your favorite authors and books. It has a recommendation system as you add your books to your favorite list.


It uses a naive approach of `KNN` implementation and was trained from the [large books](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download) dataset

### Overview

![Screen Shot 2024-08-20 at 2 43 44 AM](https://github.com/user-attachments/assets/e1359b4e-ad79-4a55-8537-15816052aff8)

----
#### How did I train the model?
simple, I used the `books.json` dataset and trimmed the data on google colab [here](https://www.kaggle.com/code/ioliveros/book-recommender-genre) or just refer to [this](https://github.com/ioliveros/booky/blob/main/reco/knn.py) code

To train from the given data, I fit the training to just two features 
`Genres` - used `MultiLabelBinarizer` to convert the list of genres for each book into a binary feature vector, and then `Average Rating` -  (thanks ChatGPT!)

--- 
#### Running Django (Main API)

```bash
cd booky
pip install > requirements.pip
python3 -m venv env
source env/bin/activate
python3 manage.py runserver
```
#### django server
```
❯ python manage.py runserver
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
--- 
#### ORM Schema and Authentication
DB Schema is straightforward, I used 3 additional entity tables-- Authors, Books and UserProfile. I reused the built-in User and `rest_framework_simplejwt` for JWT token implementation

![Screen Shot 2024-08-20 at 3 22 18 AM](https://github.com/user-attachments/assets/466e369f-2da2-428c-9653-ba33510d5fba)


#### How to obtain a JWT token?

Register
```bash
curl --location 'http://localhost:8000/api/register' \
--form 'username="ioliveros"' \
--form 'email="foo@bar.com"' \
--form 'password="xxxxx"' \
--form 'first_name="Ian"' \
--form 'last_name="Dev"'
```
Get Access Token
```bash
curl --location 'http://localhost:8000/api/token/' \
--form 'username="ioliveros"' \
--form 'password="xxxxx"' \
--form 'email="foo@bar.com""'
```
You should be able to get a `refresh` and `access` token
```bash
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2xxx",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2xxx"
}
```
How do I used the token?
```
curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2xxx' \
--form 'title="Harry Potter and the Prisoner of Azkaban"' \
--form 'author="1"' \
--form 'description="Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author J. K. Rowling and is the third in the Harry Potter series. The book follows Harry Potter, a young wizard, in his third year at Hogwarts School of Witchcraft and Wizardry. Along with friends Ronald Weasley and Hermione Granger, Harry investigates Sirius Black, an escaped prisoner from Azkaban, the wizard prison, believed to be one of Lord Voldemort'\''s old allies."' \
--form 'publish_date="1999-07-08"'
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
cd reco
pip install > requirements.pip
python3 -m venv env
source env/bin/activate
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
