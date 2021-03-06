from django.db import models
from django.contrib.auth.models import User


class UserProf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icon', default='icon/default_icon.jpg')  # 头像(有默认头像)
    credit = models.PositiveIntegerField(default=5)  # 信誉度
    delete_times = models.PositiveIntegerField(default=0)
    introduction = models.TextField(default="个人简介")  # 个人简介
    name = models.CharField(default="user", max_length=20)  # 姓名
    student_number = models.CharField(max_length=12)  # 学号
    phone_number = models.CharField(max_length=11)  # 电话号码
    record_id = models.TextField(editable=False)  # 预约记录

    class Meta:
        db_table = 'userprof'

    def __str__(self):
        return 'user {}'.format(self.user.username)



