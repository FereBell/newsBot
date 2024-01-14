from colorama import Fore
from telegram import Update
from scripts.initFunc import initObjects
from scripts.resumeFunc import resumeInfo
from datetime import time, timezone, timedelta
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
    )
#listPages = initObjects()

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    try:
        context.job_queue.run_daily(dailyNews,
                                    time= time(hour=0, minute=22, second=0, tzinfo=timezone(timedelta(hours=-6))),
                                    days= (0,1,2,3,4,5,6), chat_id=chat_id, name=str(chat_id))
        await update.effective_message.reply_text("Todo listo para mantenerte informado !!!")     
    except Exception as e:
        print(f"Catching following: {e}")


async def dailyNews(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(context.job.chat_id, text=f"Beep! seconds are over!")
    '''
    resume, links = resumeInfo(listPages)
    for r, l in zip(resume, links):
        message = f'URL: {l} \n \
            --New--: {r}'
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text= message)
    '''

async def stringMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    startString = "No puedo procesar tu solicitud, manda /help para mas información"
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)
    
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

if __name__ == "__main__":
    with open("TelegramKey.txt", 'r') as file:
        key = file.readline()
    application = ApplicationBuilder().token(key).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('noticias', noticias))
    application.add_handler(MessageHandler(filters.TEXT, stringMessage))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    