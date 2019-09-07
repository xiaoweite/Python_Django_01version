from django.shortcuts import render
from django.http import *
# from django.template import RequestContext,loader
def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return  HttpResponse(temp.render())
    context = {'title':'43423'}
    return render(request,'booktest/index.html',context)


