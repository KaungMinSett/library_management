
from django.template import loader
from django.http import HttpResponse
import requests
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from library.models import Author, Book,Genre

from .forms import EditBookForm, NewBookForm

# Create your views here.
def book_list(request,pg_no):
    template = loader.get_template('books/books.html')
    url = 'https://freetestapi.com/api/v1/books?limit=50' #fake book list api
    response = requests.get(url)
    books = None
    pageObj = None
    if response.status_code == 200:
        books = response.json()
    if books != None:
        pageObj = Paginator(books,15)
    if(pg_no):
        books = pageObj.page(pg_no)
    else:
        books = pageObj.page(1)

    return HttpResponse(template.render({'books':books},request))

def index(request,):
    ## load template 
    ## make request
    ##
    template = loader.get_template('books/books.html')
    url = 'https://freetestapi.com/api/v1/books?limit=50'
    response = requests.get(url)
    books = None
    pageObj = None
    if response.status_code == 200:
        books = response.json()
    if books != None:
        pageObj = Paginator(books,15)
        books = pageObj.page(1)

    

    return HttpResponse(template.render({'books':books},request))

def create(request):
    
    if(request.method=="POST"):
        form = NewBookForm(request.POST,request.FILES)
        if(form.is_valid()):
            book = form.save(commit=False)
            book.save()
            book_id=book.id
            print(book,"THisiscreated")
            return redirect("books:edit",pk=book_id)
    else:
        form = NewBookForm()
    template = loader.get_template('books/form.html')
    return HttpResponse(template.render({'form':form,"title":'New Book'},request))

def edit(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if(request.method=="POST"):
        form = EditBookForm(request.POST,request.FILES,instance=book)
        if(form.is_valid()):
            form.save()
            return redirect("book:book_list",pg_no=1)
    else:
        form = NewBookForm(instance=book)
    template = loader.get_template('book/form.html')
    return HttpResponse(template.render({'form':form,"title":'Edit Book'},request))