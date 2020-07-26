from django.db import models

class Place(models.Model):
    #id = models.TextField()
    county = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    place_type = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    x97 = models.TextField(blank=True, null=True)
    y97 = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)
    desc_long = models.TextField(blank=True, null=True)
    desc_detailed = models.TextField(blank=True, null=True)
    button_label = models.TextField(blank=True, null=True)
    is_multi = models.TextField(blank=True, null=True)
    shape_area = models.TextField(blank=True, null=True)
    size_available = models.TextField(blank=True, null=True)
    replant_size = models.TextField(blank=True, null=True)
    revised_replant_size = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)

    def tojson(self):
        return {
            'county': self.county,
            'name': self.name,
            'description': self.description,
            'area': self.area,
            'place_type': self.place_type,
            'link': self.link,
            'cover': self.cover,
            'lat': self.lat,
            'lon': self.lon,
            'x97': self.x97,
            'y97': self.y97,
            'organization': self.organization,
            'action': self.action,
            'title': self.title,
            'filter': self.filter,
            'desc_long': self.desc_long,
            'desc_detailed': self.desc_detailed,
            'button_label': self.button_label,
            'is_multi': self.is_multi,
            'shape_area': self.shape_area,
            'size_available': self.size_available,
            'replant_size': self.replant_size,
            'revised_replant_size': self.revised_replant_size,
            'unit': self.unit,
        }
