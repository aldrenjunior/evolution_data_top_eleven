from PIL import Image, ImageEnhance
from typing import List
import re
import pytesseract
import os

# Configurar PATH para tesseract
URL_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = URL_TESSERACT

#    box = (390, 260, 615, 490)


def extract_text_from_image(image_path,
                            a: int, b: int, c: int, d: int) -> List:
    custom_config = r'--oem 3 --psm 6'

    image = Image.open(image_path)
    box = (a, b, c, d)
    region_skills = image.crop(box)
    enh = ImageEnhance.Contrast(region_skills)
    enh_img = enh.enhance(3.5)

    extracted_text = pytesseract.image_to_string(enh_img, config=custom_config)

    lines = extracted_text.split('\n')
    processed_lines = [line.strip().lower() for line in lines if line != '']

    return processed_lines


image_dir = "img/"

all_extracted_text = []

for img in os.listdir(image_dir):
    if img:
        img_path = os.path.join(image_dir, img)

        extracted_defense_text = extract_text_from_image(img_path, 390, 260, 615, 490)

        all_extracted_text.extend(extracted_defense_text)

print(f'{all_extracted_text=}')

# Dicionário para armazenar os padrões de habilidades
patterns = {
    "age": r"age: (\d+)",
    "quality": r"=\s*(\d+)%",
    "tackling": r'tackling (\d+)%',
    "marking": r'marking (\d+)%',
    "positioning": r'positioning (\d+)%',
    "heading": r'heading (\d+)%',
    "bravery": r'bravery (\d+)%',
    "passing": r'passing (\d+)%',
    "dribbling": r'dribbling (\d+)%',
    "crossing": r'crossing (\d+)%',
    "shooting": r'shooting (\d+)%',
    "finishing": r'finishing (\d+)%',
    "fitness": r'fitness (\d+)%',
    "strength": r'strength (\d+)%',
    "aggression": r'aggression (\d+)%',
    "speed": r'speed (\d+)%',
    "creativity": r'creativity (\d+)%'
}

info_player = {}

for line in all_extracted_text:

    if not line:
        continue

    for skill, pattern in patterns.items():
        match = re.search(pattern, line)
        if match:
            info_player[skill] = match.group(1)

print(f'{info_player=}')
