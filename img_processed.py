from PIL import Image
import pytesseract
import os

# Configurar PATH para tesseract
URL_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = URL_TESSERACT


def extract_text_from_image(image_path):
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image)

    lines = extracted_text.split('\n')

    processed_lines = [line.strip().lower() for line in lines]

    return processed_lines


image_dir = "img/"

all_extracted_text = []

for img in os.listdir(image_dir):
    if img.endswith(".png"):
        img_path = os.path.join(image_dir, img)

        extracted_text = extract_text_from_image(img_path)

        all_extracted_text.extend(extracted_text)
