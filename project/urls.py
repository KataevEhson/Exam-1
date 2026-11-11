from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', add_author, name="add_author"),    
    path('add_book', add_book, name="add_book"),  
    path('add_order', add_order, name='add_order') , 
    path('show_books', show_book, name='show_books') , 
]
