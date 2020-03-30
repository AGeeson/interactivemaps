from django.contrib import admin

# Register your models here.

from outdoorx.models import Topic, Entry, Location, Faction

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Location)
admin.site.register(Faction)

