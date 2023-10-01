from django.db import models

class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=20)
	def __str__(self):
		return self.first_name+' '+self.last_name


class Member(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=20)
	password=models.CharField(max_length=20,null=False)
	
	def __str__(self):
		return self.first_name

