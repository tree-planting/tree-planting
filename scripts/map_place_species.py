import csv

from place.models import Species, Place
counter = 0

with open('dump-sheet2site-200807.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if counter >= 1:
            sp = row[25]
            source_id = row[0]
            pl = Place.objects.get(pk=source_id)
            species_list = []
            if sp_list := sp.split(','):
                for x in sp_list:
                    if x:
                        species = Species.objects.filter(vernacular_name=x).first()
                        if species:
                            species_list.append(species)
                            #print (species)
                        else:
                            print ('not found', x)
            if species_list:
                pl.species_list.set(species_list)
                pl.save()
        counter += 1

