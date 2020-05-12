from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg,City
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.form import AddAskForm
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        all_orgs = CourseOrg.objects.all()

        all_city = City.objects.all()
        category = request.GET.get("ct","")
        hot_orgs = all_orgs.order_by("-click_num")[:3]
        if category:
           all_orgs =  all_orgs.filter(category = category)
        city_id = request.GET.get('city',"")
        city_name = ''
        if city_id:
            city = City.objects.get(id=int(city_id))
            city_name = city.name
            if city_id.isdigit():
                 all_orgs = all_orgs.filter(city__id=city_id)
        sort = request.GET.get("sort","")
        if sort:
            all_orgs = all_orgs.order_by(sort)
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs,per_page=10,request=request)
        orgs = p.page(page)
        return render(request,'org-list.html',
            {"all_orgs":orgs,"org_nums":org_nums,"all_citys":all_city,"category":category,"city_id":city_id,"city_name":city_name,"sort":sort,"hot_orgs":hot_orgs})


class AddAsk(View):
    """处理用户咨询模块"""
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status":"success",
                "msg":"提交成功"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })
