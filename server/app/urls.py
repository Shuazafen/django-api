from django.urls import path
from .import views
urlpatterns = [
    path('', views.book, name="book"),
    path('category', views.category, name="category"),
    path('author', views.author, name="author")]