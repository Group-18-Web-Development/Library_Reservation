from django.shortcuts import render
from Account_App.models import UserProf
from django.http import HttpResponse


def homepage(request):
    return render(request, 'main/homepage.html')


def personal_center(request):
    user_id = request.session.get('user_id')
    userprof = UserProf.objects.get(pk=1)
    data = {
        'icon': '../../static/uploads/' + userprof.icon.url,
        'name': userprof.name,
        'student_number': userprof.student_number,
        'phone_number': userprof.phone_number,
        'mailbox': userprof.mailbox,
        'introduction': userprof.introduction,
        'record_id_new': None,  # 待完成
        # 记录id（待完成）
        'credit': userprof.credit
        # 不良记录id（待完成）
    }
    return render(request, 'main/personal_center.html', context=data)
