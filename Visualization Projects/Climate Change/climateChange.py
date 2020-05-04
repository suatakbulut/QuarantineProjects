# -*- coding: utf-8 -*-
"""
Created on Sun May  3 04:56:24 2020

@author: akbul
"""

"""
DATA:
You can access the data set by visiting Kaggles's website': 
https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data#GlobalLandTemperaturesByCountry.csv
"""

import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
df = df.rename(columns={"AverageTemperature":"Temperature", "dt": "Date" })
df["Year"] = df.apply(lambda row: row.Date.split("-")[0] ,axis=1)

#----------------------------------------------
# Figure 1: Minimum Monthly Average Temprature
#----------------------------------------------
df_min = df.groupby(["Year", "Country"]).min().reset_index()
fig_min = px.choropleth(df_min, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Temperature", 
                    hover_name="Country", 
                    animation_frame="Year",
                    range_color=(-40, 30),
                   )

fig_min.update_layout(
    title_text = "Global Minimum Monthly Average Land Temperatures by Country",
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig_min.write_html('YearlyMin.html', auto_open=True)

#----------------------------------------------
# Figure 2: Maximum Monthly Average Temprature
#----------------------------------------------
df_max = df.groupby(["Year", "Country"]).max().reset_index()
fig_max = px.choropleth(df_max, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Temperature", 
                    hover_name="Country", 
                    animation_frame="Year",
                    range_color=(-25, 40),
                   )

fig_max.update_layout(
    title_text = "Global Maximum Monthly Average Land Temperatures by Country",
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig_max.write_html('YearlyMax.html', auto_open=True)

#----------------------------------------------
# Figure 3: Average Temprature
#----------------------------------------------
df_avg = df.groupby(["Year", "Country"]).mean().reset_index()
fig_avg = px.choropleth(df_avg, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Temperature", 
                    hover_name="Country", 
                    animation_frame="Year",
                    range_color=(-25, 35),
                   )

fig_avg.update_layout(
    title_text = "Global Yearly Average Land Temperatures by Country",
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

fig_avg.write_html('YearlyAverage.html', auto_open=True)