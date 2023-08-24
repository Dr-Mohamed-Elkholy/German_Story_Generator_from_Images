from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def get_story_with_gpt3(extracted_text_per_image):
    """
    Generate stories using GPT-3 based on the extracted text from images.

    Parameters:
    - extracted_text_per_image (dict): Dictionary containing filenames as keys and extracted text as values.

    Returns:
    - dict: A dictionary with filenames as keys and generated stories as values.
    """
    # Assuming you've set your OpenAI API key elsewhere (e.g., in main.py)
    # openai.api_key = "YOUR_API_KEY"  

    stories_per_image = {}
    for image_name, extracted_text in extracted_text_per_image.items():
        # Construct the prompt for GPT-3
        prompt_content = (
            f"Extracted text: \"{extracted_text}\"\n\n"
            f"Instructions:\n"
            f"1. Identify and extract all German words or phrases from the provided text then show them in pairs\n"
            f"2. Craft a short story in German using these German words. Ensure that the target German words are underlined and bolded.\n"
            f"3. Translate this German story into English sentence-by-sentence, ensuring corresponding English words are underlined and bolded.\n"
            f"4. VERY IMPORTANT: Format both stories into a table, side by side. Each row should have a sentence in German and its corresponding translation in English. Use emojis for added memory retention.\n"
        )
        
        # Construct the message payload for the chat model
        messages = [
            {"role": "system", "content": "You are a specialized assistant in bilingual content creation for German learners."},
            {"role": "user", "content": prompt_content}
        ]
        
        # Use the v1/chat/completions endpoint (assuming you've set up the OpenAI Python client)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        stories_per_image[image_name] = response.choices[0].message['content'].strip()
    
    return stories_per_image
