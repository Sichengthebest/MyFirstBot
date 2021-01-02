from telegram.ext import Dispatcher,CommandHandler
from json import dumps

def ainfo(update,context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.animation:
            u = str(update['message']['reply_to_message']['animation'])
            u = dumps(eval(u),indent=4)
            update.message.reply_text(u)
        else:
            update.message.reply_text("You need to reply this to an animation!")
    else:
        update.message.reply_text("You need to reply!")

def pinfo(update,context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.animation:
            u = str(update['message']['reply_to_message']['photo'][0])
            u = dumps(eval(u),indent=4)
            update.message.reply_text(u)
        else:
            update.message.reply_text("You need to reply this to a photo!")
    else:
        update.message.reply_text("You need to reply!")

def add_handler(dp):
    dp.add_handler(CommandHandler("ainfo", ainfo))
    dp.add_handler(CommandHandler("pinfo", pinfo))