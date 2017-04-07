#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app1.models import Employee
from django.core.paginator import Paginator , EmptyPage,PageNotAnInteger

def new(request):
    list = request.GET.get('list')
    title_new = Employee.objects.filter(id = list)
    return render(request,'new.html',{'title_new':title_new})

def title(request):
    title_list = Employee.objects.all()
    paginator = Paginator(title_list,10)
    page = request.GET.get('page')
    try:
        title = paginator.page(page)
    except PageNotAnInteger:
        title = paginator.page(1)
    except EmptyPage:
        title = paginator.page(paginator.num_pages)
        
    return render(request,'title.html',{'title':title})

def index(request):
    return render(request,'web.html')
