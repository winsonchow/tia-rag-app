import spacy
from bs4 import BeautifulSoup
import re

# Load the spaCy model for English
nlp = spacy.load('en_core_web_sm')

# Define entity types to ignore
ignore_entities = {'DATE', 'TIME'}

# Classify the query as specific or general
def classify_query(query):
    doc = nlp(query)

    # Check if any entities are present that are not in the ignore list
    if any(ent.label_ not in ignore_entities for ent in doc.ents):
        return "specific query"
    else:
        return "general query"
    
# Preprocess the query to extract keywords
def preprocess_query(query):
    doc = nlp(query)
    keywords = []
    
    for token in doc:
        if not token.is_stop and not token.is_punct:
            # Add named entities and nouns to keywords list
            if token.ent_type_ or token.pos_ in ['NOUN', 'PROPN', 'ADJ']:
                keywords.append(token.lemma_)
    
    return keywords

# Function to clean up the article content
def preprocess_article(article):
    # Remove HTML tags
    article = BeautifulSoup(article, 'html.parser').get_text()

    # Remove URLs
    article = re.sub(r'http\S+', '', article)

    # Handle special characters
    article = re.sub(r'&amp;', '&', article)

    # Normalise whitespace
    article = re.sub(r'\s+', ' ', article)

    # Remove source and citation tags
    article = re.sub(r'\[.*?\]+', '', article)

    return article

def fetch_and_preprocess_articles(query_type, search_results):
    # Initialize an empty list to hold the articles
    articles = []

    if query_type == "specific query":
        # Display the search results
        if search_results and 'posts' in search_results and 'hits' in search_results['posts']:
            search_posts = search_results['posts']['hits']

            # Append each article's title and content to the articles list
            articles = [post['title'] + post['content'] for post in search_posts[:30]]

            # Apply preprocessing to each article
            cleaned_articles = [preprocess_article(article) for article in articles]
        else:
            cleaned_articles = ['No relevant posts found.']
    else:
         # Display the search results
        if search_results and 'posts' in search_results:
            search_posts = search_results['posts']

            # Append each article's title and content to the articles list
            articles = [post['title'] + post['content'] for post in search_posts[:30]]

            # Apply preprocessing to each article
            cleaned_articles = [preprocess_article(article) for article in articles]
        else:
            cleaned_articles = ['No relevant posts found.']


    return cleaned_articles