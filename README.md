# RAG-app

## Overview
This project is a Retrieval-Augmented Generation (RAG) system for answering questions based on articles from Tech in Asia.

## Features
- Fetches the latest posts from Tech in Asia.
- Extract specific keywords from users' queries.
- Preprocesses and ranks articles based on user queries.
- Generates responses using OpenAI's GPT-4 model.
- Provides a user-friendly interface using Gradio.

## Choice of LLM


## Choice of Preprocessing


## Prerequisities
- Python 3.9 or higher
- OpenAI API key

## Installation
1. Clone the repository

2. Create a virtual environment
    - `python -m venv venv`

3. Activate the virtual environment
    - On macOS / Linux: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`

4. Install the required dependencies
    - Use the `pip install -r requirements.txt` command to install dependencies.

5. Set up environment variables
    - Create a .env file in the root directory of the project and add your OpenAI API key:
`OPENAI_API_KEY=your_openai_api_key`

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
```
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
```