import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image


def extract_text(file):

    text = ""

    # If file is a PDF
    if file.type == "application/pdf":

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        # If PDF had no selectable text (scanned document)
        if text.strip() == "":
            images = convert_from_bytes(file.read())

            for img in images:
                text += pytesseract.image_to_string(img)

    # If file is an image
    else:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)

    return text