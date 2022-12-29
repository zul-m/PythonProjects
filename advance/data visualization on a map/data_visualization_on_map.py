# Import the necessary Python libraries.
import numpy as np
import pandas as pd
import folium as fo

data = pd.read_csv("Volcano.csv")
print(data.head())

# Add the latitude and longitude data of the volcanoes.
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])

volcano = fo.FeatureGroup(name = "Volcano")
for a, b, c in zip(lat, lon, name):
    volcano.add_child(fo.Marker(location = [a, b], popup = c, icon = fo.Icon(color = 'blue')))

fo.Map().add_child(volcano)