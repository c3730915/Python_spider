import pytesseract
from PIL import Image
image = Image.open("test.png")
print(pytesseract.image_to_string(image))