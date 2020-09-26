from telegram.ext import CommandHandler, dispatcher

def guess(update, context):
    update.message.reply_text("You are dumb")

def addHandler(dispatcher):
    guessHandler = CommandHandler('guess', guess)
    dispatcher.add_handler(guessHandler)