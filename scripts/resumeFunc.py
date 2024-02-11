import spacy
from colorama import Fore
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from scripts.htmlInfo import getWebContent
from deep_translator import GoogleTranslator
from sumy.summarizers.text_rank import TextRankSummarizer

def resumeInfo(listPages):
    topicRelated = ("Artificial intelligence", "Deep learning", "Gan", "Gans", "Machine learning",
                    "LLM", "AI", "Generative adversial neuronal network", "Neuronal network",
                    "Convolutional neuronal network", "OpenIA", "Large lengual model", "Computer Vision",
                    "Computer Science")
    translator = GoogleTranslator(source='en', target='es')
    resume = []
    links = []
    for page in listPages:
        try:
            print(Fore.BLUE + f'Revieweing page: {page.baseUrl}')
            for link in page.saveLinks:
                if isRelated(getWebContent(link), topicRelated):
                    print(Fore.BLUE + f"Link: {link}")
                    #outputOrg = article.summarize(getWebContent(link)[:4500])
                    outputOrg = extSum(link, 5)
                    outputEsp = translator.translate(outputOrg)
                    resume.append(outputEsp)
                    links.append(link)
        except Exception as e:
            print(Fore.RED + f"Error at: {e}")
    return resume, links

"""
Using a ML model to check the relation between the post and the
news searching
Args:
    txt (str): clean post plain text
    topic: tuple with the key words
Returns:
    a bool if the text is related 
"""
def isRelated(text, topic):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for i in topic:
        val = i.lower() in [token.text.lower() for token in doc]
        if val: return True
    return False

def extSum(link, length = 22):
    text = ""
    parser = HtmlParser.from_url(link, Tokenizer('english'))
    summarizer = TextRankSummarizer()
    for sentences in summarizer(parser.document, length):
        text = text + str(sentences) + "\n"
    return text