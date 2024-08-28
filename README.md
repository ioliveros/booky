## Booky
----
booky is an app that let's you curate your favorite authors and books. It has a recommendation system as you add your books to your favorite list.


It uses a naive approach of [KNN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) implementation by scikit-learn and was trained from the [large books](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download) dataset

### Overview

![Screen Shot 2024-08-20 at 10 56 12 PM](https://github.com/user-attachments/assets/6a9f2c23-c466-4ca0-8c7d-7bd06a3738a3)

----
#### How did I train the model?
simple, I used the `books.json` dataset and trimmed the data on google colab [here](https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/book-recommender-genre-db86f289-8f8b-4e2f-819c-3bdd0065860e.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20240820/auto/storage/goog4_request%26X-Goog-Date%3D20240820T120756Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D32e317c3a8a23ef90035f0eb204b7a3deab6b33b27c0e8e770c10957d1f13977abf2b2298c23a9af06c5ddf855ebedfb3c1081f8caa7e1ec26f262d602c7e65d353b39e316754af2ae660202ff16b0a7ab5ff45346ba201ef234eaf733b239b9be83a7657f5f65e6e0345a789ec90d7e9cf71835c63a7273a185f43bbecdd3fa1d1d9914b96d651f8f4246234bb44e8aee2b773fd3ca46a388ba39945987780a5088e525e8e45517970e5a28384a0326d4e9f65af8b609a9e88b81e8ad7974a676125837ff825d12a0f70650465667edc2970a9a38238e041bdbfcf4efad62f52500cd9468074448cdda3bfe38773d86c14a77121bb5dc2b2a600f9d83bdfe6b) or just refer to [this](https://github.com/ioliveros/booky/blob/main/reco/knn.py) code, or try kaggle [here](https://www.kaggle.com/code/ioliveros/book-recommender-genre/edit/run/193223663)

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
#### create a superadmin first
```bash
(booky) python manage.py createsuperuser
```
### populating the books and authors entities
```bash
cd bin/
./create_user.sh
./add_authors.sh
./add_books.sh
```
Then you should be good to go and ready to use the BookyAPI
#### django server
```
❯ python manage.py runserver
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Quick verification for DjangoAdmin

Authors
![Screen Shot 2024-08-20 at 11 17 30 PM](https://github.com/user-attachments/assets/4b8f4867-67f2-4992-b807-6498e8644be0)

Books
![Screen Shot 2024-08-20 at 11 17 45 PM](https://github.com/user-attachments/assets/35326035-2cbf-44f2-a20a-8db7f6bfed70)

---

#### ORM Schema and Authentication
DB Schema is straightforward, I used 3 additional entity tables-- Authors, Books and UserProfile. I reused the built-in [auth.models.User](https://docs.djangoproject.com/en/5.1/ref/contrib/auth/) and [rest_framework_simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for JWToken implementation, for the CRUD operations I extended the [viewsets.ModelViewSet](https://www.django-rest-framework.org/api-guide/viewsets/) for some model, but for other just retained as-is, for straightforward implementation.

![Screen Shot 2024-08-20 at 3 22 18 AM](https://github.com/user-attachments/assets/466e369f-2da2-428c-9653-ba33510d5fba)


#### How to obtain a JWToken?

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
