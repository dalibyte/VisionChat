# VisionChat Usage Guide :rocket:

Welcome to VisionChat! This guide will help you set up and run the VisionChat script on your system. Follow the steps below to start extracting questions from images and getting answers using OpenAI's GPT model.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up Environment Variables](#setting-up-environment-variables)
- [Setting Executable Permissions](#setting-executable-permissions)
- [Running the Script](#running-the-script)

## Prerequisites
- Ensure you have Python installed on your system.
- An OpenAI API Key is required.
- Tesseract OCR should be installed.

## Installation
Before running VisionChat, you need to install the necessary dependencies. In the project's root directory, you'll find a script named `install_dependencies.sh` that will do this for you.

Open your terminal, navigate to the project directory, and run the following command to make the script executable and install the dependencies:
```sh
chmod +x install_dependencies.sh
sudo ./install_dependencies.sh
