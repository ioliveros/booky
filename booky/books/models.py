from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publish_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_books = models.ManyToManyField(Book, related_name='fans', blank=True)

    def __str__(self) -> str:
        return self.user.username
    

