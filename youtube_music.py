import pafy
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def yt(update,context):
    if len(context.args) == 1:
        url = context.args[0]
        video = pafy.new(url)
        update.message.reply_text(f"{video}")
    else:
        update.message.reply_text("请告诉我URL啊，不然我去给你变啊？！")

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('ytmusic', yt))
    
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=C7Tl7Zn-KRE"
    video = pafy.new(url)
    bestaudio = video.getbestaudio(preftype="m4a")
    filepath = f"/tmp/{bestaudio.title}.{bestaudio.extension}"
    bestaudio.download(filepath=filepath)
