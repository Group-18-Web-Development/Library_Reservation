from django.db import models


# 用户模型初步创建
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    icon = models.ImageField(upload_to='icon', default='static/image/default_icon.jpg')  # 头像(有默认头像)
    credit = models.PositiveIntegerField(default=5)  # 信誉度

    class Meta:
        db_table = 'user'
