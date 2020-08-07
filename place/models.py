from django.db import models

class Species(models.Model):
    scientific_name = models.CharField(max_length=500)
    name_code = models.CharField(max_length=500)
    vernacular_name = models.CharField(max_length=500)

class Link(models.Model):
    CAT_CHOICES = [
        ('rule', '相關規範'),
        ('admin', '所有權/管理單位'),
        ('sponsor', '認養單位'),
    ]

    title = models.CharField(max_length=500)
    url = models.URLField()
    category = models.CharField(max_length=32, choices=CAT_CHOICES)


class Place(models.Model):
    #id = models.TextField()
    county = models.CharField(blank=True, null=True, max_length=500)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    place_type = models.CharField('用地類型', blank=True, null=True, max_length=500)
    action_type = models.CharField('推動形式', blank=True, null=True, max_length=500)
    owner = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category':'admin'}, related_name='owner_places')
    administrator = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category':'admin'}, related_name='admin_places')
    sponsor = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category': 'sponsor'}, related_name='sponsor_places')
    link = models.URLField('相簿與討論區', blank=True, null=True)
    cover_url= models.URLField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    #x97 = models.TextField(blank=True, null=True)
    #y97 = models.TextField(blank=True, null=True)
    tree_info = models.TextField(blank=True, null=True)
    check_info = models.TextField(blank=True, null=True)
    species_list = models.ManyToManyField(Species, related_name='places')

    #land_script_url_list
    #filter = models.TextField(blank=True, null=True)
    #desc_long = models.TextField(blank=True, null=True)
    #desc_detailed = models.TextField(blank=True, null=True)
    #button_label = models.TextField(blank=True, null=True)
    #is_multi = models.TextField(blank=True, null=True)
    #shape_area = models.TextField(blank=True, null=True)
    #size_available = models.TextField(blank=True, null=True)
    #replant_size = models.TextField(blank=True, null=True)
    #revised_replant_size = models.TextField(blank=True, null=True)


def get_image_path(instance, filename):
    #print (instance, filename, instance.collection, instance.pk)
    print (instance.CAT, instance)
    if instance.pk:
        place_id = instance.place_id
        ext = filename.split('.')[-1].lower()
        path = 'place/{}/{}.{}'.format(place_id, instance.pk, ext)
        #exist_path = os.path.join(settings.MEDIA_ROOT, path)
        return path
    return ''


class RelatedImage(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    url= models.URLField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(RelatedImage, self).save(*args, **kwargs)
            self.image = saved_image

        super(RelatedImage, self).save(*args, **kwargs)

        class Meta:
            abstract = True

class LandScriptImage(RelatedImage):
    CAT = 'land_script'

    place = models.ForeignKey(Place, related_name='land_script_images', on_delete=models.SET_NULL, null=True)

class UnlimitedCitiesImage(RelatedImage):
    CAT = 'unlimited_cities'

    place = models.ForeignKey(Place, related_name='unlimited_cities_images', on_delete=models.SET_NULL, null=True)
