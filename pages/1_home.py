import streamlit as st
import time

st.title("Product Copy Generator")
st.write("Generate catchy copy for your product!")


product_name = st.text_input("Product Name")
product_description = st.text_area("Product Description")


if st.button("Generate Copy", type="primary"):
    if product_name and product_description:
        with st.spinner("Generating magic...."):
            time.sleep(5)
            st.write("LLM will generate value")

    else:
        st.write("You need to ask me something.")