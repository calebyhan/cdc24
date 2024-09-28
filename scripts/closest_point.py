from scipy.spatial import KDTree
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import *

metro_stops_df = pd.read_csv("../data/london_metro_stations.csv")
metro_coordinates = metro_stops_df[["Latitude", "Longitude"]].values

with open("../data/london_restaurants.txt", "r") as f:
    data = json.load(f)
    restaurants = [[data[i][2], data[i][3]] for i in range(len(data))]

kdtree = KDTree(metro_coordinates)

distance_meters = []
for restaurant in restaurants:
    distance, index = kdtree.query(restaurant)
    distance_meters.append(haversine_distance(restaurant, metro_coordinates[index]))

with open("../data/restaurant_distances.txt", "w") as f:
    f.write(str(distance_meters))
