from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app1.forms import *
from django.http import HttpResponse
from typing import Any,Dict
# Create your views here.

class tempdatarender(TemplateView):
    template_name='tempdatarender.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ecdo=super().get_context_data(**kwargs)
        ecdo['name']='bhavani'
        return ecdo

class insertdata(TemplateView):
    template_name='insert.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ecdo=super().get_context_data(**kwargs)
        sfo=StudentForm()
        ecdo['sfo']=sfo
        return ecdo
    
    def post(self,request):
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            sfd.save()
            return HttpResponse('data is inserted')

class StudentFormviewinsert(FormView):
    template_name='StudentFormviewinsert.html'
    form_class=StudentForm

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return HttpResponse('data is inserted')
        #return super().form_valid(form)  
    
