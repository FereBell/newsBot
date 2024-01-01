import re
from colorama import Fore
from scripts.objWeb import webPage
from scripts.resumeFunc import resumeInfo
from datetime import datetime

def menu():
    val =  0
    while (val < 1 or val > 5):
        print(Fore.GREEN + "--------------------------------------")
        print( "Menu de noticias")
        print("01 Noticias de la fecha actual")
        print("02 Noticias de fechas especificas")
        print("03 Detener bot")
        val = int(input("Entrada de opción: "))
        print(f"Aplicando opcion {val}") if (val > 0 and val < 6) else print(Fore.YELLOW + "Intente de nuevo")
    if val == 1:
        listPages = initObjects()
    elif val == 2:
        val01 = False
        while not val01:
            date = input("Introduce la fecha con el siguiente formato YYYY-MM-DD: ")
            val01 = verificar_formato(date)
        listPages = initObjects(date)
    return resumeInfo(listPages)

def verificar_formato(fecha):
    patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(patron.match(fecha))   

def initObjects(dateIn = datetime.now().strftime("%Y-%m-%d")):
    mitPage = webPage("https://news.mit.edu",
                    dateIn,
                    ["https://news.mit.edu/topic/artificial-intelligence2",
                    "https://news.mit.edu/topic/computers",
                    "https://news.mit.edu/topic/computer-vision"], 
                    "2023",
                    True)
    guardPage = webPage("https://www.theguardian.com/",
                        dateIn,
                        ["https://www.theguardian.com/technology/artificialintelligenceai"],
                        "2023")
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
    
    mitPage.obtainAllLinks()
    guardPage.obtainAllLinks()
    bbcPage.obtainAllLinks()
    wiredPage.obtainAllLinks()
    naturePage.obtainAllLinks()
    listPages = (mitPage, guardPage, bbcPage, wiredPage, naturePage)
    
    return listPages