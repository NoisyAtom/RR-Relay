from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Runner


def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())
	
def timer(request):
	
	context={"name":"christine"}
	template = loader.get_template('timer.html')
	return HttpResponse(template.render(context))
# Create your views here.
