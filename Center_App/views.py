from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'main/homepage.html')


def personal_center(request):
    return render(request, 'main/personal_center.html')
