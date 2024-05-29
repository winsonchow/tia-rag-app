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
| Aspect              | OpenAI GPT-4                          | Anthropic Claude                     | Google Gemini                     | Meta LLaMA                        |
|---------------------|---------------------------------------|--------------------------------------|-----------------------------------|-----------------------------------|
| Model Type          | Private/Closed                        | Private/Closed                       | Private/Closed                    | Open Source                       |
| Parameters          | Up to 175B                            | Unknown                              | Unknown                           | 7B to 65B                         |
| API Access          | Requires API Key                      | Requires API Key                     | Free access up to 50 requests/day | No official API, self-hosting required |
| Deployment Cost     | High (due to API usage fees)          | High (due to API usage fees)         | Moderate (limited free usage)     | Low to Moderate (depends on hosting) |
| Hosting             | Cloud-based (OpenAI servers)          | Cloud-based (Anthropic servers)      | Cloud-based (Google servers)      | Self-hosting required             |
| Performance         | High                                  | High                                 | High                              | Competitive (varies with size)    |
| Ethical and Compliance Considerations| High (Actively managed for biases and misuse) | High (Focus on ethical AI and reducing biases) | High (Actively managed and compliant with regulations) | Moderate (Community-driven, requires additional bias management) |
| Ease of Use         | High (well-documented)                | High (well-documented)               | High (well-documented)            | Moderate (requires setup)         |
| Scalability         | High                                  | High                                 | High                              | High                              |

Both GPT-4o and Claude are good choices due to their high accuracy and performance on NLP tasks. They are also well documented with comprehensive API and SDK support which makes integration easy. However, high computational resource and subscription costs could be its significant drawbacks. If the budget and infrastructure can accommodate these factors, both models should be considered. Additionally, if ethical considerations and natural speech expression are top priorities, Claude may be slightly more advantagous in this aspect.

Gemini offers a balanced solution with high performance, especially in a wide range of NLP tasks. It provides a good balance between accuracy and resource usage, making it a cost-effective option compared to GPT-4 and Claude. If a company is alreaady using Google Cloud services on existing workflows, Gemini is a practical and efficient choice.

LLaMA, being open-source, presents a cost-effective alternative with high performance on various NLP benchmarks. It requires more custom integration and significant computational resources, which might be a challenge. If we have the technical expertise and infrastructure to manage it, LLaMA can be a highly effective and budget-friendly option, providing strong performance without the high subscription costs of proprietary models.

For this project, I opted for GPT-4o due to its ease of integration and my familiarity with it. In retrospective, in a organisational setting, there are more factors to take into consideration as highlighted on the choice of LLM.

## Choice of Preprocessing
| Criteria                   | Boolean Retrieval                                                                 | TF-IDF                                                                                  | BM25                                                                                   | Word2Vec                                                                            | BERT-Based Retrieval                                                               |
|----------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Description**            | Uses Boolean logic (AND, OR, NOT) to match keywords in the query with documents.  | Weights terms based on their frequency in a document and their rarity across documents. | Probabilistic model that ranks documents based on query term frequency and document length. | Embedding model representing words in a continuous vector space.                  | Uses BERT to create dense embeddings for queries and documents, measuring similarity. |
| **Accuracy**               | Low: Exact matches only, no semantic understanding.                               | Medium: Considers term frequency but lacks semantic understanding.                      | High: Balances term frequency and document length for better relevance.                 | Medium-High: Captures semantic similarities but depends on pre-trained vectors.    | Very High: Captures deep contextual relationships, significantly improving relevance.  |
| **Efficiency**             | High: Simple and fast to execute.                                                 | High: Computationally efficient for small to medium datasets.                           | Medium-High: More computationally intensive than Boolean and TF-IDF.                    | Medium: Efficient for small to medium datasets, but embedding creation can be costly. | Medium-Low: Computationally expensive, especially for large datasets.              |
| **Scalability**            | High: Easily scales with dataset size.                                            | High: Scales well with dataset size.                                                    | Medium-High: Scales reasonably well but requires more resources.                       | Medium: Requires storage and handling of large vectors, which can be resource-intensive. | Medium-Low: Requires substantial computational resources for large-scale deployment. |
| **Cost**                   | Low: Minimal computational and financial cost.                                    | Low: Cost-effective for most applications.                                              | Medium: Requires more computational resources, impacting cost.                           | Medium-High: Initial training and embedding creation can be costly.                | High: High computational costs, especially for inference and large-scale deployment.  |

BM25 strikes a balance between performance, relevance, and practicality. It offers improved relevance ranking over TF-IDF and is less resource-intensive compared to advanced models like BERT. For a RAG system where the goal is to provide accurate and contextually relevant answers based on the latest posts, BM25 is an optimal choice.

## Prerequisities
- Python 3.9 or higher
- OpenAI API key

## Installation
1. Clone the repository
    - `git clone https://github.com/winsonchow/RAG-app.git`

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