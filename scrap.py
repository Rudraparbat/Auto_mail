import requests
from bs4 import BeautifulSoup

def scrape_page_text(url):
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text from the page
        page_text = soup.get_text(separator='\n', strip=True)

        return page_text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
