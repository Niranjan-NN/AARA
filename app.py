import streamlit as st
import google.generativeai as genai
from PIL import Image
import numpy as np
import io

# Configure the Gemini API
genai.configure(api_key="AIzaSyCS6fOqUlZKcCt6wN9JJNAT1LfzwOSmpq0")

# Load the model once
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Image Chat with Gemini", layout="centered")
st.title("🖼️💬 Image Chat with Gemini")
st.markdown("Upload an image and enter a prompt to chat with Gemini!")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
prompt = st.text_input("Enter your prompt")

if st.button("Generate Response") and uploaded_image and prompt:
    try:
        image = Image.open(uploaded_image)
        response = model.generate_content([prompt, image])
        st.success("✅ Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
