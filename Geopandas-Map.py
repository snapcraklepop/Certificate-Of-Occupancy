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
nyc_internet = gpd.read_file(path_to_data)

nyc = pd.read_csv("nybb_20240720.csv").rename(columns = {"the_geom" : "geometry"} )
nyc.columns

#path_boroughs = get_path("nyc_boroughs")

#boroughs = geopandas.read_file(geoplot.datasets.get_path("nyc_boroughs"))

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


gdf.plot(ax=nyc_internet.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

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



# creating a geometry column
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# Coordinate reference system : WGS84
crs = {'init': 'epsg:4326'}
# Creating a Geographic data frame
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
gdf.plot(marker='*', markersize=0.2)

from pyproj import Proj
def rule(row):
    p = Proj(proj='utm',zone=10,ellps='WGS84', preserve_units=False)
    x,y = p(row["longitude"], row["latitude"])
    return pd.Series({"X": x , "Y": y})


My_data = df.merge(df.apply(rule, axis=1), left_index= True, right_index= True)

geometry = [Point(xy) for xy in zip(My_data['X'], My_data['Y'])]




# Creating a Geographic data frame
gdf = gpd.GeoDataFrame(My_data, crs=crs, geometry=geometry)
gdf.plot(marker='*', markersize=0.2)


crs={'init':'epsg:4326'}

#boroughs = geopandas.read_file(geoplot.datasets.get_path('nyc_boroughs'))

geo_df=geopandas.GeoDataFrame(df,crs=crs,geometry=geopandas.points_from_xy(df["longitude"], df["latitude"]))

color_scale = [(0, 'yellow'), (1,'red')]

fig = px.scatter_mapbox(df,
                        lat="latitude",
                        lon="longitude",
                        hover_name="STREET NAME",
                        hover_data=["HOUSE NO"],
                        color="diff_days",
                        color_continuous_scale=color_scale,
                        size="diff_days",
                        zoom=8,
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()