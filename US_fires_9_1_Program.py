import json

infile = open("US_fires_9_1.json", "r")
outfile = open("US_fires_9_1.json", "w")

# the json.load() function converts the data into a
# format Python can work with: in this case a
# giant dictionary
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data['features']

mags,lons,lats = [],[],[]


for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo', 
    'lon': lons, 
    'lat': lats,
    'marker':{
    'size':[5*mag for mag in mags], 
    'color':mags,
    'colorscale':'Viridis', 
    'reversescale':True, 
    'colorbar':{'title':'Brightness'}}}]

my_layout = Layout(title="California Fires")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='US_fires_9_1.html')