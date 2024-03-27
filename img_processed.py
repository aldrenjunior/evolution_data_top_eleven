from PIL import Image
from typing import List, Tuple
import pytesseract


# Configurar PATH para tesseract
URL_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = URL_TESSERACT


def extract_text_from_image(image_path, box: Tuple) -> List:
    custom_config = r'--oem 3 --psm 6'

    if len(box) != 4:
        raise ValueError("A tupla 'box' deve conter exatamente 4 valores.")

    image = Image.open(image_path)
    region_skills = image.crop(box)
    extracted_text = pytesseract.image_to_string(region_skills,
                                                 config=custom_config)

    lines = extracted_text.split('\n')
    processed_lines = [line.strip().lower() for line in lines if line != '']

    return processed_lines
