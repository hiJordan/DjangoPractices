from django.shortcuts import render
from django.views.generic import View
import random
import string
from .models import Upload
from django.http import HttpResponsePermanentRedirect, HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'base.html', {})

    def post(self, request):
        if request.FILES:
            file = request.FILES.get('file')
            name = file.name
            size = int(file.size)

            with open(r'static\file\\'+name, 'wb') as f:
                f.write(file.read())
            code = ''.join(random.sample(string.digits, 8))
            u = Upload(name=name, fileSize=size, code=code,
                       path=r'static\file\\'+name, PCIP=str(request.META['REMOTE_ADDR']),)
            u.save()
            return HttpResponsePermanentRedirect('/s/'+code)


class MyView(View):
    def get(self, request):
        IP = request.META['REMOTE_ADDR']
        u = Upload.objects.filter(PCIP=str(IP))
        for i in u:
            i.downloadDocount += 1
            i.save()
        return render(request, 'content.html', {'content': u})


class DisplayView(View):
    def get(self, request, code):
        u = Upload.objects.filter(code=str(code))
        if u:
            for i in u:
                i.downloadDocount += 1
                i.save()
        return render(request, 'content.html', {'content': u})


class SearchView(View):
    def get(self, request):
        code = request.GET.get('kw')
        u = Upload.objects.filter(name=str(code))
        if u:
            for i in u:
                i.downloadDocount += 1
                i.save()
        return render(request, 'content.html', {'content': u})

