from django.shortcuts import render,redirect
from .models import StudentTable
from .forms import StudentReg
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
	data=StudentTable.objects.all()
	context={'data':data}
	return render(request,'home.html',context)

def form(request):
	form=StudentReg()

	if request.method=='POST':
		form=StudentReg(request.POST)
		if form.is_valid():
			form.save()
			first_name=form.cleaned_data.get('first_name')
			messages.success(request,'Success'+first_name)
			return redirect('home_page')
	context={'form':form}


	return render(request,'form.html', context)


def userReg(request):
	form=UserCreationForm()
	if request.method=='POST}':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render('home_page')
	context={'form':form}
	return render(request,'userReg.html',context)


