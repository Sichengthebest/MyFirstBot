import random
import pokeconfig
import pokemon_new
import pokelist
import pokeutils
import pokemons
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, InputMediaPhoto
from datetime import datetime,timedelta

def battle(update,context):
    user = update.effective_user
    _uid = str(user.id)
    update.message.reply_text('🚧 The battle command is still in development. Don\'t forget to follow the updates on https://t.me/pokebotupdates! 🚧')

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('battle', battle))