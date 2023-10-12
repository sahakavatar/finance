from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
  context = {
    'user': request.user,
  }
  print(request.user.is_authenticated)
  template = loader.get_template('view/dashboard/index.html')
  return HttpResponse(template.render(context,request))
