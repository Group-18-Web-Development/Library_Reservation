from django.shortcuts import render
from django.http import HttpResponse

from Account_App.models import User


def test(request):
    return HttpResponse("创建成功!!!")
