import xadmin
from apps.organizations.models import CourseOrg
from apps.organizations.models import City
from apps.organizations.models import Teacher
#不用继承admin.ModelAdmin
class CourseOrgAdmin(object):
    list_display=["id","name","address","is_gold"]
class TeacherAdmin(object):
    list_display = ["id", "name", "company", "job"]
class CityAdmin(object):
    list_display = [ "name", "describe"]
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Teacher,TeacherAdmin)