diceArr = ["Vacuum floor","Cook","Wash dishes","Rest","Go to supermarket","Take out garbage"]
huntArr = ["You have caught a duck! You gained 10XP!", "You have caught a duck! You gained 10XP!", "You have caught a deer! You gained 25XP!", "You have caught a deer! You gained 25XP!", "You have caught a deer! You gained 25XP!", "You have caught a boar! You gained 75XP!", "You didn't bring back anything!", "You didn't bring back anything!", "You didn't bring back anything!", "A bear caught you and you lost 30HP!"]
import random
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm THE GOD OF BOTS...")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! yOu SaID " + update.message.text)
def dice(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(diceArr))
def hunt(update, context):
    global hp
    hp = 50
    global ep
    ep = 30
    global xp
    xp = 0
    global coins
    coins = 0
    ep -= 25
    result = random.choice(huntArr)
    if result.index == 0 or result.index == 1:
        xp += 10
        context.bot.send_message(chat_id=update.effective_chat.id, text="%s You now have %sxp!" %(result, xp))
    elif result.index == 2 or result.index == 3 or result.index == 4:
        xp += 25
        context.bot.send_message(chat_id=update.effective_chat.id, text="%s You now have %sxp!" %(result, xp))
    elif result.index == 6:
        xp += 75
        context.bot.send_message(chat_id=update.effective_chat.id, text="%s You now have %sxp!" %(result, xp))
    elif result.index == 10:
        hp -= 30
        context.bot.send_message(chat_id=update.effective_chat.id, text="%s You now have %sxp!" %(result, xp))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=result)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text
def unknown(update,context):
     context.bot.send_message(chat_id=update.effective_chat.id, text="I dO NoT uNdeRsTanD wHaT YOu ArE aSkiNg mE...")

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
hunt_handler = CommandHandler('hunt', hunt)
dice_handler = CommandHandler('houseworkdice', dice)
dispatcher.addHandler(MessageHandler([Filters.command], unknown))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(dice_handler)
dispatcher.add_handler(hunt_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()