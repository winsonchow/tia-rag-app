# RAG-app

## Overview


## Features


## Choice of LLM


## Choice of Preprocessing


## Prerequisities


## Installation
1. Clone the repository

2. Create a virtual environment

3. Activate the virtual environment

4. Install the required dependencies
Use the `pip install -r requirements.txt` command to install dependencies.

5. Set up environment variables

## Usage
1. Run the application
- `python main.py`

2. Access the Gradio interface
- After running the application, you will see an output similar to this in your terminal: Running on local URL:  http://127.0.0.1:7860/
- Open the provided URL in your web browser to access the Gradio interface.

3. Interact with the application
- Enter your query in the text box and submit it.
- The system will fetch the latest posts, preprocess and rank them, generate background knowledge, and produce a response based on the context of the articles.

## Project Structure
my_project/
├── .env
├── main.py
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   ├── __init__.py
│   └── fetch.py
├── models/
│   ├── __init__.py
│   └── bm25.py
├── nlp/
│   ├── __init__.py
│   └── processing.py
├── interface/
│   ├── __init__.py
│   └── gradio_interface.py
└── utils/
    ├── __init__.py
    └── helpers.py