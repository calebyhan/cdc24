import pandas as pd
from pyproj import Transformer
import math

from internals.wrapper import *

def get_reviews_of_place(place_id: str) -> list:
    """
    Get reviews of a place by place_id

    :param place_id: A string representing the place_id
    :return: A list of dictionaries containing the reviews of the place
    """
    data = review_by_place(place_id)
    review_ids = []
    ret = []

    for review in data:
        review_ids.append(review["details"].split("?id=")[1])

    for review in review_ids:
        ret.append(review_details(review))
    return ret

def convert_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert coordinates from easting and northing to latitude and longitude

    :param df: DataFrame containing the columns 'location_name', 'Location_Easting', 'Location_Northing'
    :return: DataFrame containing the columns 'location_name', 'latitude', 'longitude'
    """
    transformer = Transformer.from_crs("epsg:27700", "epsg:4326", always_xy=True)

    latitudes = []
    longitudes = []

    for index, row in df.iterrows():
        easting = row['Location_Easting']
        northing = row['Location_Northing']

        longitude, latitude = transformer.transform(easting, northing)

        latitudes.append(latitude)
        longitudes.append(longitude)

    result_df = pd.DataFrame({
        'Stop_Name': df['Stop_Name'],
        'Latitude': latitudes,
        'Longitude': longitudes
    })

    return result_df


def haversine_distance(coord1: list, coord2: list) -> float:
    r = 6371000

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = r * c
    return distance

if __name__ == "__main__":
    print(get_reviews_of_place("42177"))
