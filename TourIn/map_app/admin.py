from django.contrib import admin

from .models import *

from leaflet.admin import LeafletGeoAdmin

class PlacesAdmin(LeafletGeoAdmin):

    list_display        =       ('place_name', 'location')

admin.site.register(Places, PlacesAdmin)
