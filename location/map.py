import folium as folium
import pandas as pd
from urllib.request import urlopen
import json
from probedict import kommun_dict
probes={}
for x in kommun_dict:
    probes[x]=len(kommun_dict[x])

probe_data = pd.DataFrame.from_dict(probes, orient='index', columns=['antal'])

with urlopen('http://kodapan.se/geodata/data/2015-06-26/kommuner-kustlinjer.geo.json') as response:
    kommuner = json.load(response)

for x in kommuner['features']:
    for k in probe_data.index:
        if k in x['properties']['name']:
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

folium.LayerControl(collapsed=True).add_to(m)

# To make a new basic html map with the highlighted municipalities
#m.save('output/map_2.html')
