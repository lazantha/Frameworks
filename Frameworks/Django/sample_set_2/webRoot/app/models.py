from django.db import models

class StudentTable(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	age=models.IntegerField(null=True)

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
	