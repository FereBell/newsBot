import spacy
from colorama import Fore
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from scripts.htmlInfo import getWebContent
from deep_translator import GoogleTranslator
from sumy.summarizers.text_rank import TextRankSummarizer

def resumeInfo(listPages, logger):
    topicRelated = ("Artificial intelligence", "Deep learning", "Gan", "Gans", "Machine learning",
                    "LLM", "AI", "Generative adversial neuronal network", "Neuronal network",
                    "Convolutional neuronal network", "OpenIA", "Large lengual model", "Computer Vision",
                    "Computer Science", "Clustering", "AI", "Meta", "Chatbot", "GPU", "Reinforcement learning",
                    "AI models", "coding", "Multi-Objective Optimization", "Algorithms")
    translator = GoogleTranslator(source='en', target='es')
    resume = []
    links = []
    names = []
    logger.info("STARTING GETTING LINKS")
    for page in listPages:
        try:
            for val, link in enumerate(page.allLinks):
                if isRelated(getWebContent(link), topicRelated):
                    outputOrg = extSum(link, 5)
                    outputEsp = translator.translate(outputOrg)
                    resume.append(outputEsp)
                    links.append(link)
                    names.append(f"{page.name}_{val}")
                    logger.info("ADDING LINK")
        except Exception as e:
            logger.error(f" ERROR AT THE RESUME- {e}")
    return resume, links, names

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