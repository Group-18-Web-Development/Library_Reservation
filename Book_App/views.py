from random import choice

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse

from Account_App.models import UserProf
from Book_App.help_function import *
from Book_App.models import Seat, Reservation


def book_seat(request):
    try:
        user_id = request.session.get('user_id') * 1
    except Exception:
        return redirect(reverse('account:user_login'))

    # 座位预约

    # 获取时间（假设能预约7天内的座位）
    days = []
    today = datetime.date.today()
    present_hour = datetime.datetime.now().hour
    days.append(today)
    for i in range(6):
        days.append(today + datetime.timedelta(days=i + 1))

    # 可选择时间点
    time_choices = ["8:00-11:00", "13:00-17:00", "18:00-21:00"]

    if request.method == 'GET':
        context = {
            'days': days,
            'today': today,
            'present_hour': present_hour,
            'time_choices': time_choices,
        }
        return render(request, 'main/book_seat.html', context=context)

    elif request.method == 'POST':

        # 日期格式化 2020年5月1日 → 2020-05-01
        day_not = request.POST.get('day')
        day = date_transform(day_not)
        time_choice = request.POST.get('time_choice')
        zone = request.POST.get('zone')

        # 查询在该时间段所有已被预约的座位，把这些座位id存至result
        result = reservation_search_id(day, time_choice)
        length = len(result)

        # 随机选座处理
        if zone == 'auto_book':
            seats = Seat.objects.all()

            # 对seats_q进行最后的筛选，若这些座位的id在result中出现，则说明该位置已被预约，应剔除
            for i in range(length):
                seats = seats.exclude(id=result[i])

            reservation = Reservation()
            user_id = request.session.get('user_id')
            userprof = UserProf.objects.get(user_id=user_id)

            time_choices = ["8:00-11:00", "13:00-17:00", "18:00-21:00"]
            if time_choice == time_choices[0]:
                reservation.time_id = 1
            elif time_choice == time_choices[1]:
                reservation.time_id = 2
            else:
                reservation.time_id = 3

            # 预约规则函数，若不符合规则，则无法预约
            msg = book_rule(userprof, reservation.time_id, day)
            if msg != "OK":
                return HttpResponse(msg)

            seat = choice(seats)
            reservation.seat_id = seat.id

            reservation.account = userprof

            reservation.date = day

            reservation.is_delete = False

            reservation.save()
            return redirect(reverse('book:book_record'))

        # 安静区/非安静区处理
        elif zone == 'quiet_or_noisy':
            seats = Seat.objects.all()

            # 对seats_q进行最后的筛选，若这些座位的id在result中出现，则说明该位置已被预约，应剔除
            for i in range(length):
                seats = seats.exclude(id=result[i])

            seats_q = seats.filter(is_quiet_area=True)
            seats_n = seats.filter(is_quiet_area=False)
            data = {
                'days': days,
                'today': today,
                'time_choices': time_choices,
                'seats_q': seats_q,
                'seats_n': seats_n,
                'day': day,
                'present_hour': present_hour,
                'time_choice': time_choice,
            }
            return render(request, 'main/book_seat.html', context=data)

        # 安静区处理
        if zone == 'quiet':

            seats_q = Seat.objects.filter(is_quiet_area=True)

            area_q = request.POST.get('area_q')
            has_power_q = request.POST.get('has_power_q')
            floor_q = request.POST.get('floor_q')
            table_type_q = request.POST.get('table_type_q')

            if area_q != 'all':
                seats_q = seats_q.filter(area=area_q)

            if has_power_q == 'yes':
                seats_q = seats_q.filter(has_power=True)
            elif has_power_q == 'no':
                seats_q = seats_q.filter(has_power=False)

            if floor_q == 'F1':
                seats_q = seats_q.filter(floor=1)
            elif floor_q == 'F2':
                seats_q = seats_q.filter(floor=2)
            elif floor_q == 'F3':
                seats_q = seats_q.filter(floor=3)
            elif floor_q == 'F4':
                seats_q = seats_q.filter(floor=4)
            elif floor_q == 'F5':
                seats_q = seats_q.filter(floor=5)

            if table_type_q == '单人桌':
                seats_q = seats_q.filter(table_type=1)
            elif table_type_q == '双人桌':
                seats_q = seats_q.filter(table_type=2)
            elif table_type_q == '四人桌':
                seats_q = seats_q.filter(table_type=4)

            # 对seats_q进行最后的筛选，若这些座位的id在result中出现，则说明该位置已被预约，应剔除
            for i in range(length):
                seats_q = seats_q.exclude(id=result[i])

            if seats_q.exists():
                msg = "有剩余座位"
            else:
                msg = "无剩余座位"

            data = {
                'days': days,
                'today': today,
                'time_choices': time_choices,
                'seats_q': seats_q,
                'day': day,
                'present_hour': present_hour,
                'time_choice': time_choice,
                'msg': msg,
            }
            return render(request, 'main/book_seat.html', context=data)

        # 非安静区处理
        elif zone == 'noisy':

            seats_n = Seat.objects.filter(is_quiet_area=False)

            floor_n = request.POST.get('floor_n')
            table_type_n = request.POST.get('table_type_n')

            if floor_n == 'F5':
                seats_n = seats_n.filter(floor=5)
            elif floor_n == 'F4':
                seats_n = seats_n.filter(floor=4)
            elif floor_n == 'F3':
                seats_n = seats_n.filter(floor=3)
            elif floor_n == 'F2':
                seats_n = seats_n.filter(floor=2)
            elif floor_n == 'F1':
                seats_n = seats_n.filter(floor=1)

            if table_type_n == '四人桌':
                seats_n = seats_n.filter(table_type=4)
            elif table_type_n == '双人桌':
                seats_n = seats_n.filter(table_type=2)
            elif table_type_n == '单人桌':
                seats_n = seats_n.filter(table_type=1)

            # 对seats_q进行最后的筛选，若这些座位的id在result中出现，则说明该位置已被预约，应剔除
            for i in range(length):
                seats_n = seats_n.exclude(id=result[i])

            if seats_n.exists():
                msg = "有剩余座位"
            else:
                msg = "无剩余座位"

            data = {
                'days': days,
                'today': today,
                'time_choices': time_choices,
                'seats_n': seats_n,
                'day': day,
                'present_hour': present_hour,
                'time_choice': time_choice,
                'msg': msg,
            }
            return render(request, 'main/book_seat.html', context=data)


