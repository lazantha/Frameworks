from django import forms
from .models import StudentTable


class StudentReg(forms.ModelForm):
	class Meta:
		model=StudentTable
		fields='__all__'




