from django.shortcuts import render
from django.views.generic import View
from .models import Upload
from django.http import HttpResponsePermanentRedirect
import random
import string
#import  datetime

# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,"base.html",{})

    def post(self, request):
        if request.FILES:
            file = request.FILES.get("file")
            name = file.name
            size = int(file.size)
            with open('static/file/' + name, 'wb')as f:
                f.write(file.read())
            code = ''.join(random.sample(string.digits, 8))
            u = Upload(
                path='static/file/' + name,
                name=name,
                Filesize=size,
                code=code,
                PCIP=str(request.META['REMOTE_ADDR']),
            )
            u.save()
            return HttpResponsePermanentRedirect("/s/" + code)


class DisplayView(View): #展示文件视图类
    def get(self,request,code):
        u=Upload.objects.filter(code=str(code))

        if u:#如果有内容，u的访问次数+1,否则返回给前端的内容也是空的
            for i in u:
                i.DownloadDoccount+=1 #每次访问，访问次数加1
                i.save()
        return render(request,'content.html',{"content":u})
