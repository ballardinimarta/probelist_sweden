from geopy.geocoders import Nominatim
from ripe.atlas.cousteau import ProbeRequest

def get_location(status):

    if status == 'connected':
        status = {"country_code": "SE", "status": "1"}
        print('loading all connected probes in sweden...')

    if status == 'disconnected':
        status = {"country_code": "SE", "status": "2"}
        print('loading all disconnected probes in sweden...')

    if status == 'abandoned':
        status = {"country_code": "SE", "status": "3"}
        print('loading all abandoned probes in sweden...')

    if status == 'all':
        status = {"country_code": "SE"}
        print('loading all probes in sweden...')

    filters = status
    probes = ProbeRequest(**filters)

    probe_id_list = []
    coordinatelist=[]
    for probe in probes:
        coordinatelist.append(probe['geometry']['coordinates'])
        probe_id_list.append(probe['id'])
    try:
        oslo_probe = probe_id_list.index(3452)
    except ValueError:
        pass
    else:
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

    def print_nice(lan_dict):
        for lan, id in lan_dict.items():
            print("{}:\n {}".format(lan, id))
        print('Antal län : %d' % len(lan_dict))


    print_nice(lan_dict)

# get_location('all') gives you all probes
# get_location('connected') gives you all connected probes
# get_location('disconnected') gives you all disconnected probes
# get_location('abandoned') gives you all abandoned probes

get_location('all')# here is where you change
