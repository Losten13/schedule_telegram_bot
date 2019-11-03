import telebot
import parse
import time

#main variables
TOKEN = "sampletoken"
bot = telebot.TeleBot(TOKEN)
inf = []
#handlers
@bot.message_handler(commands=['custom'])
def askGroup(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,"Яка група?")
    bot.register_next_step_handler(msg, askDate)
def askDate(message):
    chat_id = message.chat.id
    inf.append(message.text)
    msg = bot.send_message(chat_id,"Який день?")
    bot.register_next_step_handler(msg, getSchedule)
def getSchedule(message):
    inf.append(message.text)
    chat_id = message.chat.id
    schedule = parse.myparse(inf[0],inf[1])
    bot.send_message(chat_id,'\n'.join(map(str, schedule)))
@bot.message_handler(commands=['today'])
def askGroup(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,"Яка група?")
    bot.register_next_step_handler(msg, getSchedule)
def getSchedule(message):
    inf.append(message.text)
    chat_id = message.chat.id
    schedule = parse.myparse(inf[0],time.strftime("%d.%m.%Y"))
    bot.send_message(chat_id,'\n'.join(map(str, schedule)))
@bot.message_handler(commands=['tomorrow'])
def askGroup(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,"Яка група?")
    bot.register_next_step_handler(msg, getSchedule)
def getSchedule(message):
    inf.append(message.text)
    chat_id = message.chat.id
    schedule = parse.myparse(inf[0],time.strftime("%d.%m.%Y",time.localtime(time.time() + 24*3600)))
    bot.send_message(chat_id,'\n'.join(map(str, schedule)))

    
bot.polling()