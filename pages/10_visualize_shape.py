import streamlit as st
import geopandas as gpd
import plotly.express as px

def load_data(upload_file):
    gdf = gpd.read_file(upload_file, driver='ESRI Shapefile')
    return gdf


st.title('GIS Data Visualization with Streamlit')
uploaded_file = st.file_uploader('Upload a Shapefile (.zip)', type='zip')

if uploaded_file is not None:
    shapefile = load_data(uploaded_file)
    if not shapefile.empty:
        st.subheader('Shapefile Head:')
        st.write(shapefile.head())
        fig = px.choropleth_mapbox(shapefile,
                                       geojson=shapefile.geometry.__geo_interface__,
                                       locations=shapefile.index,
                                       color='COUNTRY',
                                       hover_name='COUNTRY', 
                                       mapbox_style="open-street-map",
                                       zoom=3, 
                                       center={'lat': shapefile.geometry.centroid.y.mean(),
                                               'lon': shapefile.geometry.centroid.x.mean()})

        st.plotly_chart(fig)
    else:
        st.write('Uploaded Shapefile could not be read.')
