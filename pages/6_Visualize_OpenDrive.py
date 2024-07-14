import streamlit as st
import folium
from streamlit_folium import folium_static
from lxml import etree
import numpy as np

st.title("Opendrive Road Network Visualization")

file_upload = st.file_uploader("Choose an OpenDrive XODR file", type="xodr")

if file_upload is not None:
    tree = etree.parse(file_upload)
    root = tree.getroot()

    roads = []
    for road in root.findall(".//road"):
        roads.append(road.get('id'))

        
    st.write(roads)