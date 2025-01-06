# Llama OCR: Image Text Extraction with Llama 3.2 Vision, Streamlit, and LangGraph

This project demonstrates how to perform Optical Character Recognition (OCR) on images using the Llama 3.2 Vision model, integrated with a Streamlit web application and powered by LangGraph for workflow management.

## Overview

This application allows users to upload an image and extract text from it using the Llama 3.2 Vision model. The project leverages:

*   **Llama 3.2 Vision:** A powerful vision model for understanding and extracting text from images.
*   **Streamlit:** A Python framework for building interactive web applications, providing the user interface for image upload and result display.
*   **LangGraph:** A library for building complex, multi-step workflows, used here to orchestrate the image processing and text extraction.
*   **Python:** The primary programming language for the project.
*   **PIL (Pillow):** Python Imaging Library for image handling.
*   **Langchain:** Framework for developing applications powered by language models.

## Features

*   **Image Upload:** Users can upload images in `png`, `jpg`, or `jpeg` formats.
*   **Text Extraction:** The application extracts text from the uploaded image using the Llama 3.2 Vision model.
*   **Clear Results:** The extracted text is displayed in the main content area of the application.
*   **Clear Button:** A button to clear the results and upload a new image.
*   **Progress Indication:** A spinner indicates when the image is being processed.
*   **Error Handling:** Basic error handling to catch and display issues during image processing.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.12+:** You can download it from [python.org](https://www.python.org/downloads/).
*   **Poetry:** A tool for dependency management. Install it by following the instructions on [poetry.org](https://python-poetry.org/docs/#installation).
*   **Ollama:** You need to have Ollama installed and running with the Llama 3.2 Vision model available. Follow the instructions on [ollama.ai](https://ollama.ai/) to install Ollama and pull the Llama 3.2 Vision model.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.axa.com/samir-kerroumi/llava-ocr-chatapp
    cd llava-ocr-chatapp
    ```

2.  **Install dependencies using Poetry:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will create a virtual environment and install all the required packages listed in `pyproject.toml`.

3.  **Activate a python 3.12 virtual environment:**

4. Install [Ollama](https://ollama.com/download) and pull llama 3.2 vision lllm
    
   ```bash
    ollama run llama3.2-vision
    ```
   Make sure the model is running 

    ```bash
    ollama ps
    ```

### Running the Application

1.  **Start the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This will launch the application in your default web browser. (http://localhost:8501/)

2.  **Upload an image:** Use the file uploader in the sidebar to select an image.

3.  **Extract Text:** Click the "Extract Text" button to process the image and display the extracted text.

## Developer Tutorial

This section provides a guide for developers who want to modify or extend the project.

### Project Structure

*   `app.py`: The main Streamlit application file, responsible for the user interface and orchestrating the workflow.
*   `graph.py`: Defines the LangGraph workflow for image processing and text extraction.
*   `agents/`: Contains the agents used in the LangGraph workflow (e.g., `image_cleaner_agent.py`).
*   `state/`: Defines the state schema used by LangGraph (`graph_state.py`).
*   `utils/`: Contains utility functions, such as the Streamlit callback function (`st_callable_util.py`).
*   `temp/`: Temporary directory for storing uploaded images.
*   `pyproject.toml`: Lists the project's dependencies.
*   `README.md`: This file.

### Overview 

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
