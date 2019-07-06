from django.db import models  #总
from django.contrib.auth.models import User #Django默认的用户数据模型，即auth_user

# Create your models here.


class UserProfile(models.Model):
    db_table = 'account_userprofile'
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True) #OneToOneField()的含义是通过user这个字段声明UserProfile类与User类之间的关系是“一对一”的。
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)