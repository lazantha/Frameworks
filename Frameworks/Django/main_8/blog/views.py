from django.shortcuts import render
from django.http import Httpresponse



def home():
	return Httpresponse("<h1>Home</h1>")
	

# Create your views here.
