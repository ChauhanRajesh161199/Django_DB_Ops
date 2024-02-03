from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def members(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

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