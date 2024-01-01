import requests
from typing import List
from colorama import Fore
from bs4 import BeautifulSoup
from htmldate import find_date
from dataclasses import dataclass

'''
The web page object needs some special urls
and we are using the useBase to simplify the 
searching
'''

@dataclass
class webPage:
    baseUrl: str
    date: str
    topicUrl: List[str]
    keyWord: List[str]
    useBase: bool = False

    """
    Search links in a web page
    Args:
        url (string): link of the web page
    Returns:
        List of links
    """
    def searchLinks(self, url):
        allLinks = []
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all('a')
            for link in links:
                allLinks.append(link.get("href"))
        else:
            print(Fore.RED + f"Bad status code from: {url}")
        return allLinks

    """
    Args:
        url (string): link of the web page
        currentDate: date to search the news
    Returns:
        List of input links
    """
    def searchUrl(self, url, currentDate):
        self.saveLinks = []
        tmp = []
        links = self.searchLinks(url)
        for href in links:
            if href and self.keyWord in href and href not in tmp:
                fullUrl = self.baseUrl + href if self.useBase else href
                if self.dateChecker(fullUrl) == currentDate:
                    self.saveLinks.append(fullUrl)
                tmp.append(href)

    """
    Check the date of the publication
    Args:
        url: URL of the publicationq
    Returns:
        Date of the publication
    """
    def dateChecker(self, url):
        try:
            response = requests.get(url)
            date = find_date(response.content.decode('utf-8'))
            return date
        except Exception as e:
            pass

    """
    Save all the links in a set
    Args:
        url: URL of the publicationq
    Returns:
        All the links founded
    """
    def obtainAllLinks(self):
        self.allLinks = set()
        for j in self.topicUrl:
            self.searchUrl(j, self.date)
            for i in self.saveLinks:
                self.allLinks.add(i)