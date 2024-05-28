import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# API endpoints
LIST_POSTS_URL = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts'
SEARCH_POSTS_URL = 'https://www.techinasia.com/wp-json/techinasia/2.0/articles?query='