from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('This is the Acumen home page')

def ian(request):
	return HttpResponse("This is ian's page. <a href='/'>return to the home page</a>")
