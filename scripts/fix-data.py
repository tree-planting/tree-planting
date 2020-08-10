import csv

from place.models import Species, Place
counter = 0

with open('dump-sheet2site-200811.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if counter >= 1:
            source_id = row[0]
            green_case = row[28]
            pl = Place.objects.get(pk=source_id)
            print (pl.case_text, '|||',green_case)
            pl.case_text = green_case
            pl.save()
            
        counter += 1
