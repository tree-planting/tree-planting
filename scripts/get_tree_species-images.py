import json

import requests

from place.models import Species



for i in Species.objects.all():
    if i.name_code:
        req = requests.get('https://data.taieol.tw/eol/endpoint/image/species/{}'.format(i.name_code))
        print (i)
        print (req.json())
        i.image_list = json.dumps(req.json())
        i.save()
