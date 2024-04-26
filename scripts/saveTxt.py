import os

def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def createTxt(name, folder, content, logger):
    try:
        with open(f'{folder}/{name}.txt', "w") as file:
            file.write(content)
        logger.info(f"SAVING THE NOTE {name}")
    except Exception as e:
        logger.error(f"GUARDANDO NOTICIAS TXT - {e}")

if __name__ == "__main__":
    createFolder("prueba")