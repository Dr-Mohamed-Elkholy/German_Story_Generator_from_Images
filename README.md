# German Story Generator from Images 🖼️📖

## Description

This project offers a unique way to create engaging German stories based on the text extracted from uploaded images. It uses Optical Character Recognition (OCR) to extract text from images and then leverages the power of GPT-3 to craft captivating stories in both German and English, presented side by side for easy comparison and learning. This tool can be especially helpful for German language learners, providing them with contextually relevant sentences and their translations.

## Features

1. **Image Upload**: Allows users to upload images containing text in any format (jpg, png, jpeg).
2. **Text Extraction**: Uses `pytesseract`, an OCR tool, to extract text from the uploaded images.
3. **Story Generation**: Utilizes the `openai` GPT-3 model to generate short, coherent stories based on the extracted text. The stories are crafted in a bilingual format: German and its corresponding English translation.
4. **Interactive Web Interface**: Uses `streamlit` to provide an interactive web application for users, making the whole process user-friendly.

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR installed on your machine (follow the [installation guide](https://github.com/tesseract-ocr/tesseract/wiki))

### Steps

1. Clone this repository:

```bash
git clone https://github.com/Dr-Mohamed-Elkholy/German_Story_Generator_from_Images.git
```

2. Navigate to the project directory:

```bash
cd German_Story_Generator_from_Images
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

(Note: `requirements.txt` should contain all the necessary packages like `streamlit`, `pytesseract`, `openai`, `PIL`, etc.)

4. Run the Streamlit app:

```bash
streamlit run main.py
```

5. Open the provided local URL in your browser.

## Usage

1. **Upload Image**: Use the file uploader to upload an image containing German text.
2. **Generate Story**: After uploading, the application will automatically extract text and generate a story.
3. **View Result**: The generated story, along with the extracted text, will be displayed in a bilingual table format.


 
## Files Overview

- `main.py`: The main driver of the application. Contains the Streamlit interface and calls functions for image processing and story generation.
- `image_processing.py`: Contains functions for text extraction from images using `pytesseract`.
- `story_generation.py`: Contains functions for story generation using `OpenAI GPT-3`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the MIT License. See `LICENSE` for more information.

---
