from pprint import pprint
from geopy.geocoders import Nominatim
from ripe.atlas.cousteau import ProbeRequest


filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

probe_id_list = []
coordinatelist=[]
for probe in probes:
    coordinatelist.append(probe['geometry']['coordinates'])
    probe_id_list.append(probe['id'])

oslo_probe = probe_id_list.index(3452)

probe_id_list.remove(probe_id_list[oslo_probe])
coordinatelist.remove(coordinatelist[oslo_probe])

flip_list=[]
for coordinate in coordinatelist:
    lon=str(coordinate[0])
    lat=str(coordinate[1])
    coordinates= (lat + ', ' + lon)
    flip_list.append(coordinates)

geolocator = Nominatim(user_agent="probelist_sweden", timeout=None)


location_list=[]
coordinates = flip_list
for coor in coordinates:
    location = geolocator.reverse(coor)
    if 'address' in location.raw:
        if 'state' in location.raw['address']:
            lan = location.raw['address']['state']
            location_list.append(lan)

keys = probe_id_list
values = location_list

location_dict = {k: v for k, v in zip(keys, values)}

lan_dict = {}
for key, value in location_dict.items():
    if value not in lan_dict:
        lan_dict[value] = [key]
    else:
        lan_dict[value].append(key)


print(lan_dict)