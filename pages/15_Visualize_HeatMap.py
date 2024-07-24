import streamlit as st
import pydeck as pdk
import pandas as pd

DATA_URL = "data/collision.csv"


def load_data():
    data = pd.read_csv(DATA_URL)
    st.write(data.head())
    return data

data = load_data()

st.title("Deck.gl with Streamlit Example")

layer = pdk.Layer(
    "HexagonLayer",
    data=data,
    get_position="[LONGITUDE, LATITUDE]",
    radius=1500,
    elevation_scale=30,
    elevation_range=[0, 3000],
    pickable=True,
    extruded=True,
)

view_state = pdk.ViewState(
    latitude=data["LATITUDE"].mean(),
    longitude=data["LONGITUDE"].mean(),
    zoom=10,
    pitch=50,
)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{position}\nElevation: {elevationValue}"},
))
