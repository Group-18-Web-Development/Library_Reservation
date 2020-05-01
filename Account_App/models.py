from django.db import models
from django.contrib.auth.models import User

# 用户模型初步创建
class UserProf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icon', default='static/image/default_icon.jpg')  # 头像(有默认头像)
    credit = models.PositiveIntegerField(default=5)  # 信誉度
    phone = models.CharField(max_length=20,null=True) #电话

    class Meta:

        db_table = 'userprof'

    def __str__(self):
        return 'user {}'.format(self.user.username)



