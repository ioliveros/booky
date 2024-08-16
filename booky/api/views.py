from django.db.utils import IntegrityError
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Author, Book, UserProfile
from .serializers import AuthorSerializer, BookSerializer, UserProfileSerializer, RegisterSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e: 
            return Response(
                {"detail": "UserProfile already exists for this user."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        suggested_books = self.get_suggested_books(instance)
        response_data = serializer.data
        response_data['suggested_books'] = suggested_books
        return Response(response_data)
    
    def get_suggested_books(self, user_profile):
        suggested_books = Book.objects.exclude(id__in=user_profile.favorite_books.values_list('id', flat=True))[:5]
        return [1, 2, 3]
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'description', 'author__name')
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "author_id cannot be null or invalid."}, 
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
