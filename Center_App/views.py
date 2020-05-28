from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from Account_App.models import UserProf


def homepage(request):
    return render(request, 'main/homepage.html')


def personal_center(request):
    # 判断用户是否已经登录
    try:
        user_id = request.session.get('user_id')*1
    except Exception:
        return redirect(reverse('account:user_login'))

    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    userprof = UserProf.objects.get(user_id=user_id)

    if request.method == 'POST':
        icon = request.FILES.get('icon')
        userprof.icon = icon
        userprof.save()

    msg = ""
    if userprof.credit == 0:
        msg = "您的信誉分过低，无法继续预约，请联系管理员！"
    data = {
        'icon': '../../static/uploads/' + userprof.icon.url,
        'name': user.username,
        'phone_number': userprof.phone_number,
        'mailbox': userprof.user.email,
        'credit': userprof.credit,
        'msg': msg,
    }
    return render(request, 'main/personal_center.html', context=data)
