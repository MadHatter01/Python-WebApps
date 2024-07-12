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



st.title("Interactive flower curve viz")

n = st.slider("Select n (number of petals if n is odd, 2n if even)", 1, 10, 4)
d = st.slider("Select d (density of petals)", 1, 10, 6)

theta = np.linspace(0, 2 * np.pi, 1000)
r = np.cos(n * theta / d)

x = r * np.cos(theta)
y = r * np.sin(theta)

fig = gobj.Figure()

fig.add_trace(gobj.Scatter(x=x, y=y, mode='lines', name='Rose Curve'))

fig.update_layout(title="Flower Curve",
                  xaxis=dict(visible=False),
                  yaxis=dict(visible=False),
                  showlegend=False,
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  title_font_color='white')

st.plotly_chart(fig)