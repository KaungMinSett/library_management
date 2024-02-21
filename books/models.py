from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering=('name',)
        verbose_name_plural="Genres"

    def __str__(self):
        return self.name

class Book(models.Model):
      title = models.CharField(max_length=255)
      author_id = models.ForeignKey(User,related_name='author',on_delete=models.CASCADE)
      isbn = models.CharField(max_length=255)
      genre_id = models.ForeignKey(Genre,related_name='books',on_delete=models.CASCADE)
      description = models.TextField(blank=True,null=True)
      published_year = models.DateTimeField()
      count = models.IntegerField(default=0)
    #   price = models.FloatField()
      image_url = models.ImageField(upload_to="media/books/",blank=True,null=True)
      created_by = models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
        ordering=('title',)
        # verbose_name_plural="Books"

      def __str__(self):
           return self.name