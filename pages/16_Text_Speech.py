import streamlit as st
from gtts import gTTS
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="Audio Generator", page_icon=":microphone:")
user_input = st.text_area("Enter text to generate speech:")

st.write(user_input)