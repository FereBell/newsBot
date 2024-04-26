import os
import logging
import sqlite3
from telegram import Update
from datetime import datetime
from scripts.initFunc import initObjects
from scripts.resumeFunc import resumeInfo
from scripts.llmOpenIA import resumeBetter
from scripts.helpFunctions import randomNumber
from scripts.similarityText import similarityText
from scripts.saveTxt import createFolder, createTxt
from datetime import time, timezone, timedelta, datetime
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    JobQueue
    )

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER
    )
''')
conn.commit()
logger = logging.getLogger(__name__)
logging.basicConfig(filename= f"logging/{datetime.now().strftime('%Y-%m-%d')}.log",
                        filemode= "w",
                        format='%(asctime)s - [%(levelname)s] -> %(message)s', level=logging.INFO)
newsCount = 0
newsHour = 0
listShuffle = []
listLinks = []
logginVal = False

# Registro de los nuemros nuevos
async def newsRegistration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chatId = update.effective_message.chat_id
        regChat = checkNumber(chatId)
        if regChat:
            cursor.execute('INSERT INTO usuarios (chat_id) VALUES (?)', (chatId,))
            conn.commit()
            await update.effective_message.reply_text("Todo listo para mantenerte informado !!! \n recibiras información diaria sobre IA")
        else:
            await update.effective_message.reply_text("Ya estabas registrado :)")
        logger.info(f"NUMERO REGISTRADO - {chatId}")
    except Exception as e:
        logger.error(f"REGISTRANDO NUMERO - {e}")

#Revisa si el numero ya esta en la base de datos
def checkNumber(chatId):
    try:
        cursor.execute('SELECT * FROM usuarios WHERE chat_id = ?', (chatId,))
        result = cursor.fetchone()
        return False if result else True
    except Exception as e:
        logger.error(f"REVISANDO NUMERO - {e}")

async def deleteRegistration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chatId = update.effective_message.chat_id
        regChat = checkNumber(chatId)
        if regChat:
            await update.effective_message.reply_text("Aun no estas registrado")
        else:
            cursor.execute(f'DELETE FROM usuarios WHERE chat_id = {chatId}')
            conn.commit()
            await update.effective_message.reply_text("Adios, esperamos regreses pronto")
    except Exception as e:
        logger.error(f"ERROR DELETING THE CHAT ID - {e}")

#Revisa diario las nuevas notas a una hora determinada y las guarda como txt
async def dailyFunction(context: CallbackContext):
    global listShuffle; global  newsHour; global listLinks
    actDate = datetime.now()
    dir = f"newsSave/{actDate.strftime('%Y-%m-%d')}_{newsHour}"
    logger.info(f"CREATING FOLDER {dir}")
    createFolder(dir)
    listPages = initObjects()
    resum, links, name = resumeInfo(listPages, logger)
    #listCheck = os.listdir(dir)
    #logger.info(f"List of old news {len(listCheck)}")
    for r, l, n in zip(resum, links, name):
        resume = 'False'
        #resume = resumeBetter(r, logger)
        if resume == 'False': resume = r
        #if len(listCheck) > 0:
        #for oldText in listCheck:
        #with open(f"{dir}/{oldText}", 'r') as file:
        #    oldResume = file.read()
        if l in listLinks:
            logger.info(f"LINK IN THE listLinks")
        else:
            listLinks.append(l)
            createTxt(n, dir, f"{resume}\n--- {l} ---", logger)
            logger.info(f"THE FOLLOWING LINK {l} WAS STORED")
    listShuffle = randomNumber(len(os.listdir(dir)))
    context.job_queue.run_once(callback = sendNew, when = 20)  

#Se manda llamar a horas diferentes del dia para mandar las notas a los numero en las
#bases de datos
async def sendNew(context: CallbackContext):
    global newsCount; global listShuffle; global  newsHour
    actDate = datetime.now()
    dir = f"newsSave/{actDate.strftime('%Y-%m-%d')}_{newsHour}"
    listNews = os.listdir(dir)
    cursor.execute('SELECT * FROM usuarios')
    chatid = cursor.fetchall()
    if len(listNews) > 0:
        rutaArchivo = os.path.join(dir, listNews[listShuffle[newsCount]])
        logger.info(f"Sending the new {rutaArchivo}")
        newsCount += 1
        with open(rutaArchivo, 'r') as file:
            resume = file.read()
        for fila in chatid:
            message = f'-- New --: {resume}'
            await context.bot.send_message(fila[1], text= message)
    if len(listNews) > newsCount:
        context.job_queue.run_once(callback = sendNew, when = 10)
    else:
        logger.info(f"ALL THE NEWS OF THE ITEM {newsHour} WERE SENDED")
        newsHour += 1; listShuffle = []; newsCount = 0
        context.job_queue.run_once(callback = dailyFunction, when = 10)


async def stringMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    startString = "No puedo procesar tu solicitud, manda /help para mas información"
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    startString = "News bot te ayudara a mantenerte informado sobre que esta\
pasando en el mundo de la Inteligencia Artificial.\n\
/help        - Mostrar este mensaje.\n\
/registro  - Recibir las noticias diarias.\n\
/adios :(   - Dejar de recibir noticias."
    await context.bot.send_message(chat_id= update.effective_chat.id, text= startString)

if __name__ == "__main__":
    with open("TelegramKey.txt", 'r') as file:
        key = file.readline()
        logger.info("READING TELEGRAM KEY")
    application = ApplicationBuilder().token(key).build()
    application.job_queue.run_daily(callback= dailyFunction,
                                    time= time(hour=22, minute=3, second=0, tzinfo=timezone(timedelta(hours=-6))),
                                    days= (0,1,2,3,4,5,6))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('start', help))
    application.add_handler(CommandHandler('registro', newsRegistration))
    application.add_handler(CommandHandler('adios', deleteRegistration))
    application.add_handler(MessageHandler(filters.TEXT, stringMessage))
    application.run_polling(allowed_updates=Update.ALL_TYPES)