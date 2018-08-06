from django.contrib import admin

from .models import Pin

class PinAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'image', 'created']
	list_filter = ['created']

admin.site.register(Pin, PinAdmin)