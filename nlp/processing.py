import spacy

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