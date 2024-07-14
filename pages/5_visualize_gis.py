import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_folium import folium_static
import pandas as pd
from folium.plugins import HeatMap
import pydeck as pdk


st.title("GIS Data Visulization")

# Sample file present in data folder, grabbed from https://github.com/johan/world.geo.json. Thank you!
file_upload = st.file_uploader("Choose a GeoJSON file", type="geojson")


# pd.set_option('display.max_columns', None)

if file_upload is not None:
    df = gpd.read_file(file_upload)
    df['lon'] = df.geometry.centroid.x
    df['lat'] = df.geometry.centroid.y

    st.subheader("Preview of Data")
    st.write(df.head())

    center = [df.geometry.centroid.y.mean(), df.geometry.centroid.x.mean()]

    geomap = folium.Map(location = center, zoom_start=10)

    st.subheader("Geo Map")
    folium.GeoJson(df).add_to(geomap)
    


    
    
    folium_static(geomap)
