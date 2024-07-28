import streamlit as st
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt



user_input = st.text_area("Enter text for analysis")

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)


if st.button('Analyze Text'):
    if user_input:
        st.subheader("Word Cloud")
        generate_wordcloud(user_input)

    else:
        st.error("Please enter text for analysis")
        