from rest_framework import serializers
from .models import Author, Book, UserProfile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, APIException

DEFAULT_FAVORITE_BOOKS_MAX = 20

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
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    favorite_books = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        many=True,
        write_only=True
    )
    favorite_books_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def validate(self, data):

        favorite_books = self.initial_data.get('favorite_books', [])
        if len(favorite_books) > DEFAULT_FAVORITE_BOOKS_MAX:
            raise serializers.ValidationError(f"You cannot have more than {DEFAULT_FAVORITE_BOOKS_MAX} favorite books.")

        return data

    def create(self, validated_data):
        favorite_books = validated_data.pop('favorite_books', [])
        user_profile = super().create(validated_data)
        user_profile.favorite_books.set(favorite_books)
        return user_profile
    
    def update(self, instance, validated_data):
        favorite_books = validated_data.pop('favorite_books', None)
        if favorite_books is not None:
            instance.favorite_books.set(favorite_books)
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['favorite_books'] = BookSerializer(instance.favorite_books.all(), many=True).data
        return representation


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