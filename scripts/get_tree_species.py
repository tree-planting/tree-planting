import pandas as pd
import requests
import csv

from place.models import Place, Species

counter = 0
sp_code_map = {'台灣油杉': '201103', '槲櫟': '203314', '森氏紅淡比': '204799', '大明橘': '433722', '鐘萼木': '204436', '流蘇': '204565', '豆梨': '204186', '天料木': '204990', '臺灣紅豆樹': '416302', '台灣梭羅木': '203709', '莿桐': '203134', '刺葉桂櫻': '424209', '南投黃肉楠': '', '樟樹': '203590', '台灣蘋果': '204152', '楓香': '203430', '無患子': '204487', '魚木': '434999', '楝樹': '204445', '大葉山欖': '202853', '毛柿': '202850', '臺灣海棗': '201181', '瓊崖海棠': '204758', '浸水營石櫟': '430736', '武威山烏皮茶': '400967', '穗花棋盤腳': '203659', '鐵釘樹': '203614', '太魯閣櫟': '203322', '細葉蚊母樹': '203427', '光臘樹': '400871', '灰背櫟': '430742', '大武石櫟': 'Kew-114512', '茄冬': '202952'}


for i in sp_code_map:
    print (i, sp_code_map[i])
    sp = Species(vernacular_name=i)
    if sp_code_map[i]:
        sp.name_code = sp_code_map[i]
        # sp.save()
        api = 'https://data.taieol.tw/eol/endpoint/taxondesc/species/{}'.format(sp.name_code)
        r = requests.get(api)
        data = r.json()
        sp.description = data['description']
        sp.locality = data['distribution']
        sp.scientific_name = data['name']
    sp.save()

