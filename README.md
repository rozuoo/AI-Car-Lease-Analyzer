# 🚗 AI Car Lease Agreement Analyzer

An AI-powered system that helps users understand car lease or loan agreements automatically.

## Features

- 📄 OCR-based contract text extraction
- 📊 Automatic contract data extraction
- 🚗 VIN verification using NHTSA API
- ⚠ Financial risk detection
- 🧠 AI-generated contract summary
- 💬 Interactive chatbot for contract questions

## Tech Stack

- Python
- Streamlit
- Tesseract OCR
- pdfplumber
- NHTSA Vehicle API

## How It Works

1. Upload a lease/loan contract (PDF or image)
2. The system extracts text using OCR
3. Important contract fields are identified
4. VIN information is verified using vehicle API
5. Risk analysis checks financial conditions
6. AI summary explains the agreement
7. Users can ask questions via chatbot

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py