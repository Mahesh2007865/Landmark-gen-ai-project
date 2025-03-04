import streamlit as st
import requests
import base64
from PIL import Image
import io

# Directly define the API key (Replace with your actual API key)
API_KEY = "AIzaSyBUlpCZakDFoukVvazvODwa8FJdqouVgy4"
API_URL = "https://your-api.com/analyze"  # Replace with actual API endpoint

st.title("Landmark AI Analyzer")
st.write("Upload an image of a landmark, and AI will describe it!")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Landmark", use_column_width=True)

    # Convert image to base64 for API
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Button to analyze image
    if st.button("Analyze Landmark"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"image": img_str}  # Sending image as base64
            )

            # Process response
            if response.status_code == 200:
                result = response.json()
                description = result.get("description", "No description available.")
                st.success("Analysis Complete!")
                st.subheader("Landmark Description:")
                st.write(description)
            else:
                st.error("Error analyzing image. Please try again.")
