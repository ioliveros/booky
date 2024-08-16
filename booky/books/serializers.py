from rest_framework import serializers
from .models import Author, Book, UserProfile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, APIException

class UnprocessableEntity(APIException):
    status_code = 422
    default_detail = 'Invalid input.'
    default_code = 'unprocessable_entity'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    
    class Meta:
        model = Book
        fields = '__all__'

    def validate_author(self, value):

        if value is None:
            raise ValidationError("author_id is required.")
        
        if not Author.objects.filter(id=value.id).exists():
            raise UnprocessableEntity(detail="Invalid author_id provided.")
        
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    favorite_books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user