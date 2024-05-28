import requests
from config.settings import LIST_POSTS_URL, SEARCH_POSTS_URL

# Function to fetch posts from API
def fetch_posts(page):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(LIST_POSTS_URL, params={'page': page}, headers=headers)

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError as e:
                print(f'Error parsing response JSON: {e}')
                return []
        else:
            print(f'Error fetching posts: HTTP {response.status_code}')
            return []
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching posts: {e}')
        return []
    
# Function to search posts from API
def search_posts(keywords):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(SEARCH_POSTS_URL, params={'query': keywords}, headers=headers)

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError as e:
                print(f'Error parsing response JSON: {e}')
                return []
        else:
            print(f'Error fetching posts: HTTP {response.status_code}')
            return []
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching posts: {e}')
        return []