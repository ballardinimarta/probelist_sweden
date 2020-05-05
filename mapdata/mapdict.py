from geopy.geocoders import Nominatim
from ripe.atlas.cousteau import ProbeRequest
from pprint import pprint


filters_1 = {"country_code": "SE", "status": "1"}
filters_2 = {"country_code": "SE", "status": "2"}
probes_con = ProbeRequest(**filters_1)
probes_dis_con = ProbeRequest(**filters_2)


probe_id_list = []
coordinatelist=[]
for probe in probes_con:
    coordinatelist.append(probe['geometry']['coordinates'])
    probe_id_list.append(probe['id'])
for probe in probes_dis_con:
    coordinatelist.append(probe['geometry']['coordinates'])
    probe_id_list.append(probe['id'])

try:
    oslo_probe = probe_id_list.index(3452)
except ValueError:
    pass
else:
    probe_id_list.remove(probe_id_list[oslo_probe])
    coordinatelist.remove(coordinatelist[oslo_probe])
try:
    lilla_vartan = probe_id_list.index(31950)
except ValueError:
    pass
else:
    probe_id_list.remove(probe_id_list[lilla_vartan])
    coordinatelist.remove(coordinatelist[lilla_vartan])


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
        if 'municipality' in location.raw['address']:
            kommun = location.raw['address']['municipality']
            location_list.append(kommun)
        elif 'town' in location.raw['address']:
            town = location.raw['address']['town']
            location_list.append(town)


keys = probe_id_list
values = location_list


location_dict = {k: v for k, v in zip(keys, values)}

kommun_dict = {}
for key, value in location_dict.items():
    if value not in kommun_dict:
        kommun_dict[value] = [key]
    else:
        kommun_dict[value].append(key)

for x in list(kommun_dict):
    if 'Göteborgs Stad' in x:
        kommun_dict['Göteborgs kommun'] = kommun_dict.pop('Göteborgs Stad')

def print_nice(kommun_dict):
    for kommun, id in kommun_dict.items():
        print("{}:\n {}\n".format(kommun, id))
    print('Antal kommuner : %d/290' % len(kommun_dict))

def dict_print(kommun_dict):
    print('kommun_dict={}'.format(kommun_dict))

dict_print(kommun_dict)
