import requests
from bs4 import BeautifulSoup
import warnings
import re

# Suppress SSL and InsecureRequestWarning
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

def extract_news_titles(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send an HTTP request to the website with the headers
    response = requests.get(url, headers=headers, verify=False)  # Bypass SSL verification
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return []

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # **Optional**: Print the prettified HTML structure for debugging
    print(soup.prettify())  # This prints the entire HTML in a readable format

    # Find all anchor tags that contain the article titles
    titles = [] 

    # The titles are within <div class="list-title"> tags in arXiv
    for div in soup.find_all('div', class_='list-title'):
        title = div.get_text(strip=True)
        if title:
            titles.append(title)

    # Return the titles list
    return titles

# Function to filter titles by keywords using regular expressions
def filter_titles_by_keywords(titles, keywords):
    filtered_titles = []
    for title in titles:
        # Create a regular expression that matches any of the keywords as whole words (case-insensitive)
        pattern = r'\b(?:' + '|'.join([re.escape(keyword) for keyword in keywords]) + r')\b'
        if re.search(pattern, title, re.IGNORECASE):
            filtered_titles.append(title)
    
    return filtered_titles

# Example URL for arXiv (Database section)
url = 'https://arxiv.org/list/cs.DB/recent'
news_titles = extract_news_titles(url)

# Keywords to filter the titles
keywords = ['RAG', 'Cloud','Datalake', 'On-device']

# Filter the titles based on the specified keywords
filtered_titles = filter_titles_by_keywords(news_titles, keywords)

# Display the filtered titles
if filtered_titles:
    print("\nFiltered News Titles from arXiv (Database Section):")
    for idx, title in enumerate(filtered_titles, start=1):
        print(f"{idx}. {title}")
else:
    print("No titles found with the specified keywords.")

# This will pause the script until you press Enter
input("Press Enter to exit...")
