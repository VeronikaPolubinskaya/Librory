from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    book = Book()
    book.name = request.data['name']
    book.author = request.data['author']
    book.year = request.data['year']
    book.isbn = request.data['isbn']
    book.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.name = request.data['name']
    book.author = request.data['author']
    book.year = request.data['year']
    book.isbn = request.data['isbn']
    book.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def find_book_by_name(request, book_name):
    book = get_object_or_404(Book, name=book_name)
    serializer = BookSerializer(book)
    return Response(serializer.data)