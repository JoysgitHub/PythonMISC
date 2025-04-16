import pyttsx3
import os
import warnings
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

warnings.filterwarnings("ignore", message="Using a slow image processor as `use_fast` is unset")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Image to text generator
def generated_caption(image_path):
    try:
        
        image = Image.open(image_path)
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs, max_length=50)  # max_length for captions
        caption = processor.decode(out[0], skip_special_tokens=True)

      

        return caption
    except Exception as e:
        return f"An error occurred: {e}"

image_path = "image1.jpg"  # Path to local image
caption = generated_caption(image_path)
full_caption = f" This is an image of {caption}"
print(f"{full_caption}")

# Text To speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed 
engine.setProperty('volume', 1)     # Volume 
engine.say(full_caption)
engine.runAndWait()
