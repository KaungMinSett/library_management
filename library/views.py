from django.shortcuts import render
from django.template import loader
from .models import Book

# Create your views here.
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.core.paginator import Paginator

def book_detail(request, pk):
    book = Book.objects.get(id=pk)

    return render(request, 'book_detail.html', {'book': book,"colors":['amber','sky','cyan','yellow','green'],
})

def book_list(request,pg_no):
    template = loader.get_template('books.html')
    books = Book.objects.all()
    pageObj = Paginator(books,15)
    if(pg_no):
        books = pageObj.page(pg_no)
    else:
        books = pageObj.page(1)

    return HttpResponse(template.render({'books':books},request))