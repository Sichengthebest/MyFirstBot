from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import random

button1 = InlineKeyboardButton("9 and more / 比九大", callback_data='morethannine')
button2 = InlineKeyboardButton("6 or 8 / 六或八", callback_data='sixoreight')
button3 = InlineKeyboardButton("7", callback_data='seven')
button4 = InlineKeyboardButton("5 and less / 比五小", callback_data='lessthanfive')
butoon6 = InlineKeyboardButton("Surrender / 逃跑", callback_data='flee')
button6 = InlineKeyboardButton("Start game / 开始", callback_data='ok')

keyb = InlineKeyboardMarkup([[button4,button2,button3,button1],[butoon6, button6]])

randomNum1 = random.randint(1,6)
randomNum2 = random.randint(1,6)
sum = randomNum1 + randomNum2
guessedNum = 0
thing = 0
msg = """I rolled two dice. Please choose one button, then press Start Game to confirm your choice.
- Press Surrender to give up and lose 10GP.
- If you get the right answer, you win 1000GP.
- If you get the wrong answer, you lose 100GP.
--------------------------------------------------------------------
我掷了两个骰子。请选择一个按钮，然后按开始来确认选择。
-按逃跑来放弃（丢失10GP）。
-如果答案正确，您将赢得1000GP。
-如果输入答案错误，您将损失50GP。
"""

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
        thing = 1
        query.answer("You chose less than five\n您选择了比五小", show_alert=True)
    elif query.data == 'lessthanfive' and sum > 5:
        thing = 2
        query.answer("You chose less than five\n您选择了比五小", show_alert=True)
    elif query.data == 'sixoreight' and sum == 6:
        thing = 1
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
    elif query.data == 'sixoreight' and sum == 8:
        thing = 1
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
    elif query.data == 'sixoreight' and not sum == 6 and not sum == 8:
        thing = 2
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
    elif query.data == 'seven' and sum == 7:
        thing = 1
        query.answer("You chose seven\n您选择了七", show_alert=True)
    elif query.data == 'seven' and not sum == 7:
        thing = 2
        query.answer("You chose seven\n您选择了七", show_alert=True)
    elif query.data == 'morethannine' and sum > 8:
        thing = 1
        query.answer("You chose more than nine\n您选择了比九大", show_alert=True)
    elif query.data == 'morethannine' and sum < 9:
        thing = 2
        query.answer("You chose more than nine\n您选择了比九大", show_alert=True)
    elif query.data == 'flee':
        query.answer("You coundn't afford to lose, that's why you gave 10GP to the casino staff to run away.\n您输不起，这就是为什么您给赌场工作人员10GP为了逃走。", show_alert=True)
        thing = 0
    elif query.data == 'ok':
        if thing == 0:
            query.answer("You haven't chosen anything.\n您还没有选择任何东西", show_alert=True)
        elif thing == 1:
            query.answer("You won the bet! Gain 1000GP, lucky you! How did you know it was %s?\n您赢了赌注！获得1000GP，幸运的你！你怎么知道数字是%s的？"%(sum,sum), show_alert=True)
            thing = 0
        elif thing == 2:
            query.answer("You lost the bet. Lose 50GP. Number was: %s\n你输掉了50GP。正确数字为：%s"%(sum,sum), show_alert=True)
            thing = 0
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2
    else:
        query.answer("You lost the bet. Lose 100GP. Number is reset.", show_alert=True)
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2
        thing = 0


def addHandler(dispatcher):
    betHandler = CommandHandler('bet', bet)
    dispatcher.add_handler(betHandler)
    dispatcher.add_handler(CallbackQueryHandler(betCallback))