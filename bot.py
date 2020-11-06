import random
import os
import logging
import guess
import hunt
import fish
import rewards
import punishs
import search
import capitals
import groupguess
from telegram.ext import CommandHandler, Updater

def start(update, context):
    msg = "I'M THE GOD OF BOTS...\n/help for commands.\nVersion: 5.4.19n------------------------------\n我是机器人的上帝...\n/help 来看命令。\n版本：5.4.19\n------------------------------\nCreator/作者: Sichengthebest"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""/start - Random command that makes the bot say \"I'm THE GOD OF BOTS...\" // 使机器人说 “我是机器人的上帝” 的随机命令。
/hunt - Gain XP by catching animals. // 以捕捉动物的方式获得XP。
/search - Go fetch the GP falling from the sky!!! // 去获取从天上掉下来的GP吧！！！
/fish - Gain XP by fishing. // 以钓鱼的方式获得XP。
/guessnum - Guess a number between 1 and 100. Try and do it with the least number of tries possible! // 猜一个0-100之间的数字。尽量减少尝试次数！
/groupguess - I rolled 3 dice, then I made a game to guess the number in groups! // 我掷了3个骰子，并做了一个游戏来以群体猜此数字！
/capitals - A general knowledge game! How good are you at capitals? // 一个常识的游戏！你了解所有首都吗？
Creator/作者: Sichengthebest""")
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text
TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
guess.addHandler(dispatcher)
hunt.addHandler(dispatcher)
fish.addHandler(dispatcher)
rewards.addHandler(dispatcher)
punishs.addHandler(dispatcher)
search.addHandler(dispatcher)
capitals.add_handler(dispatcher)
groupguess.add_handler(dispatcher)

updater.start_polling()