from django.db import models
from django.contrib.auth.models import User

# 用户模型初步创建
class UserProf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icon', default='static/image/default_icon.jpg')  # 头像(有默认头像)
    credit = models.PositiveIntegerField(default=5)  # 信誉度

    class Meta:

        db_table = 'userprof'





