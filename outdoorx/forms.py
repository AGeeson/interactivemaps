from django import forms
from .models import Topic, Entry, Location

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text':''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class LocationForm(forms.ModelForm):
	latitude = forms.DecimalField(label= 'Latitude',
                           widget= forms.HiddenInput
                           (attrs={'id':'latbox'}))
	longitude = forms.DecimalField(label='Longitude',
                           widget= forms.HiddenInput
                           (attrs={'id':'lngbox'}))

	class Meta:
		model = Location
		comment = forms.CharField()
		your_name = forms.CharField(label='Your name', max_length=100)
		fields = ['title','image','type_of_excercise','type_of_location','equipment','latitude','longitude',]
		labels = {
		'title': 'Name Your Spot (3-5 Words)',
		# 'latitude': 'Latitude',
		# 'longitude': 'Longitude',
		'image':'Upload Pictures',
		'type_of_location': 'Type of Location',
		'type_of_excercise': ' Type of Activity',
		'equipment':'Is There Any Equipment?',
		}
		# widgets = {
		#	'latitude': 'forms.TextInput(attrs={id: latbox}',
		# }
		#widgets = {
        #    'latitude': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
		
		image = forms.ImageField()
		# docfile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Upload any Pictures of Your Location')
		

