import base64
import logging
import threading

import ollama


def run(state):


    task_thread_id = threading.get_ident()
    logging.info(f"Starting parser 1 task on file {state['file_path']}, Thread ID: {task_thread_id}")

    try:
        response = perform_ocr(state['file_path'])
        state["ocr_result"]  = response.message.content
        return state
    except Exception as e:
        logging.error(f"Error in handle_action: {e}")

def encode_image_to_base64(image_path):
    """Convert an image file to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def perform_ocr(image_path):
    base64_image = encode_image_to_base64(image_path)
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': """Analyze the text in the provided image. Extract all readable content
                                           and present it in a structured Markdown format that is clear, concise, 
                                           and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                           code blocks) as necessary to represent the content effectively.""",
            'images': [base64_image]
        }]
    )

    return response

