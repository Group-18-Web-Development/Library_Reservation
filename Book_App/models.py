from django.db import models

from Account_App.models import User


# 座位模型初步创建
class Seat(models.Model):
    area = models.CharField(max_length=1)  # 阅览区，A区、B区、C区……
    position = models.CharField(max_length=10, unique=True)  # 具体位置 格式 A-001-001
    # characteristic 待扩展
    has_power = models.BooleanField(default=False)  # 默认无电源插座

    class Meta:
        db_table = 'seat'


# 预约模型初步创建
class Reservation(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)  # 与用户关联
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)  # 与座位关联
    book_time = models.CharField(max_length=10)  # 座位预约的时间点
    is_delete = models.BooleanField(default=True)  # 当前预约/预约记录

    class Meta:
        db_table = 'reservation'
