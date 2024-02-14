import sqlite3
from telegram import Update
from scripts.initFunc import initObjects
from scripts.resumeFunc import resumeInfo
from datetime import time, timezone, timedelta
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
    )

#listPages = initObjects()
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER
    )
''')
conn.commit()

async def newsRegistration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chatId = update.effective_message.chat_id
        regChat = checkNumber(chatId, cursor)
        if regChat:
            cursor.execute('INSERT INTO usuarios (chat_id) VALUES (?)', (chatId,))
            conn.commit()
            await update.effective_message.reply_text("Todo listo para mantenerte informado !!! \n recibiras información diaria sobre IA")
        else:
            await update.effective_message.reply_text("Ya estabas registrado :)")
    except Exception as e:
        print(f"Error en la inscripcion: {e}")

def checkNumber(chat_id, db):
    db.execute('SELECT * FROM usuarios WHERE chat_id = ?', (chat_id,))
    result = cursor.fetchone()
    if result:
        print(f'Chat ID: {chat_id} ya existente')
        return False
    else:
        print(f'Chat ID: {chat_id} registrado')
        return True

async def dailyNews(context: CallbackContext):
    cursor.execute('SELECT * FROM usuarios')
    for fila in cursor.fetchall():
        await context.bot.send_message(fila[1], text=f"Beep! seconds are over!")
    '''
    resume, links = resumeInfo(listPages)
    for r, l in zip(resume, links):
        message = f'URL: {l} \n \
            --New--: {r}'
        await context.bot.send_message(context.job.chat_id, text= message)
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


if __name__ == "__main__":
    with open("TelegramKey.txt", 'r') as file:
        key = file.readline()
    application = ApplicationBuilder().token(key).build()
    application.job_queue.run_daily(callback= dailyNews,
                                    time= time(hour=00, minute=17, second=30, tzinfo=timezone(timedelta(hours=-6))),
                                    days= (0,1,2,3,4,5,6))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('noticias', newsRegistration))
    application.add_handler(MessageHandler(filters.TEXT, stringMessage))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    