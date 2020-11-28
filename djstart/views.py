from django.shortcuts import render

from django.http import HttpResponse
from . forms import DjstartForm

def index(request):
    params ={
        'title': "djstart/index",
        'message':'your data:',
        'form':DjstartForm()
        # 'goto':'next',
    }
    if(request.method =='POST'):
        params['message']='名前:'+request.POST['name']+'<br>メール:' +request.POST['mail']+'<br>age:' +request.POST['age']
        params['form']=DjstartForm(request.POST)
    return render(request,'djstart/index.html',params)

# def next(request):
#     params = {
#         'title': "djstart/next",
#         'msg':'これはanotherページです。',
#         'goto':'index',
#     }
#     return render(request,'djstart/index.html',params)

# def form(request):
#     msg=request.POST['msg']
#     params = {
#         'title': "djstart/next",
#         'msg':'こんにちは' + msg +'さん',
#         'goto':'index',
#     }
#     return render(request,'djstart/index.html',params)

# Create your views here.
