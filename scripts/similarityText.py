import numpy as np
from sentence_transformers import SentenceTransformer

def similarityText(textOne, textTwo):
    model = SentenceTransformer("distilbert-base-nli-mean-tokens")
    encodOne = model.encode(textOne)
    encodTwo = model.encode(textTwo)
    numerator = np.dot(encodOne, encodTwo)
    denominador = np.linalg.norm(encodOne) * np.linalg.norm(encodTwo)
    similarity = round(numerator / denominador, 2)
    return False if similarity > 9 else True