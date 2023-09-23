#!/bin/bash

# Update package lists
apt-get update

# Install Tesseract
apt-get install -y tesseract-ocr

# Install Python libraries
pip install opencv-python-headless pytesseract nltk openai

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"
