from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'web/index.html')
	

def contact(request):
	return render(request,'web/contact.html')
	
def about(request):
	return render(request,'web/about.html')
	


# Create your views here.
