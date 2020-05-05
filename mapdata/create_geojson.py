import json
from pprint import pprint
from urllib.request import urlopen
import pandas as pd
from mapdict import mapdict

# Write a new updated kommun dict to use later at import
mapdict()

# import the dictionary after it is updated
from probedict import kommun_dict

# Change the values from ID to the amount of probes
probes={}
for x in kommun_dict:
    kommun_dict
    probes[x]=len(kommun_dict[x])

# Make that dictionary a pandas DataFrame
probe_data = pd.DataFrame.from_dict(probes, orient='index', columns=['antal'])

# Get the geojsonfile with the polygons of swedish municipalities
with urlopen('http://kodapan.se/geodata/data/2015-06-26/kommuner-kustlinjer.geo.json') as res:
    kommuner = json.load(res)

# Append the ammount of probes for every municipaliy in to the geojson file
for x in kommuner['features']:
    for k in probe_data.index:
        if k in x['properties']['name']:
            x['properties']['probes']= str(probe_data.antal[k])
for x in kommuner['features']:
    try:
        x['properties']['probes']
        pass
    except KeyError:
        x['properties']['probes'] = '0'

# Print to the already exisiting geojson file in the same folder
def geojson_print(kommuner):
    with open('mapdata/sveriges_kommuner.geojson', 'w') as skg:
        print('kommuner_geojson = {}'.format(kommuner), file = skg)

geojson_print(kommuner)
