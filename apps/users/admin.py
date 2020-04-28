from django.contrib import admin
from apps.users.models import UserProfile
from django.contrib.auth.admin import  UserAdmin
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile,UserAdmin)

#因为用户表相对来说都是系统中存在的 django内置了一个UserAdmin对显示用户信息做了优化

