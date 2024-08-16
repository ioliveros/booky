from django.contrib import admin
from .models import Book, Author, UserProfile

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'biography')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'publish_date')
    search_fields = ('title', 'genre')
    list_filter = ('author', 'publish_date')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_books_list')

    def favorite_books_list(self, obj):
        return ", ".join([book.title for book in obj.favorite_books.all()])

    favorite_books_list.short_description = 'Favorite Books'
