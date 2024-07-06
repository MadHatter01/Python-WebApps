import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title('Word Cloud Generator')
st.markdown("""
Enter your text and generate a word cloud!
""")

text_input = st.text_area('Enter your text here:', height=200)

if st.button('Generate Word Cloud'):
    if text_input.strip():
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_input)

        
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt.gcf())

    else:
        st.warning('Please enter some text to generate a word cloud.')
