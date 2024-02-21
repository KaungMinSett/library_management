from django.urls import path

from . import views
app_name = 'books'
urlpatterns = [
    path("",views.index,name='index'),
    path("<int:pg_no>/",views.book_list,name='book_list'),
    path("create/",views.create,name='create')
]