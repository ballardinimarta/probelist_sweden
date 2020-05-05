import json
from pprint import pprint
from urllib.request import urlopen
from probedict import kommun_dict
import pandas as pd

probes={}
for x in kommun_dict:
    kommun_dict
    probes[x]=len(kommun_dict[x])

probe_data = pd.DataFrame.from_dict(probes, orient='index', columns=['antal'])


with urlopen('http://kodapan.se/geodata/data/2015-06-26/kommuner-kustlinjer.geo.json') as res:
    kommuner = json.load(res)


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



print('kommuner_geojson = {}'.format(kommuner) )
