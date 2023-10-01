from django.shortcuts import render
from .models import Member
from .forms import MemberForm

def home(request):
	all_members=Member.objects.all
	return render(request,'home.html',{'all':all_members})


def content(request):
	return render(request,'content.html')

def about(request):
	return render(request,'about.html')


def join(request):

	if request.method=='POST':
		form=MemberForm(request.POST or None)
		if form.is_valid():
			form.save()
			return render(request,'join.html') 		
	return render(request,'join.html')
	




# Create your views here.
