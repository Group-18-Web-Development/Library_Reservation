from django.shortcuts import render
from django.http import HttpResponse


def books(request):
    return render(request, 'main/book.html')


def book_record(request):
    return render(request, 'main/book_record.html')
