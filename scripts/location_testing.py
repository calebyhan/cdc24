import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import *

if __name__ == "__main__":
    tube_df = pd.read_csv('../data/london_metro_stations.csv')
    tube_info = tube_df[["Station", "Latitude", "Longitude"]]

    bus_df = pd.read_csv("../data/london_bus_stops.csv")
    bus_info = bus_df[["Stop_Name", "Location_Easting", "Location_Northing"]]
    converted_bus_info = convert_coordinates(bus_df)

    df = bus_info
    converted_df = convert_coordinates(df)
    print(converted_df.iloc[1])
    # print(tube_info.iloc[9])
