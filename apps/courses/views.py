from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class CourseOrgView(View):
    def get(self,request,*args,**kwargs):
        all_course = Course.objects.all()
        hot_course = Course.objects.filter(is_banner=True)
        sort = request.GET.get("sort","")
        if sort:
            if sort=='hot':
                all_course = all_course.order_by('-fav_nums')
            else:
                all_course = all_course.order_by('-students')
        else:
            sort=''
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course,per_page=5,request=request)
        org_course = p.page(page)
        return render(request,'course-list.html',
                      {"all_course":org_course,"hot_course":hot_course,"sort":sort})


