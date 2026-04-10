import pdfplumber
import re
import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_bytes

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file):
    text = ""

    try:
        # First try normal text extraction (fast)
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # If no text found → use OCR
        if len(text.strip()) < 50:
            file.seek(0)  # reset file pointer

            images = convert_from_bytes(
                file.read(),
                poppler_path=r"C:\poppler\poppler-24.08.0\Library\bin"
            )

            for img in images:
                img = np.array(img)

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

                ocr_text = pytesseract.image_to_string(thresh)

                if ocr_text:
                    text += ocr_text

    except Exception as e:
        print("Error:", e)
        return ""

    return text.strip()


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text