from django.urls import path
from .views import edit_entry, News, index, Contact, topics, topic, new_topic, new_entry

urlpatterns = [
    path('News', News, name = 'News'),
    path('', index, name = 'index'),
    path('Contact', Contact, name = 'Contact'),
    path('topics', topics, name='topics'),
    path('topics/<int:topic_id>/)', topic, name='topic'),
    path('new_topic/', new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', edit_entry, name='edit_entry'),

]
