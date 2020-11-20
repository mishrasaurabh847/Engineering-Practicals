from PIL import Image
import pytesseract

im = Image.open("sample.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Saurabh R. Mishra\AppData\Local\Programs\Python\Python38\tesseract.exe'

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
