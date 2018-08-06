from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'author_name', 'price')


class UserSerializer(serializers.ModelSerializer):

   class Meta:
       model = User
       fields = ("id", "username", "email", "password")
