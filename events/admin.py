import admin_thumbnails
from django.contrib import admin

from events.models import Event


@admin.register(Event)
@admin_thumbnails.thumbnail('image', background=True)
class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'date', 'image', 'image_thumbnail']
    list_display = ['id', 'title', 'date', 'image_thumbnail']
    list_filter = ['date', 'organisations']
    search_fields = ['id', 'title']