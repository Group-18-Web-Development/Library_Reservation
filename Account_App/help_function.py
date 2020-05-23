import random

from django.contrib.auth.models import User

from Book_App.models import Reservation, Seat


def add_data_help():
    # 添加用户数据
    for i in range(10):
        user = User()
        user.username = 'Jason' + str(i)
        user.password = '00000' + str(i)
        user.email = '123456@gmail.com'
        user.save()

    # 添加安静区座位
    for j in range(5):
        for i in range(20):
            seat = Seat()
            seat.is_quiet_area = True
            seat.floor = j + 1
            seat.area = 'A'
            seat.table_type = random.choice([1, 2, 4])
            seat.has_power = random.choice([True, False, False, False])
            seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
            seat.save()

    for j in range(5):
        for i in range(20):
            seat = Seat()
            seat.is_quiet_area = True
            seat.floor = j + 1
            seat.area = 'B'
            seat.table_type = random.choice([1, 2, 4])
            seat.has_power = random.choice([True, False, False, False])
            seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
            seat.save()

    for j in range(5):
        for i in range(20):
            seat = Seat()
            seat.is_quiet_area = True
            seat.floor = j + 1
            seat.area = 'C'
            seat.table_type = random.choice([1, 2, 4])
            seat.has_power = random.choice([True, False, False, False])
            seat.table_position_quiet = seat.area + str(seat.floor * 100) + '-' + str(i+1)
            seat.save()

    # 添加非安静区座位
    for s in range(5):
        for i in range(30):
            seat = Seat()
            seat.is_quiet_area = False
            seat.floor = s+1
            seat.table_type = random.choice([1, 2, 4])
            seat.table_position_noisy = 'F' + str(seat.floor) + '-' + str(i + 1)
            seat.save()

    # 添加预约记录
    for i in range(9):
        record = Reservation()
        record.account_id = i + 1
        record.seat_id = random.randrange(50) + 1
        record.time_id = random.choice([1, 2, 3])
        record.save()