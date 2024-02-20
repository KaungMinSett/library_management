from django.db import models
import datetime
# Create your models here.
from django.db import models


    
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    isbn = models.CharField(max_length=13, unique=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    

    def __str__(self):
        return self.name

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(auto_now_add = False, auto_now = False, default=datetime.date.today() + datetime.timedelta(days=1))
    count = models.IntegerField(default=1)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title + " borrowed by " + self.customer.name

