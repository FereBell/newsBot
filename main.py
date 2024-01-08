
from colorama import Fore
from telegram import Update
from scripts.initFunc import menu
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
    )

async def stringMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #mensaje = update.message.text
    resume, links = menu()
    message = f'URL: {links[0]} \n \
        --New--: {resume[0]}'
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text= message)
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    startString = "News bot te ayudara a mantenerte informado sobre que esta\
pasando en el mundo de la Inteligencia Artificial.\n\
/help        - Mostrar este mensaje.\n\
/noticias  - Recibir las noticias diarias.\n\
/adios :(   - Dejar de recibir noticias."
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    startString = f'Hola {user.first_name}! Soy tu bot de noticias personal.\n\
utiliza el mensaje /help si necesitas ayuda'
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)

def main():
    resume = menu()
    print(Fore.BLUE + f"El numero de notici as son: {len(resume)}")
    for i in resume:
        print(Fore.YELLOW + 'Fuente:')
        print(Fore.CYAN + f'{i}')
        print('----------')
    

if __name__ == "__main__":
    application = ApplicationBuilder().token('KEY').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(MessageHandler(filters.TEXT, stringMessage))
    application.run_polling()
