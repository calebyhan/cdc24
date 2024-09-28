import sys
import os
import seaborn as sns
import matplotlib.pyplot as plt
import contextily as ctx
from tqdm import tqdm
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import *

GET_DATA = False
GRAPH_VAR = "count"

if GET_DATA:
    places = places("London", "restaurant", "en")
    polarities = []

    for i in tqdm(range(len(places))):
        polarity_sum = 0
        reviews = review_by_place(places[i]["id"])
        for review in reviews:
            polarity_sum += review["polarity"]
        if len(reviews) > 0:
            polarities.append([polarity_sum / len(reviews), len(reviews), places[i]["lat"], places[i]["lng"]])

    with open("../data/london_restaurants.txt", "w") as f:
        f.write(str(polarities))

with open("../data/london_restaurants.txt", "r") as f:
    polarities = json.load(f)

df = pd.DataFrame(polarities, columns=["polarity", "count", "lat", "lng"])
plt.figure(figsize=(20, 20))
ax = sns.scatterplot(x="lng", y="lat", hue=GRAPH_VAR, data=df, palette="coolwarm")

ctx.add_basemap(ax, crs="EPSG:4326", zoom=12)

plt.show()
