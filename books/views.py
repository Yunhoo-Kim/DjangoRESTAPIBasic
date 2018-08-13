from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSerializer


class BookCreateReadView(ListCreateAPIView):
    """
    get:
    # Return list of Books

    post:
    # make book instance
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'



