from django.db import models

# Create your models here.
class ApiModel(models.Model):
	fname = models.CharField(max_length=50, null=True, blank=True)
	 

	def __str__(self):
		return self.fname