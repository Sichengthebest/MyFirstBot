from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def yt():
  pass

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('ytmusic', yt))
    
if __name__ == "__main__":
    pass
