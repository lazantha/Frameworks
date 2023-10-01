from django.forms import ModelForm
from .models import StudentTable,SubjectTable,AdminTable

class StudentForm(ModelForm):
	class Meta:
		model=StudentTable
		fields='__all__' 
		#include all field 

class SubjectForm(ModelForm):
	class Meta:
		model=SubjectTable
		fields='__all__'


class AdminForm(ModelForm):
	class Meta:
		model=AdminTable
		fields='__all__'






		