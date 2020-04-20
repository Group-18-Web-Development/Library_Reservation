from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'C:/Users/wujiahao/Documents/Library_Reservation/templates/homepage.html')