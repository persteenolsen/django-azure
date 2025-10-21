from django.http import HttpResponse
from datetime import datetime

from django.template import loader

def index(request):
  template = loader.get_template('example/index.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('example/about.html')
  return HttpResponse(template.render())

def me(request):
  template = loader.get_template('example/me.html')
  return HttpResponse(template.render())