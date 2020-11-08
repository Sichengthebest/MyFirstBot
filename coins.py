import random
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler

# {
#   uid : {
#       'name': first_name,
#       'coins': 123,
#       'dailytime' : time
#       'hp' : 56
#       'items' : ["herring","trout","shark","boar","fox","deer","skunk","basilisk"]
#       }
# }

coins = {}

def check_user(user):
    uid = user.id
    first_name = user.first_name
    if not uid in coins.keys():
        coins[uid] = {'name':first_name,'coins':0,'dailytime':datetime.now(),'hourlytime':datetime.now(),'hp':100}

def check_hp(user):
    check_user(user)
    uid = user.id
    if coins[uid]['hp'] == 0:
        coins[uid]['coins'] = 0
        coins[uid]['hp'] = 100

def show_user(user):
    uid = user.id
    check_user(user)
    #  老房东(10):200
    return f"{coins[uid]['name']}, you have {coins[uid]['coins']} GP and {coins[uid]['hp']} HP"

def add_coins(user,c):
    check_user(user)
    uid = user.id
    coins[uid]['coins'] += c

def add_hp(user,c):
    check_user(user)
    uid = user.id
    if c == -100:
        coins[uid]['hp'] = 0
        check_hp(user)
    else:
        coins[uid]['hp'] += c
        check_hp(user)

def hourly(update,context):
    user = update.effective_user
    check_user(user)
    uid = user.id
    if datetime.now() > coins[uid]['hourlytime']:
        c = random.randint(50,200)
        coins[uid]['coins'] += c
        coins[uid]['dailytime'] = datetime.now() + timedelta(hours=1)
        update.message.reply_text("Here are your hourly coins, %s\n%s coins were placed in your wallet."%(user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one hour hasn't passed yet!")

def daily(update,context):
    user = update.effective_user
    check_user(user)
    uid = user.id
    if datetime.now() > coins[uid]['dailytime']:
        c = random.randint(500,2000)
        coins[uid]['coins'] += c
        coins[uid]['dailytime'] = datetime.now() + timedelta(hours=24)
        update.message.reply_text("Here are your daily coins, %s\n%s coins were placed in your wallet."%(user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one day hasn't passed yet!")

def get_coins(update, context):
    user = update.effective_user
    check_user(user)
    update.message.reply_text(f"{show_user(user)}")

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('bal', get_coins))
    dp.add_handler(CommandHandler('daily', daily))
    dp.add_handler(CommandHandler('hourly', hourly))