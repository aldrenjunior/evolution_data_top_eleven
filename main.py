from PIL import Image
import pytesseract
import re

# Configurar PATH para tesseract
URL_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = URL_TESSERACT

image = Image.open("img/124441.png")

# Extrair texto usando Tesseract OCR da imagem sem processamento
extracted_text = pytesseract.image_to_string(image)

# Exibir o texto extraído
# print(extracted_text)

# Separar o texto por linhas
lines = extracted_text.strip().split('\n')

# Preprocessamento das linhas
processed_output = []

for line in lines:
    line = line.strip().lower()
    processed_output.append(line)

print(processed_output)

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

for line in processed_output:

    if not line:
        continue

    for skill, pattern in patterns.items():
        match = re.search(pattern, line)
        if match:
            info_player[skill] = match.group(1)

print("Dicionário de Habilidades:")
print(info_player)
