from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'POST':
        # Process the POST request and create a new book
        # Validate and save the book data to the database
        book_data = request.data
        # Add logic here to save the book data in the database
        return Response(book_data, status=status.HTTP_201_CREATED)
