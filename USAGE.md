# VisionChat Usage Guide :rocket:

Welcome to VisionChat! This guide will help you set up and run the VisionChat script on your system. Follow the steps below to start extracting questions from images and getting answers using OpenAI's GPT model.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Script](#running-the-script)

## Prerequisites
Before you start, make sure you have the following:
- Python installed on your system.
- An OpenAI API Key. You can get it by signing up at [OpenAI](https://beta.openai.com/signup/).
- Tesseract OCR executable. You can download it from [here](https://github.com/tesseract-ocr/tessdoc).
## Installation
Before running VisionChat, you need to install the necessary dependencies. In the project's root directory, you'll find a script named `requirements.sh` that will do this for you.

Open your terminal, navigate to the project directory, and run the following command to make the script executable and install the dependencies:
```sh
chmod +x requirements.sh
sudo ./requirements.sh
```

## Environment Variables
This project utilizes environment variables to securely handle sensitive information such as API keys. Specifically, OPENAI_API_KEY is used to store the API key required to interact with OpenAI's services.

**Linux/MacOS:**
`export OPENAI_API_KEY="your_api_key"`

**Windows:**
`set OPENAI_API_KEY="your_api_key"`

**PowerShell:**
`$env:OPENAI_API_KEY="your_api_key"`

## Running the Script
In order to run the VisionChat Python script make sure you have your path to the tesseract.exe file along with the picture of the questions that you would like to have answered in the same directory. Then when running the script make sure you insert the variables when they are asked to be provided. The python script is:
```sh
sudo python3 visionchat.py
```
