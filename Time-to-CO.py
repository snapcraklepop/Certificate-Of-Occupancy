import pandas as pd
import numpy as np
import seaborn as sns
import geopandas
import geoplot
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


co_df = pd.read_csv('DOB_NOW__Certificate_of_Occupancy_20240709.csv')

co_df_final = co_df[co_df['C OF O FILING TYPE'] == "Final"]

co_df_final[['SUBMITTED DATE', 'C OF O ISSUANCE DATE']]

co_df_final['diff_days'] = (pd.to_datetime(co_df_final['C OF O ISSUANCE DATE']) - pd.to_datetime(co_df_final['SUBMITTED DATE'])) / np.timedelta64(1, 'D')

sns.histplot(data=co_df_final, x="diff_days")

###############################################

crs={'init':'epsg:4326'}

geopandas.read_file(geoplot.datasets.get_path('nyc_boroughs'))