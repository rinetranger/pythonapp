from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . forms import DjstartForm

class DjstartView(TemplateView):

    def __init__(self):
        self.params = {
            'title': "djstart/index",
            'form':DjstartForm(),
            'result':None,
        }

    def get(self,request):
        return render(request,'djstart/index.html',self.params)

    def post(self,request):
        chk = request.POST['check']
        self.params['result'] = 'You selected:"' + chk + '".'
        self.params['form'] = DjstartForm(request.POST)
        return render(request,'djstart/index.html',self.params)



# Create your views here.
