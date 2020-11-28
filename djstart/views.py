from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . forms import DjstartForm

class DjstartView(TemplateView):

    def __init__(self):
        self.params = {
            'title': "djstart/index",
            'message':'your data:',
            'form':DjstartForm()
        }

    def get(self,request):
        return render(request,'djstart/index.html',self.params)

    def post(self,request):
        msg = 'あなたは、<b>'+ request.POST['name'] + '('+request.POST['age'] + ')さんです。<br>メールアドレスは、<b>' + request.POST['mail'] + '</b>ですね。'
        self.params['message']= msg
        self.params['form'] = DjstartForm(request.POST)
        return render(request,'djstart/index.html',self.params)



# Create your views here.
