from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male","男"),
    ("female","女")
)
# Create your models here.
class BaseModel(models.Model):
    add_time =  models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        abstract = True #将该基类定义为抽象类 即不生成对应的数据库表
        #之最为一个可以集成度基类

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="");
    birthday  = models.DateField(verbose_name="生日",null=True,blank=True);
    gender = models.CharField(max_length=6,verbose_name="性别",choices=GENDER_CHOICES)
    address = models.CharField(max_length=100,verbose_name="地址",default="")
    mobile = models.CharField(max_length=11,verbose_name="手机号码")
    image = models.ImageField(verbose_name="用户头像",upload_to="head_image/%Y/%m",default="default.jpg")
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
        # def unread_nums(self):
        #     return self.usermessage_set.filter(has_read=False).count()
        # def __str__(self):
        #     if self.nick_name:
        #         return self.nick_name
        #     else:
        #         return self.username