# 将用户选择预约的table id与用户绑定，存至reservation数据库
def book_success(request, table_id, time_id, date):
    try:
        user_id = request.session.get('user_id') * 1
    except Exception:
        return redirect(reverse('account:user_login'))

    user_id = request.session.get('user_id')
    userprof = UserProf.objects.get(user_id=user_id)
    reservation = Reservation()

    time_choices = ["8:00-11:00", "13:00-17:00", "18:00-21:00"]
    if time_id == time_choices[0]:
        reservation.time_id = 1
    if time_id == time_choices[1]:
        reservation.time_id = 2
    if time_id == time_choices[2]:
        reservation.time_id = 3

    # 预约规则函数，若不符合规则，则无法预约
    msg = book_rule(userprof, reservation.time_id, date)
    if msg != "OK":
        return HttpResponse(msg)

    reservation.seat_id = table_id

    reservation.account = userprof

    reservation.date = date

    reservation.is_delete = False

    reservation.save()
    return redirect(reverse('book:book_record'))


# 预约记录展示
def book_record(request):
    try:
        user_id = request.session.get('user_id') * 1
    except Exception:
        return redirect(reverse('account:user_login'))

    user_id = request.session.get('user_id')
    userprof = UserProf.objects.get(user_id=user_id)

    # 判断该用户的所有预约记录是否过期，若过期则将预约记录的is_delete属性置为True
    judge_is_delete(userprof)

    reservation_records = Reservation.objects.filter(account=userprof)
    reservation_records = reservation_records.order_by('-date', '-time_id')

    # 两个列表，一个存储可取消预约的记录，一个存储不可取消（过期）的记录
    records_not_delete = []
    records_is_delete = []

    for reservation_record in reservation_records:

        # re_record用于存储记录的日期、时间段、预约座位的位置、安静区/非安静区、预约记录id
        re_record = Re_Record()

        re_record.day = reservation_record.date
        re_record.id = reservation_record.id

        if reservation_record.time_id == 1:
            re_record.time_choice = '8:00-11:00'
        if reservation_record.time_id == 2:
            re_record.time_choice = '13:00-17:00'
        if reservation_record.time_id == 3:
            re_record.time_choice = '18:00-21:00'

        # 与该预约记录关联的seat
        seat = reservation_record.seat
        if seat.is_quiet_area:
            re_record.is_quiet = '安静区'
            re_record.seat_id = seat.table_position_quiet
        else:
            re_record.is_quiet = '非安静区'
            re_record.seat_id = seat.table_position_noisy

        if not reservation_record.is_delete:
            records_not_delete.append(re_record)
        else:
            records_is_delete.append(re_record)

    data = {
        'records_not_delete': records_not_delete,
        'records_is_delete': records_is_delete,
    }
    return render(request, 'main/book_record.html', context=data)


def book_cancel(request, reservation_id):
    try:
        user_id = request.session.get('user_id') * 1
    except Exception:
        return redirect(reverse('account:user_login'))

    Reservation.objects.filter(id=reservation_id).delete()

    # 个人信誉评价，若取消预约2次，则信誉度减1
    user_id = request.session.get('user_id')
    userprof = UserProf.objects.get(user_id=user_id)
    userprof.delete_times += 1
    if userprof.delete_times % 2 == 0:
        if userprof.credit >= 1:
            userprof.credit -= 1
    userprof.save()

    return redirect(reverse('book:book_record'))
