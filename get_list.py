from ripe.atlas.cousteau import ProbeRequest
import pprint
def main():

    filters = {"country_code": "SE"}
    probes = ProbeRequest(**filters)

    probelist = []
    for probe in probes:
        probelist.append([probe['asn_v4'], probe['description'], probe['geometry']['coordinates']])

    pprint.pprint(probelist)
if __name__ == '__main__':
    main()
