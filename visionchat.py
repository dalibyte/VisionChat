"""
This project uses several libraries under various licenses:

- OpenCV (BSD License): https://opensource.org/licenses/BSD-3-Clause
- pytesseract (Apache License 2.0): https://www.apache.org/licenses/LICENSE-2.0
- NLTK (Apache License 2.0): https://www.apache.org/licenses/LICENSE-2.0
- openai (MIT License): https://opensource.org/licenses/MIT
- regex (Python Software Foundation License): https://docs.python.org/3/license.html

Please refer to the respective links for the full license texts.
"""
import cv2
import pytesseract
import re
import os
import openai
from nltk.tokenize import sent_tokenize

# Configure Tesseract path through User input
directory = input("Input the directory to the tesseract executable (e.g., /opt/homebrew/bin/tesseract): ")
pytesseract.pytesseract.tesseract_cmd = directory

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def ocr_image_to_text(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text

def extract_questions(text):
    sentences = sent_tokenize(text)
    questions = [sent for sent in sentences if re.match(r'(?i)\b(who|once|after|make|define|describe|what|when|which|write|from|where|why|how|is|are|was|were|do|does|can|re-write|name|did)\b', sent) and sent.endswith('?')]
    return questions

def get_answers_from_gpt(questions):
    answers = []
    for question in questions:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        # Extract the assistant's response from the returned data
        answer = response.choices[0].message.content
        answers.append(answer.strip())
    return answers

def process_image_and_get_answers(image_path, output_file):
    text = ocr_image_to_text(image_path)
    questions = extract_questions(text)
    answers = get_answers_from_gpt(questions)

    with open(output_file, 'w') as f:
        for q, a in zip(questions, answers):
            f.write(f"Question: {q}\nAnswer: {a}\n\n")

# User I/O
image_path = input("Enter the path to your image file: ")
output_file = input("Enter the name/path of the output file (e.g., answers.txt): ")
process_image_and_get_answers(image_path, output_file)

print(f"Answers written to {output_file}")
