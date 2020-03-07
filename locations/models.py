from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
	"""A location for excercise"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str(self):
		return self.text