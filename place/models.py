import re

from django.db import models

def find_links(s):
    #print ('======', s)
    #m = re.search(r'\((.+)\)', s)
    #if m and m.group(1):
    #    print (m.group(1))
    # TODO recursive find pattern
    links = []
    if '),(' in s:
        slist = s.split('),(')
        for i in slist:
            p = i.replace(')', '').replace('(', '')
            if ',' in p:
                q = p.split(',')
                links.append('<a href={} target="_blank" class="text is-link">{}</a>'.format(q[1], q[0]))
            else:
                links.append(p)
    else:
        p = s.replace(')', '').replace('(', '')
        if ',' in p:
            q = p.split(',')
            links.append('<a href={} target=_"blank" class="text is-link">{}</a>'.format(q[1], q[0]))
        else:
            links.append(p)

    return ', '.join(links)


class Species(models.Model):
    scientific_name = models.CharField(max_length=500)
    name_code = models.CharField(max_length=500)
    vernacular_name = models.CharField(max_length=500)


class InfoText(models.Model):
    name = models.CharField(max_length=500)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return '<InfoText({}) {}>'.format(self.id, self.name)


class Link(models.Model):
    CAT_CHOICES = [
        ('rule', '相關規範'),
        ('admin', '所有權/管理單位'),
        ('sponsor', '認養單位'),
        ('contact', '諮詢對象-民間/公部門'),
        ('nursery', '苗圃'),
        ('garden', '植物園與環教場所'),
        ('case', '參考綠化案例'),
    ]

    title = models.CharField(max_length=500)
    url = models.URLField()
    category = models.CharField(max_length=32, choices=CAT_CHOICES)


class Place(models.Model):
    ACTION_CHOICES = [
        ('vision', '【願景蒐集型】'),
        ('adopt', '【代管認養型】我要認養'),
        ('donate-gov', '【捐款型】支認公部門綠化業務'),
        ('donate-ngo', '【捐款型】支持民間認養單位'),
        ('environ', '【環境復育型】'),
    ]
    source_id = models.IntegerField(blank=True, null=True)
    county = models.CharField(blank=True, null=True, max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    place_type = models.CharField('用地類型', blank=True, null=True, max_length=500)
    action_type = models.CharField('推動形式', blank=True, null=True, max_length=500, choices=ACTION_CHOICES)

    rule_text = models.TextField('相關規範', blank=True)
    owner_text = models.TextField('所有權單位', blank=True)
    administrator_text = models.TextField('管理單位', blank=True)
    contact_text = models.TextField('諮詢對象-民間/公部門', blank=True)
    sponsor_text = models.TextField('認養單位', blank=True)
    nursery_text = models.TextField('苗圃', blank=True)
    garden_text = models.TextField('植物園與環教場所', blank=True)
    case_text = models.TextField('參考綠化案例', blank=True)

    #contact = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category':'contact'}, related_name='contact_places')
    #owner = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category':'admin'}, related_name='owner_places')
    #administrator = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category':'admin'}, related_name='admin_places')
    #sponsor = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'category': 'sponsor'}, related_name='sponsor_places')
    link = models.URLField('相簿與討論區', blank=True, null=True)
    cover_url= models.TextField(blank=True, null=True) # only fit 200 chars
    lat = models.CharField(blank=True, null=True, max_length=500)
    lon = models.CharField(blank=True, null=True, max_length=500)
    #x97 = models.TextField(blank=True, null=True)
    #y97 = models.TextField(blank=True, null=True)
    #tree_info = models.TextField(blank=True, null=True)
    #check_info = models.TextField(blank=True, null=True)
    species_list = models.ManyToManyField(Species, related_name='places', blank=True)

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

    def __str__(self):
        return '<Place {}-{}>'.format(self.county, self.title)

    def get_rule_links(self):
        if not self.owner_text:
            return ''

        return find_links(self.owner_text)

    def get_owner_links(self):
        if not self.owner_text:
            return ''

        return find_links(self.owner_text)

    def get_administrator_links(self):
        if not self.administrator_text:
            return ''

        return find_links(self.administrator_text)


    def get_nursery_links(self):
        if not self.nursery_text:
            return ''

        return find_links(self.nursery_text)

    def get_sponsor_links(self):
        if not self.sponsor_text:
            return ''

        return find_links(self.sponsor_text)

    def get_contact_links(self):
        if not self.contact_text:
            return ''

        return find_links(self.contact_text)

    def get_garden_links(self):
        if not self.garden_text:
            return ''

        return find_links(self.garden_text)

    def get_case_links(self):
        if not self.case_text:
            return ''

        return find_links(self.case_text)

    @property
    def tree_species_info(self):
        if info := InfoText.objects.get(pk=1):
            return info.content

    @property
    def checklist_info(self):
        if info := InfoText.objects.get(pk=2):
            return info.content


def get_image_path(instance, filename):
    #print (instance, filename, instance.collection, instance.pk)
    #print (instance.CAT, instance)
    if instance.pk:
        place_id = instance.place_id
        ext = filename.split('.')[-1].lower()
        path = 'place/{}/{}/{}.{}'.format(place_id, instance.CAT, instance.pk, ext)
        #exist_path = os.path.join(settings.MEDIA_ROOT, path)
        return path
    return ''


class RelatedImage(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True)
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
