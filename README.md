# RAG-app

## Overview
This project is a Retrieval-Augmented Generation (RAG) system for answering questions based on articles from Tech in Asia.

## Features
- Fetches the latest posts from Tech in Asia.
- Extract specific keywords from users' queries.
- Preprocesses and ranks articles based on user queries.
- Generates responses using OpenAI's GPT-4o model.
- Provides a user-friendly interface using Gradio.

## Choice of LLM
| Aspect              | OpenAI GPT-4                          | Anthropic Claude                     | Google Gemini                     | Meta LLaMA                        | Mistral                             |
|---------------------|---------------------------------------|--------------------------------------|-----------------------------------|-----------------------------------|-------------------------------------|
| Model Type          | Private/Closed                        | Private/Closed                       | Private/Closed                    | Open Source                       | Open Source                         |
| Parameters          | Up to 175B                            | Unknown (Large Scale)                | Unknown (Large Scale)             | 7B to 65B                         | Customizable (Various Sizes)        |
| API Access          | Requires API Key                      | Requires API Key                     | Free access up to 50 requests/day | No official API, self-hosting required | No official API, self-hosting required |
| Deployment Cost     | High (due to API usage fees)          | High (due to API usage fees)         | Moderate (limited free usage)     | Low to Moderate (depends on hosting) | Low to Moderate (depends on hosting) |
| Hosting             | Cloud-based (OpenAI servers)          | Cloud-based (Anthropic servers)      | Cloud-based (Google servers)      | Self-hosting required             | Self-hosting required               |
| Fine-Tuning         | Supported (via API)                   | Supported (via API)                  | Limited/Not clear                 | Fully supported                   | Fully supported                     |
| Performance         | State-of-the-art                      | High                                 | High                              | Competitive (varies with size)    | Competitive (varies with size)      |
| Community Support   | Strong (large user base)              | Growing                              | Growing                           | Strong (active research community) | Moderate (niche community)          |
| Ease of Use         | High (well-documented)                | High (well-documented)               | Moderate (documentation available) | Moderate (requires setup)         | Moderate (requires setup)           |
| Scalability         | High (handles large-scale queries)    | High                                 | High                              | High                              | High                                |

## Choice of Preprocessing
| Criteria                   | Boolean Retrieval                                                                 | TF-IDF                                                                                  | BM25                                                                                   | Word2Vec                                                                            | BERT-Based Retrieval                                                               |
|----------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Description**            | Uses Boolean logic (AND, OR, NOT) to match keywords in the query with documents.  | Weights terms based on their frequency in a document and their rarity across documents. | Probabilistic model that ranks documents based on query term frequency and document length. | Embedding model representing words in a continuous vector space.                  | Uses BERT to create dense embeddings for queries and documents, measuring similarity. |
| **Accuracy**               | Low: Exact matches only, no semantic understanding.                               | Medium: Considers term frequency but lacks semantic understanding.                      | High: Balances term frequency and document length for better relevance.                 | Medium-High: Captures semantic similarities but depends on pre-trained vectors.    | Very High: Captures deep contextual relationships, significantly improving relevance.  |
| **Efficiency**             | High: Simple and fast to execute.                                                 | High: Computationally efficient for small to medium datasets.                           | Medium-High: More computationally intensive than Boolean and TF-IDF.                    | Medium: Efficient for small to medium datasets, but embedding creation can be costly. | Medium-Low: Computationally expensive, especially for large datasets.              |
| **Scalability**            | High: Easily scales with dataset size.                                            | High: Scales well with dataset size.                                                    | Medium-High: Scales reasonably well but requires more resources.                       | Medium: Requires storage and handling of large vectors, which can be resource-intensive. | Medium-Low: Requires substantial computational resources for large-scale deployment. |
| **Implementation Complexity** | Low: Easy to implement and maintain.                                            | Low-Medium: Simple to implement, but may require tuning.                                | Medium: More complex than Boolean and TF-IDF, requires tuning parameters.                | Medium-High: Requires understanding of embedding models and vector math.           | High: Complex to implement, requiring deep learning expertise and resource management. |
| **Cost**                   | Low: Minimal computational and financial cost.                                    | Low: Cost-effective for most applications.                                              | Medium: Requires more computational resources, impacting cost.                           | Medium-High: Initial training and embedding creation can be costly.                | High: High computational costs, especially for inference and large-scale deployment.  |

BM25 strikes a balance between performance, relevance, and practicality. It offers improved relevance ranking over TF-IDF and is less resource-intensive compared to advanced models like BERT. For a RAG system where the goal is to provide accurate and contextually relevant answers based on the latest posts, BM25 is an optimal choice.

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