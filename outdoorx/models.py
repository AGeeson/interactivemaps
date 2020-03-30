from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from colorfield.fields import ColorField



class Topic(models.Model):
	"""A topic the user is learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def  __str__(self):
		"""Return a string representation of the model."""
		return self.text

class  Entry(models.Model):
	"""SOmething specific learned about a topic"""
	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __self__(self):
		"""Return a string representation of the model."""
		return self.text[:50] + "..."

class Location(models.Model):
	"""A location for excercise"""
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200, default='A short description about the atmosphere and surroundings of the location.')
	latitude = models.DecimalField(max_digits=55, decimal_places=50, null=True, blank=True)
	longitude = models.DecimalField(max_digits=55, decimal_places=50, null=True, blank=True)
	latlng = models.CharField(max_length=50, default='00.0000, 00.0000')
	date_added = models.DateTimeField(auto_now_add=True)
	equipment = models.CharField(max_length=200, default='Unfinished- needs different model')
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	# docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	image = models.ImageField(upload_to = 'pic_folder', default = 'pic_folder/None/no-img.jpg')
	
	CALISTHENICS = 'Calisthenics'
	FREEWEIGHTS = 'Free Weights'
	MECHANISMS = 'Mechanisms'
	TRACKANDFIELD = 'Track & Field'
	SPORTS = 'Popular for Sports'
	EXTREMESPORTS = 'Extreme Sports'
	SELFDEFENCE= 'Self Defence'
	LARPING = 'Larping'
	
	PRACTICALITY_CHOICES = [
	(CALISTHENICS,'Calisthenics'),
	(FREEWEIGHTS, 'Freeweights'),
	(MECHANISMS, 'Mechanisms'),
	(TRACKANDFIELD, 'Track & Field'),
	(SPORTS, 'Popular for Sports'),
	(EXTREMESPORTS, 'Extreme Sports'), 
	(SELFDEFENCE, 'Self Defence'),
	(LARPING, 'Larping (Live Action Role Playing'),
	]
	type_of_excercise = models.CharField(
		max_length=30,
		choices=PRACTICALITY_CHOICES,
		default=CALISTHENICS
		)

	COASTAL = 'Coastal'
	RAISED = 'Raised'
	FOREST = 'Forest'
	PARK = 'Park'
	URBAN = 'Urban'
	INANDOUT = 'Indoor and Outdoor'
	SHADED = 'Shaded'

	TYPE_OF_LOCATION_CHOICES = [
	(COASTAL,'Coastal'),
	(RAISED, 'Raised'),
	(FOREST, 'Forest'),
	(PARK, 'Park'),
	(URBAN, 'Urban'),
	(INANDOUT, 'Indoor and Oudoor'),
	(SHADED, 'Shaded'),
	]
	type_of_location = models.CharField(
		max_length=30,
		choices=TYPE_OF_LOCATION_CHOICES,
		default=PARK
		)

	def __str__(self):
		return self.title


class Faction(models.Model):
	name = models.CharField(max_length = 200)
	desc = models.CharField(max_length = 10000, default = 'A great and noble faction')
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	color = ColorField(default='#FF0000')
	image = models.ImageField(upload_to = 'static/images/', default = 'static/images/no-img.jpg')
	
	def  __str__(self):
		"""Return a string representation of the model."""
		return self.name