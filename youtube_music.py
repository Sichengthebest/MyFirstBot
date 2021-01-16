import pafy
import os
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def yt(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        if not 'www.youtube.com' in url:
            update.message.reply_text("Incorrect arguments! The url must come from Youtube!")
            return
        video = pafy.new(url)
        bestaudio = video.getbestaudio(preftype="m4a")
        filepath = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
        bestaudio.download(filepath=filepath)
        update.message.reply_audio(open(filepath, 'rb'))
        os.remove(filepath)
    else:
        update.message.reply_text("Incorrect arguments! Correct format: /getytm {youtube url}")

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('getytm', yt))