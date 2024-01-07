
from scripts.initFunc import menu
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

#from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

def main():
    resume = menu()
    

if __name__ == "__main__":
    main()