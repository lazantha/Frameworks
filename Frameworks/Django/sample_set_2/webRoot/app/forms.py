from django.forms import ModelForm
from django import forms
from .models import StudentTable



class StudentForm(ModelForm):
	class Meta:
		model=StudentTable
		fields='__all__'
		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'custom-class', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'custom-class', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'custom-class', 'placeholder': 'Email'}),
         	'age': forms.TextInput(attrs={'class': 'custom-class', 'placeholder': 'Age'}),
               
        }
