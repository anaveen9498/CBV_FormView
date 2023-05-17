from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from Naveen.forms import *
from django.http import HttpResponse
# Create your views here.



class CBV_Form(FormView):
    template_name='CBV_Form.html'
    form_class=SchoolForm


    def form_valid(self, form):
        form.save()
        return HttpResponse("Data is Inserted Successfully...!!!")