from ripe.atlas.cousteau import ProbeRequest
from pprint import pprint

filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

probelist = []
for probe in probes:
    probelist.append([probe['asn_v4'], probe['description'], probe['geometry']['coordinates'], probe['status']])

pprint(probelist)