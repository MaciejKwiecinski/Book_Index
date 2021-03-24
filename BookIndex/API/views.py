from rest_framework.response import Response
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import filters
from BookIndex.models import Book


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['published_date', 'authors']
    ordering_fields = ['published_date', 'authors']


class DocsView(APIView):
    def get(self, request):
            apidocs = {
                   'API Book List': request.build_absolute_uri('books/'),
                   }
            return Response(apidocs)