# probelist_sweden
This is a program to find information on the Ripe Atlas probes and anchors that are located in sweden
https://atlas.ripe.net/results/maps/network-coverage/?filter=Sweden+(se)

## How to use
#### Clone this repo
```bash
$ git clone https://github.com/ballardinimarta/probelist_sweden.git
```

#### Install requirements
```bash
$ pip install -r requirements.txt
```
## get_asn.py
This script gets you a python dictionary of the ASN correlating to the network provider of that ASN
(ASN stands for Autonomous System Number).

To run the script you do not have to adjust anything its ready to run.

```bash
$ python3 asn/get_asn.py
```
you should get a dictionary with about 119 values.

But if you just want the results i have a txt file called <b>asndict.txt</b> that you can look at.

asndict.txt is the output of get_asn.py at 21/04 -2020

## get_geocode.py
This script gets you a python dictionary of the 21 regions or the 290 municipalitys in Sweden and the probes that are located in that region/municipality.

#### customize
To run the script you can choose if you either want to use get_lan()(for regions) or get_kommun()(for municipalitys). But if you want to see only the connected, disconnected or abandoned probes you can go to get_geocode.py and at the bottom change to your liking.

```bash
# get_lan/get_kommun('all') gives you all probes
# get_lan/get_kommun('connected') gives you all connected probes
# get_lan/get_kommun('disconnected') gives you all disconnected probes
# get_lan/get_kommun('abandoned') gives you all abandoned probes

get_lan('all')# here is where you change
get_kommun('all')# here is where you change
```
then after you adjusted the script to what output you want, just run the script.

```bash
$ python3 location/get_geocode.py
```

<b>Note that this script uses a library which is a wrapper for the google api, so to run the script can take a while.</b>

But if you just want the results of
```bash
get_lan('all')
```
or
```bash
get_kommun('all')
```

i have a txt file called <b>landict.txt</b> or <b>kommundict.txt</b> that you can look at.

landict.txt is the output of get_geocode.py at 21/04 -2020

kommundict.txt is the output of get_geocode.py at 23/04 -2020

## get_missing.py
A script to find out the municipalities in Sweden that do not have a Ripe Atlas probe

You do not have to change anything it is ready to run
```bash
$ python3 location/get_missing.py
```
if you only want to see the output i have a txt file with the output from 23/4-2020 called <b>missinglist.txt</b>
