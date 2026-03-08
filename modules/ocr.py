import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image


def extract_text(file):

    text = ""

    # If file is a PDF
    if file.type == "application/pdf":

        # Try extracting selectable text first
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        # If no text found → use OCR
        if text.strip() == "":
            file.seek(0)
            images = convert_from_bytes(file.read())

            for img in images:
                img = img.convert("L")  # convert to grayscale
                text += pytesseract.image_to_string(img, config="--psm 6")

    # If file is an image
    else:
        image = Image.open(file)
        image = image.convert("L")  # grayscale for better OCR
        text = pytesseract.image_to_string(image, config="--psm 6")

    return text
