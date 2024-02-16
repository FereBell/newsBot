import re
from datetime import datetime
from scripts.objWeb import webPage

def verificar_formato(fecha):
    patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(patron.match(fecha))   

def initObjects(dateIn = datetime.now().strftime("%Y-%m-%d")):
    dateIn = '2024-02-15'
    mitPage = webPage("https://news.mit.edu",
                    dateIn,
                    ["https://news.mit.edu/topic/artificial-intelligence2",
                    "https://news.mit.edu/topic/computers",
                    "https://news.mit.edu/topic/computer-vision"], 
                    "2024",
                    True)
    guardPage = webPage("https://www.theguardian.com/",
                        dateIn,
                        ["https://www.theguardian.com/technology/artificialintelligenceai"],
                        "2024")
    bbcPage = webPage("https://www.bbc.com",
                    dateIn,
                    ["https://www.bbc.com/mundo/topics/cwr9j26ddr5t?page=1"],
                    "articles")
    wiredPage = webPage("https://www.wired.com",
                        dateIn,
                        ["https://www.wired.com/tag/artificial-intelligence/"],
                        "story",
                        True)
    naturePage = webPage("https://www.nature.com/",
                        dateIn,
                        ["https://www.nature.com/"],
                        "articles",
                        True)
    techcrunch = webPage("https://techcrunch.com/",
                         dateIn,
                         ["https://techcrunch.com/"],
                         "2024")
    theNextWeb = webPage("https://thenextweb.com",
                         dateIn,
                         ["https://thenextweb.com"],
                         "news",
                         True)

    mitPage.obtainAllLinks()
    guardPage.obtainAllLinks()
    bbcPage.obtainAllLinks()
    wiredPage.obtainAllLinks()
    naturePage.obtainAllLinks()
    techcrunch.obtainAllLinks()
    theNextWeb.obtainAllLinks()
    listPages = (mitPage, guardPage, bbcPage, wiredPage, naturePage, techcrunch, theNextWeb)
    
    return listPages