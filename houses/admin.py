from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from.models import House


@admin.register(House)
class HouseAdmin(GISModelAdmin):
    list_display = ('id', 'number', 'bedrooms','location',)
    
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 8,
            'default_lat': 50.324422739309384,
            'default_lon': 8.887939453125,
        },
    }
