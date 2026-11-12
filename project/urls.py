from django.urls import path
from .views import *

urlpatterns = [
    path('', add_author, name="add_author"),    
    path('edit_order/<int:id>/', edit_order, name='edit_order'),
    path('edit_book/<int:id>/', edit_book, name='edit_book'),
    path('edit_author/<int:id>/', edit_author, name='edit_author'),
    path('show_orders', show_orders, name='show_orders'),
    path('orders/<int:id>/', order_more_info, name='order_more_info'),
    path('book/<int:id>/', book_more_info, name='book_detail'),
    path('add_book', add_book, name="add_book"),  
    path('add_order', add_order, name='add_order') , 
    path('show_books', show_book, name='show_books') , 
    path('authors', show_authors, name='show_authors'),
    path('authors/<int:id>/', author_more_info, name='author_more_info'),

     
]
