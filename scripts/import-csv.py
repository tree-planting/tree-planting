import csv

from place.models import Place

counter = 0
link = {
    'rule': {},
    'admin': {},
    'sponsor': {},
}
with open('dump-sheet2site-200807.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        #print (row)
        if counter > 0:
            a = row[0] #source_id
            b = row[1] # county
            c = row[2] # name
            d = row[3] #county-name
            e = row[4] # descr
            f = row[5] # locality
            g = row[6] # 用地屬性
            h = row[7] # link
            i = row[8] # cover_url
            j = row[9] # lat
            k = row[10] # lon
            l = row[11] # 97x
            m = row[12] # 97y
            n = row[13] # 諮詢對象-民間/公部門
            o = row[14] # 對策
            p = row[15] # 行動類
            q = row[16] # filter
            r = row[17] # long_descr
            s = row[18] # detail descr
            t = row[19] # button text
            u = row[20] # area
            v = row[21] # owner
            w = row[22] # admin
            x = row[23] # code
            y = row[24] # rule
            z = row[25] # recommand
            aa = row[26] #landscript
            ab = row[27] # unlimitedcity
            ac = row[28] # ref case
            ad = row[29] # nursery
            ae = row[30] # botanic garden

            action_type = ''
            if p:
                for act in Place.ACTION_CHOICES:
                    if act[1] == p:
                        action_type = act[0]
            rule = ''
            #if y:
            #    y1= y.replace('(', '')
            #    y1 = y1.replace(')', '')
            #    y1 = y1.split(',')
            #    if len(y1) > 1:

            get_place = Place.objects.filter(id=a).first()
            if get_place:
                get_place.description = e
                get_place.save()
            else:
                place = Place(
                    source_id=a,
                    county=b,
                    title=c,
                    description=e,
                    action_type=action_type,
                    place_type=g,
                    rule_text=y,
                    owner_text=v,
                    administrator_text=w,
                    contact_text=n,
                    nursery_text=ad,
                    garden_text=ae,
                    link=h,
                    cover_url=i,
                    lat=j,
                    lon=k,
                )
            place.save()
        counter +=1
