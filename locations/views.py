from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Location
from .forms import LocationForm

def locations(request):
	locations = Locations.objects.filter(owner=request.user).order_by('date_added')
	locations = Locations.order_by('date_added')
	context = {'locations' : locations}
	return render(request, 'locations/locations.html')

# Create your views here.
@login_required
def new_location(request): 
	if request.method != 'POST':
		form = LocationForm()
	else:
		form = LocationForm(request.POST)
		if form.is_valid():
			new_location = form.save(commit=False)
			new_location.owner = request.user
			new_location.save()
			return HttpResponseRedirect(reverse('locations'))
	context = {'form': form}
	return render(request, 'locations/new_location.html', context)


def location(request, topic_id):
	location = Location.objects.get(id=topic_id)
	if location.owner!= request.user:
		raise Http404
	context = {'topic': topic}
	return render(request, 'locations/location.html', context)