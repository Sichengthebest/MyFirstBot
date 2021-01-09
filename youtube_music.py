from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def yt():
  pass

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('ytmusic', yt))
