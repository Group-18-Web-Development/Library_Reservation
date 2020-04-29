from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm, RegistrationForm
from Account_App.models import User
from Book_App.models import Reservation, Seat

import random


def add_data(request):
    # # 添加用户数据
    # for i in range(10):
    #     user = User()
    #     user.username = 'Jason' + str(i)
    #     user.password = '00000' + str(i)
    #     user.email = '123456@gmail.com'
    #     user.save()

    # 添加安静区座位
    # for i in range(50):
    #     seat = Seat()
    #     seat.is_quiet_area = True
    #     seat.floor = i % 5 + 1
    #     seat.area = random.choice(['A', 'B', 'C'])
    #     seat.table_type = random.choice([1, 2, 4])
    #     seat.has_power = random.choice([True, False])
    #     seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i)
    #     seat.save()

    # 添加非安静区座位
    # for i in range(50):
    #     seat = Seat()
    #     seat.is_quiet_area = False
    #     seat.floor = i % 5 + 1
    #     seat.table_type = random.choice([1, 2, 4])
    #     seat.table_position_noisy = str(seat.floor * 100) + '-' + str(i)
    #     seat.save()

    # 添加预约记录
    # for i in range(9):
    #     record = Reservation()
    #     record.account_id = i + 1
    #     record.seat_id = random.randrange(50) + 1
    #     record.time_id = random.choice([1, 2, 3])
    #     record.save()

    return HttpResponse('用户、座位添加成功')


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


def logout(request):
    return redirect(reverse('account:user_login'))


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        return render(request, "Account_App/register.html", {"form": user_form})
