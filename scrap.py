import requests
from bs4 import BeautifulSoup

def scrape_page_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text(separator='\n', strip=True)
        return page_text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

