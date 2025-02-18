import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_titles(url):
    response = requests.get(url, verify=False)  # Bypass SSL certificate verification
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find elements that contain the titles
    # Example: titles might be inside <h2> or <div> tags
    titles = soup.find_all('div', class_='article-title-class')  # Adjust class or tag as needed

    # Get the current date
    today = datetime.today().strftime('%Y-%m-%d')

    updated_titles = []
    for title in titles:
        # Extract the publication date for each title, e.g., in a <span> or similar
        # Example: check if the article date matches today's date
        article_date = title.find('span', class_='date-class').text.strip()  # Adjust as needed
        if article_date == today:
            updated_titles.append(title.get_text(strip=True))

    return updated_titles

url = "https://www.jiqizhixin.com/users/294c393b-25f7-45b0-bec6-33e3bd344e61"
titles = extract_titles(url)

for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title}")
