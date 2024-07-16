import streamlit as st
import pandas as pd
import plotly.express as px

file_upload = st.file_uploader("Choose a CSV file with lat and lon", type="csv")
st.title("Earthquake Visualization")

if file_upload is not None:
    data = pd.read_csv(file_upload)
    st.write(data)

    fig = px.scatter_mapbox(
        data,
        lat='latitude',
        lon='longitude',
        size='mag',
        color='mag',
        zoom=1,
        height=600,
        hover_name='place',
        color_continuous_scale='OrRd',
        hover_data={'latitude':True, 'longitude':True, 'time':True},
    )
    
    fig.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox_zoom=1,
        mapbox_center={"lat": 0, "lon": 0},
        margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig)