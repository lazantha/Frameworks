from django.db import models

# Create your models here.

class PostTable(models.Model):
	post_id=models.AutoField(primary_key=True)
	topic=models.CharField(max_length=50)
	content=models.CharField(max_length=50)
	def __str__(self):
		return self.topic


