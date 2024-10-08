from django.db.utils import IntegrityError
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Author, Book, UserProfile
from .serializers import AuthorSerializer, BookSerializer, UserProfileSerializer, RegisterSerializer, UserSerializer

import requests
import json
import traceback

RECOMMENDER_SERVICE = 'http://reco-service:8888/suggested_books'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e: 
            return Response(
                {
                    "detail": "UserProfile already exists for this user.",
                    "error": traceback.format_exc()
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = serializer.data

        is_reco = request.query_params.get('reco', None)
        print("is_reco >> ", is_reco)
        if request.query_params.get('reco', None):
            suggested_books = self.get_suggested_books(instance, serializer)
            if suggested_books:
                response_data['suggested_books'] = suggested_books
            else:
                response_data['suggested_books'] = [] 

        return Response(response_data)
    
    def get_suggested_books(self, instance, serializer):
        genres = [item['genre'].lower() for item in serializer.data['favorite_books']]
        titles = [item['title'].lower() for item in serializer.data['favorite_books']]
        if len(titles) > 0:
            pick_title = titles[0] 
            with requests.Session() as client:
                payload = json.dumps({"genres": genres, "title": pick_title})
                response = client.post(RECOMMENDER_SERVICE, headers={'content-type': 'application/json'}, data=payload)
            return response.json()

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
