import config
from telegram import Update, BotCommand
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from json import dumps,loads

def info(update,context):
    u = str(update)
    u = dumps(eval(u),indent=2)
    context.bot.send_message(update.effective_user.id,text=u)

def get_command():
    return [
        BotCommand('info','Random command that makes the bot say "I\'m THE GOD OF BOTS..." // 使机器人说 “我是机器人的上帝” 的随机命令。')
    ]

def add_handler(dp):
    dp.add_handler(CommandHandler(["info"], info))