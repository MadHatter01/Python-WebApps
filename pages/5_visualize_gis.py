import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_folium import folium_static

st.title("GIS Data Visulization")

file_upload = st.file_uploader("Choose a GeoJSON file", type="geojson")

if file_upload is not None:
    df = gpd.read_file(file_upload)

    st.subheader("Preview of Data")
    st.write(df.head())