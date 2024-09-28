"""
Created Two data frames with information from the London tube and the London bus system.
'bus_info' is a pd dataframe with Stop_Name, Latitude, and Longitude
'tube_info' is a pd dataframe with Station, Latitude, and Longitude

They are combine
"""
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import convert_coordinates


# Read the CSV file
tube_df = pd.read_csv('../data/london_metro_stations.csv')
tube_info = tube_df[["Station", "Latitude", "Longitude"]]
# Display the DataFrame
bus_df = pd.read_csv("../data/london_bus_stops.csv")
bus_info = bus_df[["Stop_Name", "Location_Easting", "Location_Northing"]]
converted_bus_info = convert_coordinates(bus_df)

#Combine most important info
transportation_info = tube_info, bus_info

if __name__ == "__main__":
    print(converted_bus_info.head(), tube_info.head())
