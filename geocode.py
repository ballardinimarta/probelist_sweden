import pprint
import reverse_geocoder as rg
from ripe.atlas.cousteau import ProbeRequest

filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

probelist = []
coordinatelist=[]
for probe in probes:
    coordinatelist.append(probe['geometry']['coordinates'])

flip_list=[]
for coordinate in coordinatelist:
    lon=coordinate[0]
    lat=coordinate[1]
    coordinates= ((lat, lon))
    flip_list.append(coordinates)

location_list=[]
coordinates = flip_list
location = rg.search(coordinates)
for dict in location:
    if 'admin2' in dict:
        kommun = dict['admin2']
        location_list.append(kommun)

pprint.pprint(location_list)