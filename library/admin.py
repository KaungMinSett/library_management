from django.contrib import admin

# Register your models here.
from .models import Author, Book, Customer, Genre, Record

admin.site.register(Author)
admin.site.register(Book)   
admin.site.register(Customer)
admin.site.register(Genre)
admin.site.register(Record)
