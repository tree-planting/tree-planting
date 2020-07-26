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
        }
