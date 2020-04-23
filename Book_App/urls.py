from django.urls import path, re_path

from Book_App import views

app_name = '[Book_App]'
urlpatterns = [
    path('book_seat/', views.book_seat, name='book_seat'),
    path('book_record/', views.book_record, name='book_record'),
    path('book_cancel/', views.book_cancel, name='book_cancel'),
]
