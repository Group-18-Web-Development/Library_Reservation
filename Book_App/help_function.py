from Book_App.models import Reservation
import datetime


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


# 判断该用户的所有预约记录是否过期，若过期则将预约记录的is_delete属性置为True
def judge_is_delete(userprof):
    reservation_records = Reservation.objects.filter(account=userprof).filter(is_delete=False)
    today = str(datetime.date.today())

    # 删除当日之前的记录
    for reservation_record in reservation_records:
        if reservation_record.date < today:
            reservation_record.is_delete = True
            reservation_record.save()

    # 处理当日的记录，若当日时间已过，亦需删除
    reservation_records = reservation_records.filter(is_delete=False).filter(date=today)
    time_now = datetime.datetime.now().hour
    if time_now >= 18:
        for reservation_record in reservation_records:
            reservation_record.is_delete = True
            reservation_record.save()
    elif time_now >= 13:
        for reservation_record in reservation_records:
            if reservation_record.time_id <= 2:
                reservation_record.is_delete = True
                reservation_record.save()
    elif time_now >= 8:
        for reservation_record in reservation_records:
            if reservation_record.time_id == 1:
                reservation_record.is_delete = True
                reservation_record.save()


class Re_Record:
    def __init__(self):
        self.day = ''
        self.time_choice = ''
        self.is_quiet = ''
        self.seat_id = ''
        self.id = 0


# 预约规则函数
def book_rule(userprof, time_id, date):
    # case1 信誉分为0，则无法继续预约
    if userprof.credit == 0:
        return "您的信誉分过低，无法预约，可联系管理员提高信誉分！"

    # case2 同一时间段不能重复预约
    reservation_record = Reservation.objects.filter(account=userprof).filter(time_id=time_id).filter(date=date)
    if reservation_record.exists():
        return "在该时间段已有预约，您不能重复预约！"

    # case3 当前预约次数最多为3次
    # 判断该用户的所有预约记录是否过期，若过期则将预约记录的is_delete属性置为True
    judge_is_delete(userprof)
    reservation_records = Reservation.objects.filter(account=userprof).filter(is_delete=False)
    if reservation_records.count() >= 3:
        return "您的当前预约次数已达上限，无法继续预约！"

    return "OK"

