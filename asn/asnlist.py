from asn import asnprobe
from pprint import pprint

gavlix = [47970, 43065, 16117, 20626, 1653, 25417, 28847, 28954, 60213, 206114, 210140, 20625, 208201, 51132]
sthix = []
with open('asn/sthix.txt') as f:
    for line in f:
        for word in line.split():
            try:
                n = int(word)
                sthix.append(n)
            except ValueError:
                pass
    for x in sthix:
        if x < 6000:
            sthix.remove(x)
netnod = []
with open('asn/netnod.txt') as f:
    for line in f:
        for word in line.split():
            try:
                n = int(word)
                netnod.append(n)
            except ValueError:
                pass


def gavlix_check():
    asnumber = asnprobe.keys()
    no_probe=[]
    for x in gavlix:
        if x not in asnumber:
            no_probe.append(x)
    print('The AS that do not have a ripe atlas probe (ASNs from gavlix)')
    pprint(no_probe)

def netnod_check():
    asnumber = asnprobe.keys()
    no_probe=[]
    for x in netnod:
        if x not in asnumber:
            no_probe.append(x)
    print('The AS that do not have a ripe atlas probe (ASNs from netnod)')
    pprint(no_probe)

def sthix_check():
    asnumber = asnprobe.keys()
    no_probe=[]
    for x in sthix:
        if x not in asnumber:
            no_probe.append(x)
    print('The AS that do not have a ripe atlas probe (ASNs from sthix)')
    pprint(no_probe)

gavlix_check()
netnod_check()
sthix_check()
