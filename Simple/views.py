from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def members(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

def signin(request):
   template = loader.get_template('signin.html')
   context = {}
   return HttpResponse(template.render(context, request))

def signup(request):
   template = loader.get_template('signup.html')
   context = {}
   return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

########################################## Testing ################################################
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))