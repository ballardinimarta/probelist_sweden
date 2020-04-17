from urllib import request
import json
from ripe.atlas.cousteau import ProbeRequest
from pprint import pprint

filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

all_asn_list = []
for probe in probes:
    all_asn_list.append(probe['asn_v4'])

not_none_asn_list =[]
network_list = []
for asn in all_asn_list:
    if asn is not None:
        url = ("https://stat.ripe.net/data/as-overview/data.json?resource=AS%s" % asn)

        response = request.urlopen(url)

        data = json.loads(response.read())

        networkprovider = data['data']['holder']

        network_list.append(networkprovider)
        not_none_asn_list.append(asn)

keys = not_none_asn_list
values = network_list
asn_dict = {k: v for k, v in zip(keys, values)}


pprint(asn_dict)
