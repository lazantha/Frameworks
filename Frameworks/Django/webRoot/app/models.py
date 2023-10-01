from django.db import models

class StudentTable(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)

	
class SubjectTable(models.Model):
	student=models.ForeignKey(StudentTable,null=True,on_delete=models.SET_NULL)
	subject_name=models.CharField(max_length=50,null=False)

class AdminTable(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=100)
	

