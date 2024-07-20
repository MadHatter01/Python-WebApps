import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

file_path = 'data/alt_fuel_stations (Jul 19 2024).csv'

data = pd.read_csv(file_path)
st.write("Column Names:", data.columns)
data = data[data['Fuel Type Code']== "ELEC"]

geomap = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

for idx, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"{row['Station Name']}<br>{row['Street Address']}<br>{row['City']}, {row['State']} {row['ZIP']}",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(geomap)

folium_static(geomap)