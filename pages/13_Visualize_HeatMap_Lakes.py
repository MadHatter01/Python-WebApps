import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import json

file_upload = st.file_uploader("Choose a GeoJSON file", type="geojson")

if file_upload is not None:
    geojson_data = json.load(file_upload)


    coordinates = []
    for feature in geojson_data['features']:
        if feature['geometry']['type'] == 'Polygon':
            for polygon in feature['geometry']['coordinates']:
                for coord in polygon:
                    coordinates.append([coord[1], coord[0]])

    m = folium.Map(location=coordinates[0], zoom_start=10, tiles='CartoDB dark_matter')

    HeatMap(coordinates).add_to(m)

    st_folium(m, width = 700, height=500)