# image_captioning.py

import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_captioning_model():
    """Load the BLIP model and processor for image captioning."""
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        return processor, model
    except Exception as e:
        st.error(f"Error loading captioning model: {e}")
        return None, None

def generate_caption(image_bytes: bytes):
    """Generate a caption for a given image."""
    processor, model = load_captioning_model()
    if not processor or not model:
        return "Captioning model not available."

    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        inputs = processor(image, return_tensors="pt")

        with torch.no_grad():
            output = model.generate(**inputs, max_length=50, num_beams=4, early_stopping=True)

        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error generating caption: {e}"