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
        data_f = request.FILES
        data = request.POST

        Books.objects.create(
            name=request.POST['name'],
            author=Author.objects.get(id=data['author_id']),
            picture=data_f['picture']
        )
        return redirect('add_order')
    authors = Author.objects.all()
    return render(request, 'index1.html', {'authors': authors})

# Category.objects.get(id=data["category_id"]).   author_id


def add_order(request):
    if request.method == "POST":
        Order.objects.create(
            cust_name = request.POST['cust_name'],
            book = Books.objects.get(id=request.POST['book']),
            time = request.POST['time']
        )
        return redirect('show_books')
    books = Books.objects.all()
    return render(request, 'index2.html', {'books': books})


def show_authors(request):
    authors = Author.objects.all()
    return render(request, 'show_authors.html', {'authors': authors})


def author_more_info(request, id):
    if request.method == 'POST':
        return delete_author(request, id)
    avtor = Author.objects.get(id=id)
    return render(request, 'avtor.html', {'avtor': avtor})


def delete_author(request, id):
    if request.method == 'POST':
        avtor = Author.objects.get(id=id)
        avtor.delete()
        return redirect('show_authors')

    return redirect('show_authors')


def edit_author(request, id):
    if request.method == 'POST':
        avtor = Author.objects.get(id=id)
        avtor.name = request.POST['name']
        avtor.age = request.POST['age']
        avtor.save()
        return redirect('show_authors')

    return render(request, 'izmenit_avtor.html', {'avtor': avtor})


def show_book(request):
    books = Books.objects.all()
    return render(request, 'show_books.html', {'books': books})


def book_more_info(request, id):
    if request.method == 'POST':
        return delete_book(request, id)
    kniga = Books.objects.get(id=id)
    return render(request, 'kniga.html', {'kniga': kniga})


def delete_book(request, id):
    if request.method == 'POST':
        kniga = Books.objects.get(id=id)
        kniga.delete()
        return redirect('show_books')

    return redirect('show_books')

def edit_book(request, id):
    if request.method == 'POST':
        kniga = Books.objects.get(id=id)
        kniga.name = request.POST['name']
        kniga.author = Author.objects.get(id=request.POST['author_id'])
        kniga.save()
        return redirect('show_books')

    authors = Author.objects.all()
    return render(request, 'izmenit_kniga.html', {'kniga': kniga,'authors': authors})

def show_orders(request):
    orders = Order.objects.all()
    return render(request, 'show_orders.html', {'orders': orders})


def order_more_info(request, id):
    if request.method == 'POST':
        return delete_order(request, id)
    zakaz = Order.objects.get(id=id)
    return render(request, 'zakaz.html', {'zakaz': zakaz})


def delete_order(request, id):
    if request.method == 'POST':
        zakaz = Order.objects.get(id=id)
        zakaz.delete()
        return redirect('show_orders')

    return redirect('show_orders')


def edit_order(request, id):
    if request.method == 'POST':
        zakaz = Order.objects.get(id=id)
        zakaz.cust_name = request.POST['cust_name']
        zakaz.book = Books.objects.get(id=request.POST['book'])
        zakaz.time = request.POST['time']
        zakaz.save()
        return redirect('show_orders')

    books = Books.objects.all()
    return render(request, 'izmenit_zakaz.html', {'zakaz': zakaz, 'books': books})

