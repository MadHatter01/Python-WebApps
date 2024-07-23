import streamlit as st
import prettymaps
import matplotlib.pyplot as plt
import io

def plot_map(location):
    fig, ax = plt.subplots(figsize=(20, 16))
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0) 
    ax.axis('off')

    prettymaps.plot(location, ax=ax, circle=True )
    plt.close(fig)
    return fig

st.title('Simple PrettyMaps Visualization')

location = st.text_input('Enter location (e.g., "San Diego"), press enter', 'San Diego')

if location:
    fig = plot_map(location)
    st.pyplot(fig)
