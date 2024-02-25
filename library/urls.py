from django.urls import path

from . import views
app_name = 'library'
urlpatterns = [
    path("<int:pg_no>/",views.book_list,name='book_list'),
    path("detail/<int:pk>/",views.book_detail,name='book_detail')
]