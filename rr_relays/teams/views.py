from django.http import HttpResponse
from django.shortcuts import render
from .models import Runner


def index(request):
    return HttpResponse("Hello, world. You're at the runneymede runners index.")

# Create your views here.
