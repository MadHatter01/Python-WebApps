import streamlit as st
import pandas as pd
import plotly.express as px

file_upload = st.file_uploader("Choose a CSV file with lat and lon", type="csv")

if file_upload is not None:
    data = pd.read_csv(file_upload)
  

    data['MONTH'].fillna(1, inplace=True)
    data['DAY'].fillna(1, inplace=True)

    data['YEAR'] = data['YEAR'].astype(int)
    data['MONTH'] = data['MONTH'].astype(int)
    data['DAY'] = data['DAY'].astype(int)
    data['datetime'] = pd.to_datetime(data[['YEAR', 'MONTH', 'DAY']].astype(str).agg('-'.join, axis=1), errors='coerce')
    data = data.dropna(subset=['datetime'])
    data = data.dropna(subset=['MAGNITUDE'])
    data['year'] = data['datetime'].dt.year
    data['MAGNITUDE'] = pd.to_numeric(data['MAGNITUDE'], errors='coerce').fillna(0)

    min_year = int(data['year'].min())
    max_year = int(data['year'].max())

    year = st.slider("Select a year range", min_year, max_year, (min_year, max_year))

    filtered_data = data[(data['year'] >= year[0]) & (data['year'] <= year[1])]

    fig = px.scatter_mapbox(
        filtered_data, 
        lat='LATITUDE', 
        lon='LONGITUDE', 
        size='MAGNITUDE', 
        color='MAGNITUDE',
        hover_name='CITY',
        hover_data={'LATITUDE': False, 'LONGITUDE': False, 'datetime': True, 'MAGNITUDE': True, 'EQ_DEPTH': True},
        animation_frame='year', 
        zoom=1, 
        height=600,
         color_continuous_scale='OrRd',
        title=f"Global Earthquakes from {year[0]} to {year[1]}"
    )
    
    fig.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox_zoom=1,
        mapbox_center={"lat": 0, "lon": 0},
        margin={"r":0,"t":0,"l":0,"b":0})
    
    st.plotly_chart(fig)