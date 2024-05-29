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
| Aspect        | TF-IDF                                  | BM25                                       | Word2Vec                                       | BERT                                               |
|---------------|-----------------------------------------|--------------------------------------------|------------------------------------------------|----------------------------------------------------|
| Description   | Statistical measure for word importance | Probabilistic ranking model                | Neural network-based word vectors              | Transformer-based contextual embeddings            |
| Advantages    | Simple, fast                            | Better relevance ranking, handles long queries | Captures semantic relationships, flexible     | Contextual understanding, state-of-the-art         |
| Disadvantages | No context, fixed vocabulary            | Requires parameter tuning, more complex    | Context independence, training time            | Computationally intensive, complex to implement     |
| Use Cases     | Basic information retrieval             | Search engines, complex queries            | Word similarity, clustering, classification    | Advanced NLP tasks, fine-tuning for specific tasks  |

| Retrieval Method        | Description                                                                                          | Accuracy                                  | Efficiency                               | Scalability                          | Implementation Complexity           | Cost                                  |
|-------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
| Boolean Retrieval       | Uses Boolean logic (AND, OR, NOT) to match keywords in the query with documents.                     | Low                                      | High                                     | High                                 | Low                                  | Low                                   |
| TF-IDF                  | Weights terms based on their frequency in a document and their rarity across the entire document set. | Moderate                                 | High                                     | High                                 | Low                                  | Low                                   |
| BM25                    | Probabilistic model that ranks documents based on the query term frequency, document length, and term saturation. | High                                      | High                                     | High                                 | Low                                  | Low                                   |
| LSA                     | Uses singular value decomposition (SVD) to reduce dimensionality of term-document matrix.             | Moderate                                 | Moderate                                 | Moderate                             | Moderate                             | Moderate                              |
| Word2Vec/FastText       | Embedding models that represent words in a continuous vector space, capturing semantic similarities. | High                                      | Moderate                                 | Moderate                             | Moderate                             | Moderate                              |
| BERT-Based Retrieval    | Uses BERT to create dense embeddings for queries and documents, measuring similarity via cosine similarity. | High                                      | Low                                      | Moderate                             | High                                 | High                                  |
| BM25 + Embeddings       | Combines BM25 scores with embedding-based similarity scores.                                         | High                                      | Moderate                                 | High                                 | Moderate                             | Moderate                              |
| Learning-to-Rank (LTR)  | Trains a model to rank documents based on various features, including relevance scores and user feedback. | Very High                                 | Moderate                                 | Moderate                             | High                                 | High                                  |
| Neural Ranking Models   | Utilizes deep neural networks to learn relevance from query-document pairs.                          | Very High                                 | Low                                      | Moderate                             | Very High                            | Very High                             |
| ElasticSearch + Vectors | Uses ElasticSearch to store and search dense vector embeddings.                                      | High                                      | High                                     | High                                 | Moderate                             | Moderate                              |
| FAISS                   | Library for efficient similarity search and clustering of dense vectors.                             | High                                      | Very High                                | High                                 | High                                 | Moderate                              |
| Knowledge Graphs        | Utilizes relationships between entities in a graph to retrieve and rank documents.                   | High                                      | Moderate                                 | Moderate                             | High                                 | High                                  |

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