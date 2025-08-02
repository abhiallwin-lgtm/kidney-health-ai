# utils/extract_data.py
import fitz  # PyMuPDF
import easyocr
import re
import tempfile
import numpy as np

# --- Extract from PDF ---
def extract_from_pdf(uploaded_pdf):
    text = ""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_pdf.read())
        tmp_file_path = tmp_file.name

    doc = fitz.open(tmp_file_path)
    for page in doc:
        text += page.get_text()
    doc.close()

    return parse_lab_values(text)

# --- Extract from Image ---
def extract_from_image(uploaded_image):
    reader = easyocr.Reader(['en'])
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_img:
        tmp_img.write(uploaded_image.read())
        tmp_img_path = tmp_img.name

    result = reader.readtext(tmp_img_path, detail=0)
    full_text = " ".join(result)
    return parse_lab_values(full_text)

# --- Common Parsing Function ---
def parse_lab_values(text):
    lab_values = {}

    patterns = {
        'blood_urea': r"urea[\s:]*([\d.]+)",
        'creatinine': r"creatinine[\s:]*([\d.]+)",
        'hemoglobin': r"hemoglobin[\s:]*([\d.]+)",
        'sodium': r"sodium[\s:]*([\d.]+)",
        'potassium': r"potassium[\s:]*([\d.]+)",
    }

    text = text.lower()
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            lab_values[key] = float(match.group(1))
        else:
            lab_values[key] = np.nan

    return lab_values
