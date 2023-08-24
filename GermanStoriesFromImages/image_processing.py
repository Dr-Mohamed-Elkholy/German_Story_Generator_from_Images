import pytesseract
from PIL import Image
import streamlit as st

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_images(uploaded_files):
    """
    Extract text from the uploaded images using pytesseract.
    
    Parameters:
    - uploaded_files (dict): Dictionary containing uploaded file objects.

    Returns:
    - dict: A dictionary with filenames as keys and extracted text as values.
    """
    all_extracted_text = {}
    for image_name in uploaded_files.keys():
        image = Image.open(uploaded_files[image_name])
        extracted_text = pytesseract.image_to_string(image)
        all_extracted_text[image_name] = extracted_text
    return all_extracted_text
