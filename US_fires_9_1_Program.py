import json

infile = open("US_fires_9_1.json", "r")
outfile = open("US_fires_9_1.json", "w")

# the json.load() function converts the data into a
# format Python can work with: in this case a
# giant dictionary
fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

list_of_fires = fire_data['features']

brights,lons,lats = [],[],[]


for fire in list_of_fires:
    bright = fire['brightness']
    lon = fire['longitude']
    lat = fire['latitude']
    brights.append(bright)
    lons.append(lon)
    lats.append(lat)

    if list_of_fires[count] > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

    count += 1


print(brights[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo', 
    'lon': lons, 
    'lat': lats,
    'marker':{
    'size':10, 
    'color':brights,
    'colorscale':'Viridis', 
    'reversescale':True, 
    'colorbar':{'title':'Brightness'}}}]

my_layout = Layout(title="California Fires - 9/1/20 through 9/13/20")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='US_fires_9_1.html')