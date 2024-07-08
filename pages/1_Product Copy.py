import streamlit as st
import time
from openai import OpenAI

client = OpenAI()

st.title("Product Copy Generator")
st.write("Generate catchy copy for your product!")

def generate_product_copy(prompt, max_tokens = 100):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are an experienced copywriter specializing in creating engaging product copy and taglines."},
            {"role": "user", "content": prompt}
        ],
        max_tokens = max_tokens
    )
    return response.choices[0].message.content

product_name = st.text_input("Product Name")
product_description = st.text_area("Product Description")

# col1, col2, colx = st.columns([2.5,3,7])
col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Copy", type="primary"):
        if product_name and product_description:
            with st.spinner("Generating magic...."):
                prompt = (f"Generate a catchy copy for the product. \n\n"
                f"Product Name: {product_name}\n\n"
                f"Product Description: {product_description}\n\n"
                f"Product Copy: ")
                copy = generate_product_copy(prompt)
                st.write("LLM will generate value")
                st.write(copy)

        else:
            st.write("You need to ask me something.")
with col2:
    if st.button("Generate Tagline"):
        if product_name and product_description:
            with st.spinner("Generating magic...."):
                prompt = (f"Generate a catchy tagline for the product.\n\n"
                        f"Product Name: {product_name}\n"
                        f"Product Description: {product_description}\n\n"
                        f"Tagline:")

                tagline = generate_product_copy(prompt, max_tokens = 20)
                st.write("Generating magic...")
                st.write(tagline)
        else:
            st.write("Please enter both product name and description")