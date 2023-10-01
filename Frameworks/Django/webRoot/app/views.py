from django.shortcuts import render,redirect
from .forms import *

def home(request):
	
	return render(request,'home.html')

def createStudent(request):
	form=StudentForm()
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('page_home')
	context={'form':form}
	
	return render(request,'register.html',context)


def subjectReg(request):

	form=SubjectForm()
	if request.method=='POST':
		form=SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('page_home')
	context={'form':form}
	return render(request,'sub_reg.html',context)



def adminRegister(request):
	form=AdminForm()
	if request.method=='POST':
		form=AdminForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('page_home')
	context={'form':form}
	return render(request,'admin_register.html',context)
#database querying methods

#queryset=Customer.objects.all()
#queryset=Customer.objects.get()
#queryset=Customer.objects.filter()
#queryset=Customer.objects.exclude()

