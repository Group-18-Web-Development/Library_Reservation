from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from Account_App.models import User


def test(request):
    return HttpResponse("创建成功!!!!!!")


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Wellcome You. You hava been authenticated successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invaild login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "Account_App/login.html", {"form": login_form})
