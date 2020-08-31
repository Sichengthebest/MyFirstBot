import random
diceArr = ["Vacuum floor","Go to supermarket","Cook","Wash dishes","Take out garbage","Rest"]
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
def dice(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(diceArr))
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! yOu SaID " + update.message.text)

updater = Updater(token='1187785181:AAGLGNddzyqx4wY8bSRhByMAZtWlQZPBKhY', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dice_handler = CommandHandler('householdice', dice)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()