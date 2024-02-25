from django.shortcuts import render
from django.template import loader
from .models import Book,Genre

# Create your views here.
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q


def book_detail(request, pk):
    book = Book.objects.get(id=pk)

    return render(request, 'book_detail.html', {'book': book,"colors":['amber','sky','cyan','yellow','green'],
})

def book_list(request,pg_no):
    template = loader.get_template('books.html')
    query = request.GET.get('query','')
    genre_id = request.GET.get('genre_id',0)
    genres = Genre.objects.all();
    books = Book.objects.all()

    if(genre_id):
        books = books.filter(genre=int(genre_id))
    if(query):
        books = books.filter(Q(title__icontains=query)|Q(description__icontains=query)|Q(author__name__icontains=query))

    pageObj = Paginator(books,15)
    if(pg_no):
        books = pageObj.page(pg_no)
    else:
        books = pageObj.page(1)

    return HttpResponse(template.render({'books':books,'genres':genres,"query":query,"genre_id":int(genre_id)},request))


    

    
    # return HttpResponse(template.render({"books":books,"query":query,'genres':genres,'genre_id':int(genre_id)},request))