from django.shortcuts import render
from django.http import HttpResponse
from . models import Friend
from .forms import DjstartForm

def index(request):
    params ={
        'title':'djstat',
        'message':'all friends.',
        'form':DjstartForm(),
        'data':[],
    }
    if(request.method =="POST"):
        num =request.POST['id']
        item = Friend.objects.get(id = num)
        params['data'] = [item]
        params['form'] = DjstartForm(request.POST)
    else:
        params['data']=Friend.objects.all()

    return render(request,'djstart/index.html',params) 

    


# Create your views here.
