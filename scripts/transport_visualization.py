import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import contextily as ctx
import json

from scripts.transportation_test import transportation_info

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import *

metro_info, bus_info = transportation_info

with open("../data/london_restaurants.txt", "r") as f:
    polarities = json.load(f)

df = pd.DataFrame(polarities, columns=["polarity", "count", "lat", "lng"])
plt.figure(figsize=(20, 20))
ax = sns.scatterplot(x="lng", y="lat", hue="", data=df, palette="coolwarm")

ctx.add_basemap(ax, crs="EPSG:4326", zoom=12)

plt.show()
