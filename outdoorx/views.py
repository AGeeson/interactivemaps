from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Location, Faction
from .forms import TopicForm, EntryForm, LocationForm

# Create your views here.
def factions(request):
	factions = Faction.objects.filter(owner=request.user).order_by('date_added')
	factions = Faction.objects.order_by('date_added')
	context = {'factions' : factions, }
	return render(request, 'master/factions.html', context)


def success(request):
	return render(request, 'master/success.html')

def index(request):
	locations = Location.objects.filter(owner=request.user).order_by('date_added')
	locations = Location.objects.order_by('date_added')
	coords = []
 	# for location in Location.latlng coords.append()
	context = {'locations' : locations, 'coords': coords}
	return render(request, 'master/index.html', context)


def News(request):
	return HttpResponse("<h1>This is our latest news</h1>")

def Contact(request):
	return HttpResponse("<h1>Contact us here!</h1>")

@login_required
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'master/topics.html', context)

@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if topic.owner!= request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries' : entries}
	return render(request, 'master/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted ; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data. 
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('topics'))
	context = {'form': form}
	return render(request, 'master/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'master/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topic', args=[topic_id]))

	context = {'entry': entry, 'topic': topic, 'form':form}
	return render(request, 'master/edit_entry.html', context)

def locations(request):
	locations = Location.objects.filter(owner=request.user).order_by('date_added')
	locations = Location.objects.order_by('date_added')
	coords = []
 	# for location in Location.latlng coords.append()
	context = {'locations' : locations, 'coords': coords}
	return render(request, 'master/locations.html', context)


def location(request, location_id):
	location = Location.objects.get(id=location_id)
	if location.owner!= request.user:
		raise Http404
	context = {'location': location}
	return render(request, 'master/location.html', context)

def new_location(request):
	if request.method != 'POST':
		# No data submitted ; create a blank form.
		form = LocationForm()
	else:
		# POST data submitted; process data. 
		form = LocationForm(request.POST, request.FILES)
		test = request.POST.get("latlng")
		if form.is_valid():
			new_location = form.save(commit=False)
			new_location.owner = request.user
			new_location.save()
			return HttpResponseRedirect(reverse('locations'))
	context = {'form': form}
	return render(request, 'master/new_location.html', context)