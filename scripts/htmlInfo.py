import re
import requests
from bs4 import BeautifulSoup

"""
Args: 
    html: html content with scratch information
Returns:
    Clean text
"""
def cleanHtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", "head"]):
        script.decompose()
    text = soup.get_text()
    text = re.sub('\s+', ' ', text).strip()
    return text

def getWebContent(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        cleaned_content = cleanHtml(response.text)
        return cleaned_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None