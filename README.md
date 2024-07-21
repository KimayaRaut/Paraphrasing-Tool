# Paraphrasing Tool

## Overview

This project is a web application designed to assist users with text paraphrasing, spell-checking, and grammar correction. It features a Flask backend with an HTML, CSS, and JavaScript frontend. The tool aims to improve content clarity and accuracy by allowing users to input text for various corrections.

## Features

- **Text Input:** Users can input text for paraphrasing, spell-checking, and grammar correction.
- **Content Improvement:** Enhances text clarity and accuracy.
- **Spell-Checking and Grammar Correction:** Utilizes `Speller` and `language_tool_python` libraries for text improvements.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Spell-Checking and Grammar Correction:** `Speller`, `language_tool_python`
- **Python Libraries:** Flask, Speller, language_tool_python

## Installation

### Step 1: Clone the Repository

```plaintext 
git clone url
```

### Step 2: Create a Virtual Environment
Using virtualenv


```plaintext 
pip install virtualenv
```


```plaintext 
virtualenv venv
```

### Step 3: Activate the Virtual Environment
On Windows:


```plaintext 
venv\Scripts\
```


On MacOS/Linux:


```plaintext
source venv/bin/activate
```

### Step 4: Install the Required Packages
```plaintext 
pip install -r requirements.txt
```
### Step 5: Start the Flask Server
```plaintext 
python app.py
```
### Usage
Ensure the Flask server is running.

Open your web browser and navigate to http://127.0.0.1:5000.

Input text into the provided field to receive paraphrasing, spell-checking, and grammar correction.

### File Structure
```plaintext
paraphrasing-tool/
├── app.py                     # Flask application
├── model/
│   └── model.py               # Script for text processing
├── static/
│   ├── css/
│   │   └── styles.css         # CSS file for styling
│   └── script/
│       └── script.js          # JavaScript file for frontend functionality
├── templates/
│   └── index.html             # HTML file for the frontend
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation
```

# Output:
![screencapture-127-0-0-1-8000-2024-05-04-00_55_32](https://github.com/KimayaRaut/Paraphrasing-Tool/assets/66699500/51dd03c5-7ca9-4832-955c-1444b10f154d)
