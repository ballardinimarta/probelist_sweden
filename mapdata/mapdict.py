from geopy.geocoders import Nominatim
from ripe.atlas.cousteau import ProbeRequest
from pprint import pprint

def mapdict():
    # Filters for all connected and disconncted probes
    filters_1 = {"country_code": "SE", "status": "1"}
    filters_2 = {"country_code": "SE", "status": "2"}

    # Get the probes from those filters
    probes_con = ProbeRequest(**filters_1)
    probes_dis_con = ProbeRequest(**filters_2)

    # Take out coordinates and ids to separate lists
    probe_id_list = []
    coordinatelist=[]
    for probe in probes_con:
        coordinatelist.append(probe['geometry']['coordinates'])
        probe_id_list.append(probe['id'])
    for probe in probes_dis_con:
        coordinatelist.append(probe['geometry']['coordinates'])
        probe_id_list.append(probe['id'])

    # Flip the order so its Lat, Lon
    flip_list=[]
    for coordinate in coordinatelist:
        lon=str(coordinate[0])
        lat=str(coordinate[1])
        coordinates= (lat + ', ' + lon)
        flip_list.append(coordinates)
    # Set geolocator
    geolocator = Nominatim(user_agent="probelist_sweden", timeout=None)

    # Get the municipality of the coordinates
    # Some off adresses does not have a stated municipality but the 'town' key instead has the municipality information
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

    # Make the list a dictionary
    location_dict = {k: v for k, v in zip(keys, values)}

    # Make a new dict where municipality is key and ids are the values
    kommun_dict = {}
    for key, value in location_dict.items():
        if value not in kommun_dict:
            kommun_dict[value] = [key]
        else:
            kommun_dict[value].append(key)

    # 'Göteborgs kommun' is stated as 'Göteborgs Stad' so we change that for later on
    for x in list(kommun_dict):
        if 'Göteborgs Stad' in x:
            kommun_dict['Göteborgs kommun'] = kommun_dict.pop('Göteborgs Stad')

    # Print it in the form of a dictionary that is called 'kommun_dict' and print the output to a file called 'probedict.py'
    def dict_print(kommun_dict):
        with open('mapdata/probedict.py', 'w') as pbd:
            print('kommun_dict={}'.format(kommun_dict), file=pbd)

    dict_print(kommun_dict)

mapdict()
