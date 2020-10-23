from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import random

def capitals(update,context):
    update.message.reply_text("""A general knowledge game! The bot will randomly generate a country and a number of answer choices, depending on your chosen difficulty level. The choices are as shown:
-------------------------------------------------------------------------
- /capitals easy : You are supposed to be cultivated enough to know these countries's capitals.
4 answer choices, with one aberrant choice.
Rewards: 10GP per correct answer, lose 50GP per wrong answer.
-------------------------------------------------------------------------
- /capitals normal : Quite easy questions for those who have at least observed correctly a map.
4 answer choices
Rewards: 25GP per correct answer, lose 20GP per wrong answer.
-------------------------------------------------------------------------
- /capitals hard : Quite hard countries, but most of which you have heard of, but probably not the capitals...
5 answer choices
Rewards: 50GP per correct answer, lose 10GP per wrong answer.
-------------------------------------------------------------------------
- /capitals extreme : Countries you have never heard of! Big cash to win, though!
6 answer choices
Rewards: 125GP per correct answer, lose 5GP per wrong answer.""")

def add_handler(dispatcher):
    guessHandler = CommandHandler('capitals', capitals)
    dispatcher.add_handler(guessHandler)