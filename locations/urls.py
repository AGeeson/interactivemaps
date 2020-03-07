from django.urls import path
from .views import new_location, locations

app_name = 'locations'

urlpatterns = [
	path('new_location/', new_location, name='new_location'),
	path('', locations, name='locations'),
	
	
]
