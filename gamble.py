import random
import coins
from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta

gametimes = {}

def get_users(user):
    if not user in gametimes:
        gametimes[user] = datetime.now()

def gamble(update,context):
    user = update.effective_user
    get_users(user)
    uid = str(user.id)
    botnum = random.randint(1,6)
    yournum = random.randint(1,6)
    t = datetime.now()
    if t < gametimes[user]:
        update.message.reply_text("Slow it down, cmon!!! If I let you bet whenever you wanted, you'd be a lot poorer.\n放慢速度，呆瓜！！！如果我允许您随时下注，那么您就会破产。\nCreator/作者: Sichengthebest")
        return
    if len(context.args) == 0:
        update.message.reply_text("You have to bet something, seems like common sense.\n您必须赌一些钱，对我来说是常识。")
    elif not context.args[0].isdigit():
        update.message.reply_text("You have to bet a positive integer, seems like common sense.\n您必须赌一个正数，对我来说是常识。")
    else:
        bet = int(context.args[0])
        if bet <= 100:
            update.message.reply_text("You have to bet a positive integer larger than 100.\n您必须赌一个比一百大的正数。")
        else:
            if bet > coins.coins[uid]['coins']:
                update.message.reply_text("You only have %s coins, dont try to lie to me...\n您只有%s枚硬币，不要试图骗我。"%(coins.coins[uid]['coins'],coins.coins[uid]['coins']))
            else:
                if botnum > yournum:
                    coins.add_coins(user,-bet)
                    update.message.reply_text("""Your number: %s
My number: %s
You lost %s GP! You now have %s GP."""%(yournum,botnum,bet,coins.coins[uid]['coins']))
                elif botnum == yournum:
                    update.message.reply_text("""Your number: %s
My number: %s
You tied with your opponent! Your wallet hasn't changed! You still have %s GP."""%(yournum,botnum,coins.coins[uid]['coins']))
                else:
                    coins.add_coins(user,bet)
                    update.message.reply_text("""Your number: %s
My number: %s
You won %s GP! You now have %s GP."""%(yournum,botnum,bet,coins.coins[uid]['coins']))
    gametimes[user] = datetime.now() + timedelta(seconds=20)

def get_command():
    return [BotCommand('gamble','Roll your dice against the bot, if you get higher than the bot you\'ll win! // 与机器人投骰子，如果得到的数比机器人高，您将获胜！')]

def add_handler(dispatcher):
    dispatcher.add_handler(CommandHandler('gamble',gamble))