import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# --- Cache the model to avoid reloading on every interaction ---
@st.cache_resource
def load_generation_model():
    try:
        model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        pipe = pipe.to("cpu")  # Use CPU on Hugging Face Spaces (unless you have GPU)
        return pipe
    except Exception as e:
        st.error(f"Error loading image generation model: {e}")
        return None

# --- Main function to generate an image from text ---
def generate_image(prompt: str) -> Image.Image:
    """
    Generate an image from a text prompt using Stable Diffusion.
    Handles long prompts by truncating them to avoid token overflow issues.
    """
    pipe = load_generation_model()
    if not pipe:
        return None

    try:
        # Truncate the prompt using the tokenizer to max 77 tokens
        tokenizer = pipe.tokenizer
        max_length = 77

        # Tokenize and truncate
        tokens = tokenizer(prompt, truncation=True, max_length=max_length, return_tensors="pt")
        truncated_prompt = tokenizer.decode(tokens["input_ids"][0], skip_special_tokens=True)

        # Run inference without gradient tracking
        with torch.no_grad():
            image = pipe(truncated_prompt).images[0]
        return image
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None
