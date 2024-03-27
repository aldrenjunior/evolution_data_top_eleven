from img_processed import extract_text_from_image
import pytesseract
import re
import os

# Configurar PATH para tesseract
URL_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = URL_TESSERACT

image_dir = "img/"

all_extracted_text = []

# box = (xa, ya, xb, yb)
box_defense = (390, 260, 615, 490)
box_attack = (615, 260, 840, 490)
box_physic = (840, 260, 1065, 490)

boxs = (box_defense, box_attack, box_physic)

for img in os.listdir(image_dir):
    if img:
        img_path = os.path.join(image_dir, img)

        for box in boxs:
            extracted_text = extract_text_from_image(img_path, box)
            all_extracted_text.extend(extracted_text)

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
    "dribbling": r'driboting (\d+)%' or r'dribbling (\d+)%',
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
