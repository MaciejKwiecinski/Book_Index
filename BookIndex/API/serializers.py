from rest_framework import serializers
from BookIndex.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']