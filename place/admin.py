from django.contrib import admin

from .models import (
    Place
)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place

#    search_fields=['species_name', 'species_name_zh', 'family_name', 'family_name_zh', 'verbatim_scientific_name']