import pafy
import os
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand, InputMediaAudio, bot

def yt(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        if not 'www.youtube.com' in url:
            update.message.reply_text("Incorrect arguments! The url must come from Youtube!")
            return
        video = pafy.new(url)
        bestaudio = video.getbestaudio(preftype="m4a")
        music_size = bestaudio.get_filesize()
        if music_size > 10000000:
            update.message.reply_text("Sorry, but that video is too long, I can only download videos smaller that 10MB!")
            return
        msg = update.message.reply_photo('https://i.pcmag.com/imagery/articles/04oP7J3OIykTchX4vhU57vn-28..1569485834.jpg',caption=f"Dowloading... Please be patient. Your video is {music_size/1000} KBs long")
        filepath = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
        bestaudio.download(filepath=filepath)
        msg.edit_media(InputMediaAudio(open(filepath, 'rb')))
        os.remove(filepath)
    else:
        update.message.reply_text("Incorrect arguments! Correct format: /getytm {youtube url}")

def getCommand():
    return [BotCommand('getytm', 'Download some music from a Youtube url!')]

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('getytm', yt))