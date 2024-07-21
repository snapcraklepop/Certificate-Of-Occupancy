import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from geodatasets import get_path
from Time_to_CO import *
import plotly.express as px

#kings_county_map = gpd.read_file('kc_tract_10.shp')
#kings_county_map.plot()

path_to_data = get_path("nybb")
nyc = gpd.read_file(path_to_data)

nyc = pd.read_csv("nybb_20240720.csv")

path_boroughs = get_path("nyc_boroughs")

boroughs = geopandas.read_file(geoplot.datasets.get_path("nyc_boroughs"))

#gdf["area"] = gdf.area

#gdf.plot("area", legend=True)

df = clean_data()


geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

gdf['geometry'].str.contains

gdf[~gdf["lat"].str.contains("POINT EMPTY")]



#this is a simple map that goes with geopandas
# deprecated: world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#world = gpd.read_file(geodatasets.data.naturalearth.land['url'])


gdf.plot(ax=nyc.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

# Create scatter map
fig = px.scatter_geo(df, lat='latitude', lon='longitude', color='diff_days',
                     hover_name='STREET NAME', #size='mag',
                     title='Earthquakes Around the World')
fig.show()



geo_df = gpd.GeoDataFrame(df, #specify our data
                          crs=crs, #specify our coordinate reference system
                          geometry=geometry) #specify the geometry list we created
geo_df.head()

len(geometry)
len(df)

fig, ax = plt.subplots(figsize=(15,15))
nyc.plot(ax=ax, alpha=0.4, color='grey')
geo_df[geo_df['diff_days'] < 40].plot(ax=ax,
                                       markersize=20,
                                       color='blue',
                                       marker='o',
                                       label='Neg')

geo_df[geo_df['diff_days'] >= 40].plot(ax=ax,
                                       markersize=20,
                                       color='red',
                                       marker='^',
                                       label='Pos')
plt.legend(prop={'size':15})