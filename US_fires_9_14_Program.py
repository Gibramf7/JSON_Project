import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_14.json", "r")


# the json.load() function converts the data into a
# format Python can work with: in this case a
# giant dictionary

us_fires = json.load(infile)


brights,lons,lats = [],[],[]

count = 0


for fire in us_fires:
    bright = us_fires[count]['brightness']
    lon = us_fires[count]['longitude']
    lat = us_fires[count]['latitude']


    if us_fires[count]["brightness"] > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

    count += 1

    


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

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='US_fires_9_14.html')