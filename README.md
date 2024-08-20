## Booky
----
booky is an app that let's you curate your favorite authors and books. It has a recommendation system as you add your books to your favorite list.


It uses a naive approach of `KNN` implementation and was trained from the [large books](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download) dataset

### Overview

![Screen Shot 2024-08-20 at 2 43 44 AM](https://github.com/user-attachments/assets/e1359b4e-ad79-4a55-8537-15816052aff8)

----
#### How did I train the model?
simple, I used the `books.json` dataset and trimmed the data on google colab [here](https://www.kaggle.com/code/ioliveros/book-recommender-genre) or just refer to [this](https://github.com/ioliveros/booky/blob/main/reco/knn.py) code

To train from the given data, I fit the training to just two features 
`Genres` - used `MultiLabelBinarizer` to convert the list of genres for each book into a binary feature vector, and then `Average Rating` -  (thanks ChatGPT!)

--- 
#### Running Django (Booky API)

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
#### How to use the token?
Add Author
```
curl --location 'http://localhost:8000/api/authors/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2xxx' \
--form 'name="Dan Brown"' \
--form 'biography="American author best known for his thriller novels, including the Robert Langdon novels Angels & Demons (2000), The Da Vinci Code (2003), The Lost Symbol (2009), Inferno (2013), and Origin (2017). His novels are treasure hunts that usually take place over a period of 24 hours."'
```
Add Book
```
curl --location 'http://localhost:8000/api/books/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2xxx' \
--form 'title="Digital Fortress"' \
--form 'author="1"' \
--form 'genre="thriller"' \
--form 'description="The book explores the theme of government surveillance of electronically stored information on the private lives of citizens, and the possible civil liberties and ethical implications of using such technology."' \
--form 'publish_date="1999-07-08"'
```

---
#### Running Flask (Reco Service) 

NOTE: there are pre-requisites to run the recommender service, you need to have the ff. metadata
```bash
knn_model.pkl
mlb.pkl
books.json
```
Running the service
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
Test recommender service
```bash
curl --location 'http://127.0.0.1:5000/recommend' \
--header 'Content-Type: application/json' \
--data '{
    "genres": [
        "favorites",
        "fantasy",
        "action"
    ],
    "title": "Some Book Title"
}'
```
Output
```
[
    {
        "author_name": "Mark Musa",
        "average_rating": 3.67,
        "title": "Advent at the Gates: Dante's Comedy"
    },
    {
        "author_name": "Don Cupitt",
        "average_rating": 3.67,
        "title": "Meaning of It All in Everyday Speech"
    },
    {
        "author_name": "Jeremy Mark Robinson",
        "average_rating": 3.75,
        "title": "Thomas Hardy And John Cowper Powys: Wessex Revisited"
    },
    {
        "author_name": "Peter Boysen",
        "average_rating": 3.79,
        "title": "A Tale of Two Cities"
    },
    {
        "author_name": "Michael W.  Smith",
        "average_rating": 3.8,
        "title": "Freedom"
    }
]
```
