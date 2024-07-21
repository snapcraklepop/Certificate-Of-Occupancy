import pandas as pd
import numpy as np
import seaborn as sns
import geopandas
import geoplot
import matplotlib.pyplot as plt
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

def clean_data():
    co_df = pd.read_csv('DOB_NOW__Certificate_of_Occupancy_20240709.csv')

    co_df_final = co_df[co_df['C OF O FILING TYPE'] == "Final"]

    co_df_final[['SUBMITTED DATE', 'C OF O ISSUANCE DATE']]

    co_df_final['job_type'] = co_df_final['JOB TYPE'].str.lower()

    co_df_final_newB = co_df_final[co_df_final['job_type'].str.contains("new building")]

    co_df_final_newB['diff_days'] = (pd.to_datetime(co_df_final_newB['C OF O ISSUANCE DATE']) - pd.to_datetime(co_df_final_newB['SUBMITTED DATE'])) / np.timedelta64(1, 'D')

    return co_df_final_newB

#sns.histplot(data=co_df_final_newB, x="diff_days")
##############################################

#co_df_final['ntaName'].drop_duplicates()


###############################################

#crs={'init':'epsg:4326'}

#geopandas.read_file(geoplot.datasets.get_path('nyc_boroughs'))