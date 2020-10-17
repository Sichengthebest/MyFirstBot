from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import random

button1 = InlineKeyboardButton("9 and more", callback_data='morethannine')
button2 = InlineKeyboardButton("6 or 8", callback_data='sixoreight')
button3 = InlineKeyboardButton("7", callback_data='seven')
button5 = InlineKeyboardButton("8", callback_data='eight')
button4 = InlineKeyboardButton("5 and less", callback_data='lessthanfive')
butoon6 = InlineKeyboardButton("Surrender", callback_data='flee')
button6 = InlineKeyboardButton("Start game", callback_data='ok')

keyb = InlineKeyboardMarkup([[button4,button2,button3,button1],[butoon6, button6]])

randomNum1 = random.randint(1,6)
randomNum2 = random.randint(1,6)
sum = randomNum1 + randomNum2
guessedNum = 0
thing = 0
msg = "I rolled two dice. Please choose one button, then press Start Game to confirm your choice.\n- Press Surrender to give up (and lose 10GP).\n- If you get the right answer, you win 1000GP.\n- If you get the wrong answer, you lose 50GP."

def bet(update, context):
    global msg
    update.message.reply_text("%s"%msg, reply_markup = keyb)

def betCallback(update, context):
    global sum
    global randomNum1
    global randomNum2
    global thing
    query = update.callback_query
    if query.data == 'lessthanfive' and sum < 6:
        thing += 1
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'lessthanfive' and sum > 5:
        thing += 2
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'sixoreight' and sum == 6:
        thing += 1
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'sixoreight' and sum == 8:
        thing += 1
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'sixoreight' and not sum == 6 and not sum == 8:
        thing += 2
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'seven' and sum == 7:
        thing += 1
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'seven' and not sum == 7:
        thing += 2
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'eight' and sum == 8:
        thing += 1
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'morethannine' and sum < 9:
        thing += 2
        query.answer("You chose %s"%query.data, show_alert=True)
    elif query.data == 'flee':
        query.answer("You coundn't afford to lose, that's why you gave 10GP to the casino staff to run away.", show_alert=True)
    elif query.data == 'ok':
        if thing == 0:
            query.answer("You haven't chosen anything.", show_alert=True)
        elif thing == 1:
            query.answer("You won the bet! Gain 1000GP, lucky you!", show_alert=True)
            thing = 0
        elif thing == 2:
            query.answer("You lost the bet. Lose 50GP.", show_alert=True)
            thing = 0
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2
    else:
        query.answer("You lost the bet. Lose 150GP. Number is reset.", show_alert=True)
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2


def addHandler(dispatcher):
    betHandler = CommandHandler('bet', bet)
    dispatcher.add_handler(betHandler)
    dispatcher.add_handler(CallbackQueryHandler(betCallback))