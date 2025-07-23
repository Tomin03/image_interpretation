from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import streamlit as st
import numpy as np

@st.cache_resource
def load_blip():
    procesor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return procesor, model

def generate_caption(image: Image.Image) -> str:
    procesor, model = load_blip()
    inputs = procesor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = procesor.decode(outputs[0], skip_special_tokens=True)
    return caption
