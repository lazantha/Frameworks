from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1>Welcome Home</h1>")

def contact(request):
	return HttpResponse("<h1>Contact Page</h1>")

def about(request):
	return HttpResponse("<h1>About Page</h1>")

# Create your views here.
