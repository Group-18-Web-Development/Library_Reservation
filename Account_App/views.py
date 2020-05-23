from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm, RegistrationForm, UserProfForm

from .help_function import add_data_help


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
    add_data_help()
    return HttpResponse('用户、座位添加成功')

