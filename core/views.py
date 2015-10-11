from django.shortcuts import render
#from django.http import HttpResponse # for testview
from django.views.generic import TemplateView
# Create your views here.



class SplashView(TemplateView): #inherits from TemplateView
    template_name = "index.html" #settings.py -> TEMPLATES -> DIRS -> look for index.html "template file"