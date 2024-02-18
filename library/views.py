from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})