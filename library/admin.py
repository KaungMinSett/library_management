from django.contrib import admin
import datetime

# Register your models here.
from .models import Author, Book, Customer, Genre, Record

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn', 'count', 'get_genres')
    search_fields = ('title', 'author__name')
    list_filter = ('author', 'publication_date', 'genre')
   
    ordering = ('-publication_date',)
    
    def get_genres(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])
    
    get_genres.short_description = 'Genres'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    search_fields = ('name',)
    ordering = ('name',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'customer', 'issue_date', 'due_date', 'count', 'returned')
    search_fields = ('book__title', 'customer__name')
    list_filter = ('book', 'customer', 'returned')
    date_hierarchy = 'issue_date'
    ordering = ('-issue_date','customer__name')
    list_per_page = 15
    list_max_show_all = 20

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.issue_date = datetime.date.today()
            obj.return_date = obj.issue_date + datetime.timedelta(days=5)
           
        super().save_model(request, obj, form, change)
    


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_book')
    search_fields = ('name',)
    
    def get_book(self, obj):
        return ', '.join([book.title for book in obj.book_set.all()])
    
    get_book.short_description = 'Books'


admin.site.register(Author)
admin.site.register(Book, BookAdmin)   
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Genre)
admin.site.register(Record, RecordAdmin)
