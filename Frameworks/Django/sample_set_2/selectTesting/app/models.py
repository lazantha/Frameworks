from django.db import models



class PostTable(models.Model):
	topic=models.CharField(max_length=50)
	content=models.CharField(max_length =50)


