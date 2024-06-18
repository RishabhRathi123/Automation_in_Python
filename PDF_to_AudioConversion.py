# shell script
pip install PyPDF2 gtts

import PyPDF2
from gtts import gTTS
import os

def pdf_to_audio(pdf_path, audio_path, language='en'):
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)
    text = ""

    # Extract text from each page
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # If no text could be extracted, raise an exception
    if not text.strip():
        raise ValueError("No text could be extracted from the PDF.")

    # Use gTTS to convert text to speech
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(audio_path)

    print(f"Audio file saved as {audio_path}")

# Example usage
pdf_path = 'example.pdf'  # Replace with your PDF file path
audio_path = 'output.mp3'  # Desired audio file path

try:
    pdf_to_audio(pdf_path, audio_path)
except Exception as e:
    print(f"An error occurred: {e}")
