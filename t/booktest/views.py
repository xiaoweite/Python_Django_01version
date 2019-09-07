#encoding=utf-8
from django.shortcuts import render
from django.http import *
from .models import *
# from django.template import RequestContext,loader
def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return  HttpResponse(temp.render())
    # context = {'title':'43423'}
    bookList=BookInfo.objects.all()
    context = {'list':bookList}
    return render(request,'booktest/index.html',context)


