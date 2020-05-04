# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:40:18 2020

@author: akbul
"""

"""
DATA:
You can access the data set by visiting Kaggles's website': 
https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
"""

import pandas as pd
# import plotly.graph_objects as go
import plotly.express as px

# Load the data
df = pd.read_csv("covid_19_data.csv")
# Rename the Country/Region and ObservationDate columns
df = df.rename(columns={"Country/Region":"Country", "ObservationDate": "Date" })

# Find the total number of confirmed cases for each Country across Date
df_country = df.groupby(["Date", "Country"]).sum().reset_index()

# Observe that df_country is sorted by Date. No need to sort it again

#-----------------------------------
# Figure 1: Total Number of Deaths
#-----------------------------------
fig1 = px.choropleth(df_country, 
                    locations="Country",
                     locationmode = "country names",
                    color="Deaths", 
                    hover_name="Country", 
                    animation_frame="Date"
                   )

fig1.update_layout(
    title_text = 'Total Number of Deaths by Country',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

#----------------------------------------------
# Figure 2: Ratio of Deaths to Confirmed Cases 
#----------------------------------------------
# Create the ratio of total deaths to total confirmed cases
df_country["Deaths/Confirmed"]  = df_country.Deaths / df_country.Confirmed

fig2 = px.choropleth(df_country, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Deaths/Confirmed", 
                    hover_name="Country", 
                    animation_frame="Date"
                   )


fig2.update_layout(
    title_text = 'Ratios of Deaths to Confirmed Cases by Country',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

#-------------------------------------
# Figure 3: Distribution of  Deaths 
#-------------------------------------
# Create daily death distribution
dailyTotalDeaths = df_country.groupby("Date").sum().Deaths
df_country["Deaths Ratio"]  = df_country.apply(lambda row: row.Deaths / dailyTotalDeaths[row.Date] ,axis=1)

fig3 = px.choropleth(df_country, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Deaths Ratio", 
                    hover_name="Country", 
                    animation_frame="Date",
                    range_color=(0, 1),
                   )


fig3.update_layout(
    title_text = 'Distribution of Deaths Across Countries',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))

# show the results 
fig1.write_html('Deaths.html', auto_open=True)
fig2.write_html('Ratios.html', auto_open=True)
fig3.write_html('DistDeaths.html', auto_open=True)