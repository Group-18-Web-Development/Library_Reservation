from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm, RegistrationForm, UserProfForm
from Account_App.models import UserProf
from Book_App.models import Reservation, Seat

import random


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                # 保存session记录
                request.session['user_id'] = user.id
                # 登录成功，定向至主页
                return redirect(reverse('center:homepage'))
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invaild login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "Account_App/login.html", {"form": login_form})


def logout(request):

    try:
        user_id = request.session.get('user_id')*1
    except Exception:
        return redirect(reverse('account:user_login'))

    request.session.flush()
    return redirect(reverse('account:user_login'))


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userpro_form = UserProfForm(request.POST)
        if user_form.is_valid() * userpro_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_pro = userpro_form.save(commit=False)
            new_pro.user = new_user
            new_pro.save()
            return redirect(reverse('account:user_login'))
        else:
            return HttpResponse("sorry, your can not register.")
    else:
        user_form = RegistrationForm()
        userpro_form = UserProfForm()

        return render(request, "Account_App/register.html", {"form": user_form, "pro": userpro_form})


def add_data(request):
    # # 添加用户数据
    # for i in range(10):
    #     user = User()
    #     user.username = 'Jason' + str(i)
    #     user.password = '00000' + str(i)
    #     user.email = '123456@gmail.com'
    #     user.save()

    # 添加安静区座位
    # for j in range(5):
    #     for i in range(20):
    #         seat = Seat()
    #         seat.is_quiet_area = True
    #         seat.floor = j + 1
    #         seat.area = 'A'
    #         seat.table_type = random.choice([1, 2, 4])
    #         seat.has_power = random.choice([True, False, False, False])
    #         seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
    #         seat.save()
    #
    # for j in range(5):
    #     for i in range(20):
    #         seat = Seat()
    #         seat.is_quiet_area = True
    #         seat.floor = j + 1
    #         seat.area = 'B'
    #         seat.table_type = random.choice([1, 2, 4])
    #         seat.has_power = random.choice([True, False, False, False])
    #         seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
    #         seat.save()
    #
    # for j in range(5):
    #     for i in range(20):
    #         seat = Seat()
    #         seat.is_quiet_area = True
    #         seat.floor = j + 1
    #         seat.area = 'C'
    #         seat.table_type = random.choice([1, 2, 4])
    #         seat.has_power = random.choice([True, False, False, False])
    #         seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
    #         seat.save()

    # 添加非安静区座位
    # for s in range(5):
    #     for i in range(30):
    #         seat = Seat()
    #         seat.is_quiet_area = False
    #         seat.floor = s+1
    #         seat.table_type = random.choice([1, 2, 4])
    #         seat.table_position_noisy = 'F' + str(seat.floor) + '-' + str(i + 1)
    #         seat.save()

    # 添加预约记录
    # for i in range(9):
    #     record = Reservation()
    #     record.account_id = i + 1
    #     record.seat_id = random.randrange(50) + 1
    #     record.time_id = random.choice([1, 2, 3])
    #     record.save()

    return HttpResponse('用户、座位添加成功')

