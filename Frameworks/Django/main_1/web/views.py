from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1>Home</h1>")

def contact(request):
	return HttpResponse("<h1>Contact</h1>")

def about(request):
	return HttpResponse("<h1>About</h1>")

def mainForm(request):
	return HttpResponse("<h1>Main Form</h1>")

# Create your views here.
