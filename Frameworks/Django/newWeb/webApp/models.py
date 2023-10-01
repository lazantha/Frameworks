from django.db import models

class StudentTable(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=50)

class AdminTable(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	password=models.CharField(max_length=50)
	

# Create your models here.
