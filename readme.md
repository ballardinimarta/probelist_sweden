# probelist_sweden
This is a program to find information on the Ripe Atlas probes and anchors that are located in Sweden
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
## map.html
<<<<<<< HEAD
If you like graphics and want to see a map of Sweden, with the municipalities with probes highlighted you can either look at the link to the visualisation of my html-file [map.html](https://ballardinimarta.github.io/probelist_sweden/map.html)
=======
If you like graphics and want to see a map of sweden, with the municipalities with probes highlighted you can either look at the link to the visualisation of my html-file [map.html](https://ballardinimarta.github.io/probelist_sweden/map.html)
>>>>>>> b16f9e4f7af72590673135074eb60d1c828a90c6

or clone my repo and open it in your browser in file-mode.

To update the information of the map, i.e. the ripe atlas data, you simply have to run
```bash
$ python3 mapdata/create_geojson.py
```
it takes quite a long time to run but after that your data for map.html is updated
## get_asn.py
This script gets you a python dictionary of the ASN correlating to the network provider of that ASN
(ASN stands for Autonomous System Number).

To run the script you do not have to adjust anything its ready to run.

```bash
$ python3 asn/get_asn.py
```
you should get a dictionary with about 119 values.

But if you just want the results i have a txt file called <b>asndict.txt</b> that you can look at. Find it under [asn/output](https://github.com/ballardinimarta/probelist_sweden/tree/master/asn/output)

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

i have a txt file called <b>landict.txt</b> or <b>kommundict.txt</b> that you can look at under [location/output](https://github.com/ballardinimarta/probelist_sweden/tree/master/location/output).

landict.txt is the output of get_geocode.py at 21/04 -2020

kommundict.txt is the output of get_geocode.py at 23/04 -2020

## get_missing.py
A script to find out the municipalities in Sweden that do not have a Ripe Atlas probe

You do not have to change anything it is ready to run
```bash
$ python3 location/get_missing.py
```
if you only want to see the output i have a txt file with the output from 23/4-2020 called <b>missinglist.txt</b>you can find it at [location/output](https://github.com/ballardinimarta/probelist_sweden/tree/master/location/output)
