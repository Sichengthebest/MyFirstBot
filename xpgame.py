import random
import os
import logging
import asd
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

def rewards(update,context):
    rewards = ["COOL! +90XP!", "Good! +40XP!", "Sad... Nothing happens.", "Let BOTGOD decide your fate!"]
    randomReward = random.choice(rewards)
    if randomReward == rewards[3] :
        context.bot.send_message(chat_id=update.effective_chat.id, text="%s\nDear %s, BOTGOD has rewarded you with %s XP, keep up the good work!!!"%(
            randomReward,
            update.message.from_user.first_name,
            random.randint(50,150)))
    else :
        context.bot.send_message(chat_id=update.effective_chat.id, text=randomReward)
def start(update, context):
    msg = "I'm a bot, please talk to me!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
def echo(update, context):
    msg = "%s, yOu sAId %s, YOur uid iS %s, I hAte You." %(
        update.message.from_user.first_name,
        update.message.text,
        update.message.from_user.id,)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

updater = Updater(token='1293770094:AAFlINaaTdxuGCGT7_jeKQgVzpkoevFE3vk', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
goodHandler = CommandHandler('gainxp', rewards)
asd.addHandler(dispatcher)

updater.start_polling()