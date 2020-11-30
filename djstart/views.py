from django.shortcuts import render
from django.http import HttpResponse
from . models import Friend

def index(request):
    data = Friend.objects.all()
    params ={
        'title':'djstatr',
        'message':'all friends.',
        'data':data,
    }

    return render(request,'djstart/index.html',params) 

    


# Create your views here.
