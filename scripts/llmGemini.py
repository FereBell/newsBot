import google.generativeai as genai

def readAPI():
    with open("GoogleGemini.txt", 'r') as file:
        key = file.readline()
    return key

def resumeBetter(txt):
    key = readAPI()
    genai.configure(api_key=key)
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content('Mejora la coherencia del siguiente texto para que enganche al lector: ' + txt)
        return response.text
    except Exception as e:
        print(f'Error en el resumen del LLM: {e}')
        return "False"

if __name__ == "__main__":
    resumeBetter("Mira el video")