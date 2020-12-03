import random
import os
import logging
import guess
import hunt
import fish
import search
import capitals
import coins
import beg
import gif
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def start(update, context):
    msg = "I'M THE GOD OF BOTS...\n/help for commands.\nVersion: 5.9.3\n------------------------------\n我是机器人的上帝...\n/help 来看命令。\n版本：5.9.3\n------------------------------\nCreator/作者: Sichengthebest"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Here's all my bot's commands. Have fun!
这是我的机器人的所有命令。玩得开心点！
-------------------------------------------------
/start - Random command that makes the bot say \"I'm THE GOD OF BOTS...\" // 使机器人说 “我是机器人的上帝” 的随机命令。
/hunt - Gain XP by catching animals. // 以捕捉动物的方式获得XP。
/huntbal - Check the amount of beastcoins you have. // 检查您有多少兽币。
/huntshop - Buy nice useful stuff for catching more animals! // 购买帮忙捕捉动物的东西！
/fish - Gain XP by fishing. // 以钓鱼的方式获得XP。
/fishbal - Check the amount of fishcoins you have. // 检查您有多少鱼币。
/fishshop - Buy nice useful stuff for catching more fish! // 购买帮忙捕捉鱼的东西！
/search - Go fetch the GP falling from the sky!!! // 去获取从天上掉下来的GP吧！！！
/guessnum - Guess a number between 1 and 100. Try and do it with the least number of tries possible! // 猜一个0-100之间的数字。尽量减少尝试次数！
/capitals - How good are you at capitals? // 你了解所有首都吗？
/bal - Check the amount of money you have. // 检查您有多少GP。
/shop - Buy nice useful stuff! // 购买有用的东西！
/inv - [BETA] Check the items you have in your inventory. // [测试] 检查库存中的物品。
/daily - Get daily GP! // 每日打卡！
/hourly - Get hourly GP! // 每时打卡！
/beg - Go beg, peasant! // 去讨钱吧，穷人！
/convert - Convert one currency into another! // 将一种货币转换为另一种货币！
/dep - Deposit money from your wallet to your bank! // 从钱包里存钱到银行！
/banknote - Increase the amount of GP you can stuff into your bank! // 增加您可以存入银行的GP数量！
/withdraw - Withdraw money from your bank to your wallet! // 从银行提款！
Creator/作者: Sichengthebest""")
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def get_command():
    return [
        BotCommand('start','Random command that makes the bot say "I\'m THE GOD OF BOTS..." // 使机器人说 “我是机器人的上帝” 的随机命令。'),
        BotCommand('help','Know your commands! // 了解你的命令！')]

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
search.addHandler(dispatcher)
capitals.add_handler(dispatcher)
coins.add_handler(dispatcher)
beg.add_handler(dispatcher)
gif.add_handler(dispatcher)
commands = coins.get_command() + capitals.get_command() + search.get_command() + guess.get_command() + fish.get_command() + hunt.get_command() + get_command() + beg.get_command() + gif.get_command()
updater.bot.set_my_commands(commands)

updater.start_polling()