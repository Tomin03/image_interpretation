import numpy as np
import pandas as pd
import streamlit as st
import base64

# Background

# Conversion to Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


image_path = "Background.jpg"
image_base64 = get_base64_of_bin_file(image_path)

# Implementing background
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{image_base64}");
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>🖼️ Image interpretation</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🔍 Choose the picture to analyse</h2>", unsafe_allow_html=True)

image_list = [f"Image_{i}.jpg" for i in range(1, 11)]
selected_image = st.selectbox("🔽 Image", image_list)
