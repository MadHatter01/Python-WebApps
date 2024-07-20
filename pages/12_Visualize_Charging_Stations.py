import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import Fullscreen, MarkerCluster


file_path = 'data/alt_fuel_stations (Jul 19 2024).csv'

data = pd.read_csv(file_path)
st.write("Column Names:", data.columns)
data = data[data['Fuel Type Code']== "ELEC"]

geomap = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10,  tiles='CartoDB dark_matter')

# for idx, row in data.iterrows():
#     folium.Marker(
#         location=[row["Latitude"], row["Longitude"]],
#         popup=f"{row['Station Name']}<br>{row['Street Address']}<br>{row['City']}, {row['State']} {row['ZIP']}",
#         icon=folium.Icon(color="blue", icon="info-sign"),
#     ).add_to(geomap)
marker_cluster = MarkerCluster().add_to(geomap)


for idx, row in data.iterrows():
    popup_info = f"""
    <div style="width: 200px;">
    <b>Station Name:</b> {row['Station Name']}<br>
    <b>Address:</b> {row['Street Address']}, {row['City']}, {row['State']} {row['ZIP']}<br>
    <b>Phone:</b> {row['Station Phone']}<br>
    <b>Status:</b> {row['Status Code']}
    </div>
    """
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=10,
        color="#aec6cf",
        fill=True,
        fill_color="#aec6cf",
        fill_opacity=0.7,
        popup=popup_info
    ).add_to(marker_cluster)

Fullscreen().add_to(geomap)

folium_static(geomap)