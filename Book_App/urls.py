from django.urls import path, re_path

from Book_App import views

app_name = '[Book_App]'
urlpatterns = [
    path('books/', views.books, name='books'),
    path('bookrecord/', views.book_record, name='book_record'),
]