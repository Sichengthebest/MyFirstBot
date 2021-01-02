from telegram.ext import Dispatcher,CommandHandler
from json import dumps

def ainfo(update,context):
    u = str(update['message']['reply_to_message']['animation'])
    u = dumps(eval(u),indent=4)
    update.message.reply_text(u)

def pinfo(update,context):
    u = str(update['message']['reply_to_message']['photo'][0])
    u = dumps(eval(u),indent=4)
    update.message.reply_text(u)

def add_handler(dp):
    dp.add_handler(CommandHandler("ainfo", ainfo))
    dp.add_handler(CommandHandler("pinfo", pinfo))