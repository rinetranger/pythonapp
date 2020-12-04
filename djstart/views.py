from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . models import Friend
from .forms import FriendForm
from .forms import FindForm


def index(request):
    data=Friend.objects.all()
    params ={
        'title':'djstat',
        'data':data,
    }
    return render(request,'djstart/index.html',params) 

#create Model

def create(request):
    if(request.method == "POST"):
        obj=Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to ='/djstart')
    params = {
        'title':'Test',
        'form':FriendForm(),
    }
    return render(request,'djstart/create.html',params)

def edit(request,num):
    obj = Friend.objects.get(id=num)
    if(request.method=='POST'):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/djstart')
    params = {
        'title':'Test',
        'id':num,
        'form':FriendForm(instance=obj),
    }
    return render(request,'djstart/edit.html',params)

def delete(request,num):
    friend = Friend.objects.get(id=num)
    if(request.method == "POST"):
        friend.delete()
        return redirect(to='/djstart')
    params = {
        'title':'Test',
        'id':num,
        'obj':friend,
    }
    return render(request,'djstart/delete.html',params)

def find(request):
    if(request.method == 'POST'):
        msg = 'search reult:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(name__contains=str)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
            'title':'Test',
            'message':msg,
            'form':form,
            'data':data,
    }
    return render(request,'djstart/find.html',params)



# Create your views here.
