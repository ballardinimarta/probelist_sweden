from urllib import request
import json
from ripe.atlas.cousteau import ProbeRequest
from pprint import pprint

filters = {"country_code": "SE"}
probes = ProbeRequest(**filters)

asnlist = []
for probe in probes:
    asnlist.append(probe['asn_v4'])

network_list = []
for asn in asnlist:
    if asn is not None:
        url = ("https://stat.ripe.net/data/as-overview/data.json?resource=AS%s" % asn)

        response = request.urlopen(url)

        data = json.loads(response.read())

        networkprovider = data['data']['holder']

        network_list.append([asn , networkprovider])

pprint(network_list)
