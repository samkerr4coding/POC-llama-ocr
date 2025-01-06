# app.py
# -*- coding: utf-8 -*-

import logging
import os

import streamlit as st
from PIL import Image

from graph.graph import invoke_graph, create_graph
from utils.st_callable_util import get_streamlit_cb

# Configure logging
logging.basicConfig(level=logging.INFO)

SYSTEM_PROMPT = """Please provide the text in the image without adding any comment or summary."""

# Page configuration
st.set_page_config(
    page_title="Llama OCR",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description in main area
st.title("My OCR assistant (🦙Llama 3.2 vision, ollama and langgraph")

# Add clear button to top right
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear 🗑️"):
        if 'ocr_result' in st.session_state:
            del st.session_state['ocr_result']
        st.rerun()

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Llama 3.2 Vision!</p>',
            unsafe_allow_html=True)
st.markdown("---")

# Create the graph once, outside the button click handler


# Move upload controls to sidebar
with st.sidebar:
    st.header("Upload your Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display the uploaded image
        os.makedirs("temp", exist_ok=True)

        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
            image_path = f.name

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Extract Text 🔍", type="primary"):
            # No need to recreate the graph here
            with st.spinner("Processing image..."):
                try:
                    if 'graph' not in st.session_state:
                        st.session_state.graph = create_graph()
                    st_callback = get_streamlit_cb(st.empty())
                    logging.info("Invoking graph...")
                    response = invoke_graph({"file_path": image_path}, [st_callback])
                    logging.info(f"Graph response: {response}") # Log the response
                    st.session_state['ocr_result'] = response['ocr_result']
                except Exception as e:
                    logging.error(f"Error processing image: {e}")
                    st.error(f"Error processing image: {str(e)}")

# Main content area for results
if 'ocr_result' in st.session_state:
    st.markdown(st.session_state['ocr_result'])
else:
    st.info("Upload your image and click 'Extract Text' to see the results here.")

# Footer
st.markdown("---")
st.markdown(
    "POC made with Llama 3.2 Vision, Ollama, Langgraph and streamlit | [Report an Issue]( https://github.axa.com/samir-kerroumi/Llava-ocr-chatapp/issues)")
