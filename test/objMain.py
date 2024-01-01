import os
import json
from PyPDF2 import PdfReader

class phdProyect:
    def __init__(self, selectType):
        self.selectType = selectType
        with open('id.json', 'r') as file:
            data = json.load(file)
        if ('chatgpt_4' or 'chatgpt_35') == selectType:
            os.environ["OPENAI_API_KEY"] = data[selectType]
            print('Using chatgpt')
        elif ('llama_7' or 'llama_13' or 'llama_70') == selectType:
            print("Not available now")
        else:
            print('Not a valid option')

    def rawText(self, dir):
        reader = PdfReader(dir)
        return ''.join([page.extract_text().strip() for page in reader.pages if page.extract_text()])