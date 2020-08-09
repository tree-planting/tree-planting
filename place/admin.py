
from django.contrib import admin

from .models import (
    Place,
    InfoText,
    LandScriptImage,
    UnlimitedCitiesImage,
)


class LandScriptInlineAdmin(admin.TabularInline):
   model = LandScriptImage
   extra = 0


class UnlimitedCitiesInlineAdmin(admin.TabularInline):
   model = UnlimitedCitiesImage
   extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = Place
    list_display = ('id', 'county', 'title', 'place_type')
    inlines = (LandScriptInlineAdmin, UnlimitedCitiesInlineAdmin)
#    search_fields=['species_name', 'species_name_zh', 'family_name', 'family_name_zh', 'verbatim_scientific_name']

@admin.register(InfoText)
class InfoTextAdmin(admin.ModelAdmin):
    model = InfoText
