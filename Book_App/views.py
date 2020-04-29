import datetime

from django.shortcuts import render
from django.http import HttpResponse
import time

from Book_App.models import Seat, Reservation


def book_seat(request):
    # 座位预约

    # 获取时间（假设能预约7天内的座位）
    days = []
    today = datetime.date.today()
    days.append(today)
    for i in range(6):
        days.append(today + datetime.timedelta(days=i + 1))

    # 可选择时间点
    time_choices = ["8:00-11:00", "13:00-17:00", "18:00-21:00"]

    if request.method == 'GET':
        context = {
            'days': days,
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

        # 安静区/非安静区处理
        # if zone != 'quiet' and zone != 'noisy':
        #     seats = Seat.objects.all()
        #
        #     # 对seats_q进行最后的筛选，若这些座位的id在result中出现，则说明该位置已被预约，应剔除
        #     for i in range(length):
        #         seats = seats.exclude(id=result[i])
        #
        #     data = {
        #         'days': days,
        #         'time_choices': time_choices,
        #         'seats_q': seats,
        #         'day': day,
        #         'time_choice': time_choice,
        #     }
        #     return render(request, 'main/book_seat.html', context=data)

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

            data = {
                'days': days,
                'time_choices': time_choices,
                'seats_q': seats_q,
                'day': day,
                'time_choice': time_choice,
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

            data = {
                'days': days,
                'time_choices': time_choices,
                'seats_n': seats_n,
                'day': day,
                'time_choice': time_choice,
            }
            return render(request, 'main/book_seat.html', context=data)


# 将用户选择预约的table id与用户绑定，存至reservation数据库
def book_success(request, table_id):
    print(table_id)
    return HttpResponse('预约成功')


def book_record(request):
    # 预约记录
    return render(request, 'main/book_record.html')


def book_cancel(request):
    # 取消预约
    return render(request, 'main/book_cancel.html')


# 日期格式化函数 2020年5月1日 → 2020-05-01
def date_transform(day_f):
    year = day_f[0:4]
    if day_f[6] == '月':
        month = '0' + day_f[5]
    else:
        month = day_f[5]
    if day_f[-3] == '月':
        day = '0' + day_f[-2]
    else:
        day = day_f[-3:-1]
    return year + '-' + month + '-' + day


# 查询在该时间段所有已被预约的座位，把这些id存至result
def reservation_search_id(day, time_choice):
    reservation_record = Reservation.objects.filter(date=day)
    if time_choice == "8:00-11:00":
        reservation_record = reservation_record.filter(time_id=1)
    elif time_choice == "13:00-17:00":
        reservation_record = reservation_record.filter(time_id=2)
    elif time_choice == "18:00-21:00":
        reservation_record = reservation_record.filter(time_id=3)
    result = []
    for item in reservation_record:
        result.append(item.seat_id)
    return result
