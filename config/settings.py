import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from the environment variable
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# API endpoints
LIST_POSTS_URL = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts'
SEARCH_POSTS_URL = 'https://www.techinasia.com/wp-json/techinasia/2.0/articles?query='