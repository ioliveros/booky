from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, UserProfileViewSet, RegisterView
# AddFavoriteBookView, RemoveFavoriteBookView

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view(), name='register'),
    # path('favorites/add/', AddFavoriteBookView.as_view(), name='add-favorite-book'),
    # path('favorites/remove/', RemoveFavoriteBookView.as_view(), name='remove-favorite-book'),
]
