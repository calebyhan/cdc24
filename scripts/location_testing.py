from scripts.transportation_test import bus_info
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from internals.tools import *

if __name__ == "__main__":
    df = bus_info

    converted_df = convert_coordinates(df)

    print(converted_df)