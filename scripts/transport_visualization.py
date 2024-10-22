import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import contextily as ctx
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import convert_coordinates

TYPE_TRANSPORT = "metro"

tube_df = pd.read_csv('../data/london_metro_stations.csv')
tube_info = tube_df[["Station", "Latitude", "Longitude"]]

bus_df = pd.read_csv("../data/london_bus_stops.csv")
bus_info = bus_df[["Stop_Name", "Location_Easting", "Location_Northing"]]
converted_bus_info = convert_coordinates(bus_df)

plt.figure(figsize=(20, 20))
if TYPE_TRANSPORT == "metro":
    ax = sns.scatterplot(x="Longitude", y="Latitude", data=tube_info)
else:
    ax = sns.scatterplot(x="Longitude", y="Latitude", data=converted_bus_info)

ctx.add_basemap(ax, crs="EPSG:4326", zoom=12)

plt.show()
