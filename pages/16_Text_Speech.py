import streamlit as st
from gtts import gTTS
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="Audio Generator", page_icon=":microphone:")
user_input = st.text_area("Enter text to generate speech:")

if st.button("Generate Audio"):
    if user_input:
        tts = gTTS(text=user_input, lang="en")
        tts.save("output.mp3")

        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()


        st.audio(audio_bytes, format = "audio/mp3")

    