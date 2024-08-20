from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, UserProfileViewSet, RegisterView, UserViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'profile', UserProfileViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterView.as_view(), name='register'),
]
