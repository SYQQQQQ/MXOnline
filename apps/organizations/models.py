from django.db import models
from apps.users.models import BaseModel
from apps.users.models import UserProfile
# Create your models here.
class City(BaseModel):
    name = models.CharField(default="",max_length=5,verbose_name="城市名")
    describe = models.CharField(default="这是个美丽的地方",max_length=100,verbose_name="描述")
    class Meta:
        verbose_name="城市信息"
        verbose_name_plural = verbose_name
        def __str__(self):
            return self.name
class CourseOrg(BaseModel):
    name = models.CharField(default="",max_length=50,verbose_name="机构名称")
    notice =models.CharField(default="",max_length=50,verbose_name="机构标签")
    category = models.CharField(default="",max_length=10,verbose_name="机构类别",choices=(("gr", "个人"), ("gx", "高校"),("pxjg","培训机构")))
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(verbose_name="机构地址",default="",max_length=300)
    students = models.IntegerField(default=0,verbose_name="学习人数")
    class_num = models.IntegerField(default=0,verbose_name="课程数")
    is_identification = models.BooleanField(default=False,verbose_name="是否认证")
    is_gold = models.BooleanField(default=False,verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")
    class Meta:
        verbose_name="课程机构"
        verbose_name_plural = verbose_name
        def __str__(self):
            return self.name
class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    affiliations = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name="所属机构")
    name = models.CharField(default="", max_length=5, verbose_name="教师名")
    work_num = models.IntegerField(default=0, verbose_name="工作年限")
    company = models.CharField(default="", max_length=15, verbose_name="就职公司")
    job = models.CharField(default="", max_length=15, verbose_name="公司职位")
    characteristic = models.CharField(default="", max_length=300, verbose_name="教学特点")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    old = models.IntegerField(default=0,verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)
    class Meta:
        verbose_name="教师信息"
        verbose_name_plural = verbose_name
        def __str__(self):
            return self.name
