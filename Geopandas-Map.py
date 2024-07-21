import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from geodatasets import get_path
from Time-to-CO import *

#kings_county_map = gpd.read_file('kc_tract_10.shp')
#kings_county_map.plot()

path_to_data = get_path("nybb")
gdf = gpd.read_file(path_to_data)

gdf["area"] = gdf.area

gdf.plot("area", legend=True)


geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)

#this is a simple map that goes with geopandas
# deprecated: world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);


