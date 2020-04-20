# probelist_sweden
This is a program to find information on the Ripe Atlas probes and anchors that are located in sweden
https://atlas.ripe.net/results/maps/network-coverage/?filter=Sweden+(se)

## get_asn.py
This script gets you a python dictionary of the ASN correlating to the networkprovider of that ASN 
(ASN stands for Autonomous System Number).

To run the script you do not have to adjust anything its ready to run.

```bash
$ python3 get_asn.py
```
you should get a dictionary with about 119 values.

## get_geocode.py
This script gets you a python dictionary of the probe id correlating to its state where its located.

To run the script you do not have to adjust anything its ready to run.

```bash
$ python3 get_geocode.py
```
you should get a dictionary with about 393 values.

<b>Note that this script uses a library which is a wrapper for the google api, so to run the script can take a while.<b> 
