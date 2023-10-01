from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import StudentTable,Author,Book
from django.db.models import Q
def home(request):
	form=StudentForm()
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('homePage')
	context={'form':form}

	return render(request,'home.html',context)


def read(request):
	#data=StudentTable.objects.all()
	data=StudentTable.objects.all()
	data=StudentTable.objects.values('first_name','email','last_name','age').filter(Q(age__gte=18)).order_by('age')
	
	books=Book.objects.all()
	
	context={'data':data,'book_data':books}
	return render(request,'read.html',context)



def dynamicUrl(request,data):

	

	context={'data':data}
	print(context['data'])
	return render(request,'dynamic.html',context)
