from django.shortcuts import render
from .models import StudentTable

def home(request):
	student_data=StudentTable.objects.all()
	return render(request,'home.html',{'student_data':student_data})

# Create your views here.
