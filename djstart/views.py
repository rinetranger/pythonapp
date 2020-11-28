from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    params ={
        'title': "djstart/index",
        'msg':'お名前は？',
        # 'goto':'next',
    }
    return render(request,'djstart/index.html',params)

# def next(request):
#     params = {
#         'title': "djstart/next",
#         'msg':'これはanotherページです。',
#         'goto':'index',
#     }
#     return render(request,'djstart/index.html',params)

def form(request):
    msg=request.POST['msg']
    params = {
        'title': "djstart/next",
        'msg':'こんにtには' + msg +'さん',
        'goto':'index',
    }
    return render(request,'djstart/index.html',params)

# Create your views here.
