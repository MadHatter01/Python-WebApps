import streamlit as st
import numpy as np
import plotly.graph_objs as gobj

st.title("Interactive animated plot")

freq = st.slider("Select frequency", 1, 20, 5)

x = np.linspace(0, 2*np.pi, 500)
y_sin = np.sin(freq * x)
y_cos = np.cos(freq * x)

fig = gobj.Figure()
fig.add_trace(gobj.Scatter(x=x, y=y_sin, mode='lines', name='Sine Wave'))
fig.add_trace(gobj.Scatter(x=x, y=y_cos, mode='lines', name='Cos Wave'))

st.plotly_chart(fig)