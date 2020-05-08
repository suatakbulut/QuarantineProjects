# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:10:21 2020

@author: akbul
"""

"""
DATA:
You can access the data set by visiting Kaggles's website': 
https://www.kaggle.com/austinreese/craigslist-carstrucks-data
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# Load the data
df_raw = pd.read_csv("vehicles.csv")

def remOutlier(data, col):    
    quant1 = data[col].quantile(0.25)
    quant3 = data[col].quantile(0.75)
    iqr = quant3 - quant1
    filtered = data.loc[(data[col] >= quant1 - 1.5*iqr) & (data[col] <= quant1 + 1.5*iqr)]
    
    return filtered

cols = ["region", "state", "year", "manufacturer", "model", "odometer", "title_status", "transmission", "type", "condition", "description", "paint_color", "price" ]
df_all = df_raw.copy()[cols]
df_used = df_all.loc[df_all.condition != "new"]
df_used_pr = remOutlier(df_used, "price")
df_used_od = remOutlier(df_used_pr, "odometer")

cars = df_used_od.copy()



fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
subplot1 = ax1.boxplot(cars.price, 
                       patch_artist=True,
                       labels= ["Price"])
for patch in subplot1["boxes"]:
    patch.set_facecolor("lightblue")
    
subplot2 = ax2.boxplot(cars.odometer,
                       patch_artist=True,
                      labels = ["Odometer"])
for patch in subplot2["boxes"]:
    patch.set_facecolor("lightgreen")
    
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_ylabel('Observed values')
    
fig.suptitle("Boxplot of Price and Odometer Variables After Removing the Outliers")
plt.show()

import plotly.graph_objects as go


import plotly.express as px

cars_state = cars[["price", "state", "odometer"]].groupby("state").mean().reset_index()
cars_state.state = cars_state.apply(lambda row: row.state.upper(), axis=1)
fig = px.choropleth(cars_state, 
                    locations="state",
                    locationmode = "USA-states",
                    color="odometer", 
                    hover_name="state",
                    scope="usa",
                    color_continuous_scale="Viridis"
                   )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


    