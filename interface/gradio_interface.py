import os
import gradio as gr
import openai
from data.fetch import fetch_posts, search_posts
from nlp.processing import preprocess_query, classify_query
from models.bm25 import rank_articles
from config.settings import OPENAI_API_KEY

# OpenAI API key
openai.api_key = OPENAI_API_KEY

# Generate background knowledge
def generate_background_knowledge(top_articles):
    # Combine the content of the top articles into a single string
    background_knowledge = "\n\n".join(top_articles)
    
    return background_knowledge

# Generate response using OpenAI
def generate_response(query, background_knowledge):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Answer the question based on the question asked and background knowledge provided below"},
                {"role": "user", "content": f"Question: {query}\nBackground Knowledge: {background_knowledge}\nAnswer:"}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f'Error generating response: {e}')
        return "An error occurred while generating the response."
    
# Build the Gradio interface
def rag_interface(query):
    keywords = preprocess_query(query)
    query_type = classify_query(query)

    if query_type == "specific query":
        search_results = search_posts(keywords)
    else:
        search_results = fetch_posts(page=1)

    cleaned_articles = fetch_and_preprocess_articles(query_type, search_results)
    top_5_articles = rank_articles(cleaned_articles, keywords)
    background_knowledge = generate_background_knowledge(top_5_articles)

    return generate_response(query, background_knowledge)

# Launch the Gradio interface
def launch_interface():
    iface = gr.Interface(
        fn=rag_interface,
        inputs="text",
        outputs="text",
        title='Tech in Asia RAG System',
        description='Ask a question about Tech in Asia and get an answer based on the context of the latest posts.'
    )
    iface.launch()