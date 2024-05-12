'''
from langchain_community.llms import Ollama
'''
from openai import OpenAI

def readAPI():
    with open("OpenIA.txt", 'r') as file:
        key = file.readline()
    return key

def resumeBetter(txt, logger):
    try:
        key = readAPI()
        client = OpenAI(api_key = key)
        mensajes = [{"role": "system", "content": "Experto escritor de micro notas",}]
        mensajes.append({"role": "user", "content": "Mejora la coherencia del siguiente texto: " + txt,})
        chat = client.chat.completions.create(
            messages=mensajes,
            model="gpt-3.5-turbo",
        )
        logger.info('BETTER RESUME DONE')
        return chat.choices[0].message.content
    except Exception as e:
        logger.error(f'ERROR IN THE BETTER RESUME - {e}')
        return "False"
'''
def resumeBetterLocal(txt, logger):
    try:
        llm = Ollama(model = "llama3")
        return llm.invoke(f'Mejora la coherencia del siguiente texto, no agregues comentarios propios solo regresa el resultado y en español: {txt}')
    except Exception as e:
        logger.error(f"ERROR IN THE BETTER RESUME - {e}")
        return "False"
'''
    
if __name__ == "__main__":
    print(resumeBetter("Si claro como de que no sabes que hacer"))