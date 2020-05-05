import folium as folium
import pandas as pd
from urllib.request import urlopen
import json
from probedict import kommun_dict
from folium.plugins import MarkerCluster

probes={}
for x in kommun_dict:
    probes[x]=len(kommun_dict[x])

probe_data = pd.DataFrame.from_dict(probes, orient='index', columns=['antal'])

with urlopen('http://kodapan.se/geodata/data/2015-06-26/kommuner-kustlinjer.geo.json') as response:
    kommuner = json.load(response)

for x in kommuner['features']:
    for k in probe_data.index:
        if k in x['properties']['name'] and x['properties']['status'] != 3:
            x['properties']['probes']= str(probe_data.antal[k])
for x in kommuner['features']:
    try:
        x['properties']['probes']
        pass
    except KeyError:
        x['properties']['probes'] = '0'



probe_geo = kommuner

m = folium.Map(location=[62.99,17.64], zoom_start=5)

bins = list(probe_data['antal'].quantile([0,0.000001,0.000002,1]))

mc = MarkerCluster()

markers = folium.Marker(
    with urlopen('https://stat.ripe.net/data/atlas-probes/data.json?resource=SE') as res:
        prober = json.load(res)
    for i in prober:
        location= [prober[i]['latitude'],prober[i]['longitude']],
        popup =('<strong>Probe Status: </strong>'+probes[i]['status_name'] +
                '<br><strong>Probe ID: </strong>'+JSON.stringify(probes[i]['id']) +
                '<br><strong>Probe ASN: </strong>' + JSON.stringify(probes[i]['asn_v4'])+
                '<br><strong>Probe Country: </strong>'+probes[i]['country_code'])
                )

choropleth = folium.Choropleth(
    geo_data=probe_geo,
    name='choropleth',
    data=probe_data,
    columns=[probe_data.index, 'antal'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    highlight=True,
    bins=bins,
).add_to(m)

choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'],labels=True, aliases=['kommuner: '])
)

markers.add_child(mc)

folium.LayerControl(collapsed=True).add_to(m)

# To make a new basic html map with the highlighted municipalities
m.save('output/map_2.html')
