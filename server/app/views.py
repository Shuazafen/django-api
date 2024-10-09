from django.shortcuts import render
from django.http import Http404
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# @api_view()
# def book_list(request):
#     return Response({"message":"hello, world!"})


# @api_view(["GET"])
# def book(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# def book_id(request, book_id):
#     book = 