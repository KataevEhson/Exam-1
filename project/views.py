from django.shortcuts import render, redirect
from .models import *





def add_author(request):
    if request.method == "POST":
        Author.objects.create(
        name = request.POST['name'],
        age = request.POST['age']
        )
        
        return redirect('add_book')
    return render(request, 'index.html')



def add_book(request):
    if request.method == "POST":
        Books.objects.create(
            name = request.POST['name'],
            author_id = request.POST['author_id']
        )
        return redirect('add_order')
    return render(request, 'index1.html')




def add_order(request):
    if request.method == "POST":
        Order.objects.create(
            cust_name = request.POST['cust_name'],
            book_id = request.POST['book'],
            time = request.POST['time']
        )
        return redirect('show_books')
    return render(request, 'index2.html')




def show_authors(request):
    if request.method == "POST":
        authors=Author.objects.all()
        return render(request, '', {"authors":authors})






def show_book(request):
    if request.method == "POST":
        books=Author.objects.all()
        return render(request, 'show_books.html', {"books":books})





def show_orders(request):
    if request.method == "POST":
        orders=Author.objects.all()
        return render(request, '', {"orders":orders})




