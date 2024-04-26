import numpy as np
import os

def randomNumber(numNews):
    totalNum = np.arange(numNews)
    np.random.shuffle(totalNum)
    return totalNum

if __name__ == "__main__":
    listShuffle = randomNumber(len(os.listdir('2024-04-19')))
    listNews = os.listdir('2024-04-19')
    print(listNews)
    print(listShuffle)
    os.path.join('2024-04-19', listNews[listShuffle[0]])