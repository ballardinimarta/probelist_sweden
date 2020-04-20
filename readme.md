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
This script gets you a python dictionary of the 21 states of sweden and the probes that are located in that state.

To run the script you do not have to adjust anything its ready to run.

```bash
$ python3 get_geocode.py
```
you should get a dictionary with 21 keys that each have different amount of values .

<b>Note that this script uses a library which is a wrapper for the google api, so to run the script can take a while. But if you just want the results i have a txt file called landict.txt that you can look at.<b> 
landict.txt is the output of get_geocode.py at 20/04 -2020 
