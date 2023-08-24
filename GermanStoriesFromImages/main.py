# main.py

import streamlit as st
from image_processing import extract_text_from_images
from story_generation import get_story_with_gpt3

def main():
    st.title("German Story Generator from Images")
    
    # Upload the image through Streamlit
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    # Showing image
    st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)

    
    if uploaded_image is not None:
        # Extract text from the uploaded image
        extracted_text_per_image = extract_text_from_images({uploaded_image.name: uploaded_image})
        
        # Generate the story using GPT-3
        resulting_stories = get_story_with_gpt3(extracted_text_per_image)
        
        # Display the story on the Streamlit app
        for image_name, story in resulting_stories.items():
            st.write(f"Generated story for {image_name}:\n\n{story}\n\n")

# The following line ensures that when the script is run, the Streamlit app is launched
if __name__ == "__main__":
    main()
