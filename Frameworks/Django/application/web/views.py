from django.shortcuts import render
from django.http import HttpResponse



def home(request):

	return HttpResponse(request,'Home')


def contact(request):

	return HttpResponse(request,'Contact')
# Create your views here.

