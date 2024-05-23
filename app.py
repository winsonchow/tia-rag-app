import gradio as gr
import requests
import json
from bs4 import BeautifulSoup

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    return soup.get_text()

def get_posts(page=1):
    url = f"https://www.techinasia.com/wp-json/techinasia/2.0/posts?page={page}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        try:
            data = response.json()  # Parse JSON response
            for post in data.get('posts', []):
                post['content'] = clean_html(post.get('content', ''))
            return data
        except json.JSONDecodeError:
            print(f"Invalid JSON response: {response.text}")  # Log the raw response
            return {"error": "Invalid JSON response"}
    except requests.RequestException as e:
        return {"error": str(e)}

def search_posts(keyword):
    url = f"https://www.techinasia.com/wp-json/techinasia/2.0/articles?query={keyword}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        try:
            data = response.json()  # Parse JSON response
            for post in data.get('posts', []):
                post['content'] = clean_html(post.get('content', ''))
            return data
        except json.JSONDecodeError:
            print(f"Invalid JSON response: {response.text}")  # Log the raw response
            return {"error": "Invalid JSON response"}
    except requests.RequestException as e:
        return {"error": str(e)}

def display_posts(page):
    posts = get_posts(page)
    if "error" in posts:
        return posts["error"]
    return posts

def display_search(keyword):
    results = search_posts(keyword)
    if "error" in results:
        return results["error"]
    return results

iface_posts = gr.Interface(fn=display_posts, inputs="number", outputs="json", 
                           title="List of Posts", description="Retrieve posts by page number.")

iface_search = gr.Interface(fn=display_search, inputs="text", outputs="json",
                            title="Search Posts", description="Search posts by keyword.")

gr.TabbedInterface([iface_posts, iface_search], ["List Posts", "Search Posts"]).launch()