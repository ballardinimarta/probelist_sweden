from urllib import request
import json
from ripe.atlas.cousteau import ProbeRequest

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

def print_nice(asn_dict):
    print('A dictionary of the ASNs of the Ripe Atlas probes in Sweden and their correlating network provider in the format of ASN : network provider ')
    for asn, network in asn_dict.items():
        print("{}:\n {}\n".format(asn, network))

print(asn_dict)
