from django import forms

from .models import Location

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['text']
		labels = {'text': 'what is good for? eg Bodyweight, Cardio'}
		
