from pprint import pprint
import reverse_geocoder as rg
from ripe.atlas.cousteau import ProbeRequest

filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

probe_id_list = []
coordinatelist=[]
for probe in probes:
    coordinatelist.append(probe['geometry']['coordinates'])
    probe_id_list.append(probe['id'])

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

keys = probe_id_list
values = location_list

location_dict = {k: v for k, v in zip(keys, values)}

pprint(location_dict)
