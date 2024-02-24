from django.urls import path

from . import views
app_name = 'library'
urlpatterns = [
    path("book_detail/<int:pg_no>/",views.book_detail,name='book_detail')
]