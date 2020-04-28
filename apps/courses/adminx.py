import xadmin
from apps.courses.models import Course
#不用继承admin.ModelAdmin
class CourseAdmin(object):
    list_display=["id","name","learn_times","desc"]
    search_file=["name","desc"]
xadmin.site.register(Course,CourseAdmin)