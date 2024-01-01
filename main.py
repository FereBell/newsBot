
from scripts.resumeFunc import resumeInfo
from scripts.initFunc import initObjects, menu
#from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

def main():
    menu()
    """
    listPages = initObjects()
    resume = resumeInfo(listPages)
    for i in resume:
        print(i)
        print("------------")
    """

if __name__ == "__main__":
    main()