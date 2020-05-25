from django.db import models

from Account_App.models import UserProf


# 座位模型创建
class Seat(models.Model):
    is_quiet_area = models.BooleanField(default=True)  # 安静区/非安静区

    # 座位分为安静区与非安静区
    # 安静区：floor、area、table_type、has_power、table_position_quiet
    # 非安静区：floor、table_type、table_position_noisy

    floor = models.IntegerField(default=1)  # 楼层，5层
    area = models.CharField(max_length=1, null=True)  # 阅览区，A区、B区、C区
    table_type = models.IntegerField(default=4)  # 桌子类型，1人桌、2人桌、4人桌
    has_power = models.BooleanField(default=False)  # 默认无电源插座

    table_position_noisy = models.CharField(max_length=20, null=True)  # 桌子位置 格式：floor-桌号
    table_position_quiet = models.CharField(max_length=20, null=True)  # 桌子位置 格式：A100-桌号

    class Meta:
        db_table = 'seat'


# 预约模型创建
class Reservation(models.Model):
    account = models.ForeignKey(UserProf, on_delete=models.CASCADE)  # 与用户关联
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)  # 与座位关联
    is_delete = models.BooleanField(default=True)  # 当前预约/预约记录
    date = models.CharField(max_length=20)  # 预约时间点(年-月-日）
    time_choice = (  # 可选择时间点
        (1, "8:00-11:00"),
        (2, "13:00-17:00"),
        (3, "18:00-21:00"),
    )
    time_id = models.IntegerField(choices=time_choice)  # 1、2、3

    class Meta:
        db_table = 'reservation'
        unique_together = (
            ("account", "seat", "time_id", "date"),  # 这三个字段联合唯一，防止重复预订
        )
