from django.shortcuts import render, redirect
from django.urls import reverse

from Account_App.models import UserProf
from django.http import HttpResponse


def homepage(request):
    try:
        user_id = request.session.get('user_id')*1
    except Exception:
        return redirect(reverse('account:user_login'))

    return render(request, 'main/homepage.html')


def personal_center(request):
    try:
        user_id = request.session.get('user_id')*1
    except Exception:
        return redirect(reverse('account:user_login'))

    user_id = request.session.get('user_id')
    userprof = UserProf.objects.get(user_id=user_id)

    print(type(user_id))
    icon = userprof.icon

    if request.method == 'POST':
        icon = request.FILES.get('icon')
        userprof.icon = icon
        userprof.save()

    data = {
        # 'icon': icon,
        'icon': '../../static/uploads/' + userprof.icon.url,
        'name': userprof.name,
        'student_number': userprof.student_number,
        'phone_number': userprof.phone_number,
        'mailbox': userprof.user.email,
        'introduction': userprof.introduction,
        'record_id_new': None,  # 待完成
        # 记录id（待完成）
        'credit': userprof.credit
        # 不良记录id（待完成）
    }
    return render(request, 'main/personal_center.html', context=data)
