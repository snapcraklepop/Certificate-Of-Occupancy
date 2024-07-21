import geopandas
import plotly.express as px
import seaborn as sns
from Time_to_CO import *
#import geoplot
import pandas as pd
#from shapely.geometry import Point, Polygon
#import matplotlib.pyplot as plt

#path_to_data = get_path("nybb")
#nyc_internet = gpd.read_file(path_to_data)

df = clean_data()

#what is the range across all of NYC?
sns.histplot(data=df, x="diff_days")

#averages across specific neighborhoods
neighborhoods = df.groupby(['ntaName'])['diff_days'].mean().sort_values()


#conversion form lat/long
crs={'init':'epsg:4326'}
geo_df=geopandas.GeoDataFrame(df,crs=crs,geometry=geopandas.points_from_xy(df["longitude"], df["latitude"]))

#vis settings
color_scale = [(0, 'FC6955'), (1,'AF0038')]
fig = px.scatter_mapbox(df,
                        lat="latitude",
                        lon="longitude",
                        hover_name="STREET NAME",
                        hover_data=["HOUSE NO"],
                        color="diff_days",
                        #color_continuous_scale=color_scale,
                        color_continuous_scale=px.colors.sequential.Viridis_r,
                        size="diff_days",
                        zoom=8,
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


###write out
neighborhoods.to_csv("Neighborhood Breakdown.csv")