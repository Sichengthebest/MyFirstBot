from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import random

randomNum1 = random.randint(1,6)
randomNum2 = random.randint(1,6)
sum = randomNum1 + randomNum2
guessedNum = 0
thing = 0
record = ""
recordCH = ""
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
    uid = update.effective_user.id
    button1 = InlineKeyboardButton("9 and more / 比九大", callback_data='bet:more than nine-%s'%uid)
    button2 = InlineKeyboardButton("6 or 8 / 六或八", callback_data='bet:six or eight-%s'%uid)
    button3 = InlineKeyboardButton("7", callback_data='bet:seven-%s'%uid)
    button4 = InlineKeyboardButton("5 and less / 比五小", callback_data='bet:less than five-%s'%uid)
    butoon6 = InlineKeyboardButton("Surrender / 逃跑", callback_data='bet:flee-%s'%uid)
    button6 = InlineKeyboardButton("Start game / 开始", callback_data='bet:ok-%s'%uid)

    keyb = InlineKeyboardMarkup([[button4,button2,button3,button1],[butoon6, button6]])
    global msg
    update.message.reply_text("%s"%msg, reply_markup = keyb)

def betCallback(update, context):
    global sum,randomNum1,randomNum2,thing,record,recordCH
    place, curruid = update.callback_query.data.split('-')
    uid = update.effective_user.id
    query = update.callback_query
    if str(uid) != curruid:
        query.answer("你是谁？你在哪儿？你想做啥？这是别人的，大笨蛋！",show_alert=True)
        return
    if place == 'bet:less than five' and sum < 6:
        thing = 1
        query.answer("You chose less than five\n您选择了比五小", show_alert=True)
        record = "less than five"
        recordCH = "比五小"
    elif place == 'bet:less than five' and sum > 5:
        thing = 2
        query.answer("You chose less than five\n您选择了比五小", show_alert=True)
        record = "less than five"
        recordCH = "比五小"
    elif place == 'bet:six or eight' and sum == 6:
        thing = 1
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
        record = "six or eight"
        recordCH = "六或八"
    elif place == 'bet:six or eight' and sum == 8:
        thing = 1
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
        record = "six or eight"
        recordCH = "六或八"
    elif place == 'bet:six or eight' and not sum == 6 and not sum == 8:
        thing = 2
        query.answer("You chose six or eight\n您选择了六或八", show_alert=True)
        record = "six or eight"
        recordCH = "六或八"
    elif place == 'bet:seven' and sum == 7:
        thing = 1
        query.answer("You chose seven\n您选择了七", show_alert=True)
        record = "seven"
        recordCH = "七"
    elif place == 'bet:seven' and not sum == 7:
        thing = 2
        query.answer("You chose seven\n您选择了七", show_alert=True)
        record = "seven"
        recordCH = "七"
    elif place == 'bet:more than nine' and sum > 8:
        thing = 1
        query.answer("You chose more than nine\n您选择了比九大", show_alert=True)
        record = "more than nine"
        recordCH = "比九大"
    elif place == 'bet:more than nine' and sum < 9:
        thing = 2
        query.answer("You chose more than nine\n您选择了比九大", show_alert=True)
        record = "more than nine"
        recordCH = "比九大"
    elif place == 'bet:flee':
        query.answer("You coundn't afford to lose, that's why you gave 10GP to the casino staff to run away.\n您输不起，这就是为什么您给赌场工作人员10GP为了逃走。", show_alert=True)
        query.edit_message_text("You coundn't afford to lose, that's why you gave 10GP to the casino staff to run away.\n您输不起，这就是为什么您给赌场工作人员10GP为了逃走。")
        thing = 0
    elif place == 'bet:ok':
        if thing == 0:
            query.answer("You haven't chosen anything\n您还没有选择任何东西")
        elif thing == 1:
            query.answer("You won the bet! Gain 1000GP\n您赢了赌注！获得1000GP")
            query.edit_message_text("You chose %s.\nYou won the bet! Gain 1000GP, lucky you! How did you know it was %s?\n你选择了%s。\n您赢了赌注！获得1000GP，幸运的你！你怎么知道数字是%s的？"%(record,sum,recordCH,sum))
            thing = 0
        elif thing == 2:
            query.answer("You lost the bet. Lose 50GP\n你输掉了50GP。")
            query.edit_message_text("You chose %s.\nYou lost the bet. Lose 50GP. Number was: %s\n你选择了%s。\n你输掉了50GP。正确数字为：%s"%(record,sum,recordCH,sum))
            thing = 0
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2
        record = ""
        recordCH = ""
    else:
        query.answer("Uh-oh, there was a bug somewhere!", show_alert=True)
        randomNum1 = random.randint(1,6)
        randomNum2 = random.randint(1,6)
        sum = randomNum1 + randomNum2
        thing = 0


def addHandler(dispatcher):
    betHandler = CommandHandler('bet', bet)
    dispatcher.add_handler(betHandler)
    dispatcher.add_handler(CallbackQueryHandler(betCallback,pattern="^bet:[A-Za-z0-9_]*"))