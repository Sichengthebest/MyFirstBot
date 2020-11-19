from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta
import random
import coins
import config

huntgame = {}
# {
# user:
#   {
#       huntArr: [],
#       bcoins: int,
#       gametime: datetime,
#       riflelvl: int
#   }
# }
def check_user(user):
    if not user in huntgame:
        huntgame[user] = {
            'huntArr': ["You brought back a skunk! Gain 10 beastcoins. BTW I wonder who would want a skunk...\n你带回了一只臭鼬！获得10野兽币。顺便说一句，我想知道谁会想要臭鼬...",
            "You brought back a skunk! Gain 10 beastcoins. You STINK!\n你带回了一只臭鼬！获得10野兽币。你好臭！",
            "You have caught a deer! Gain 25 beastcoins. Good thing you didn't get lost in the forest!\n你抓到了一头鹿！获得25野兽币。很好，你没有在森林里迷路！",
            "You have caught a deer! Gain 25 beastcoins. Good thing you brought your compass!\n你抓到了一头鹿！获得25野兽币。很好，你带了指南针！",
            "You have caught a fox! Nice work! Gain 30 beastcoins.\n你抓到了一只狐狸！干得好！获得30野兽币",
            "You have caught a deer! Gain 25 beastcoins.\n你抓到了一头鹿！获得25野兽币。",
            "You have caught a rhinoceros! Was that even legal? Anyways, the buyer gave you 100 beastcoins.\n你抓到了犀牛！那合法吗？无论如何，卖家给了你100野兽币。",
            "You have caught a BASILISK!! Where in the world did you find that??? These 250 beastcoins are for you, you earned them!!!\n您抓到了蛇怪！您在哪里找到的？？？这250野兽币是给你的，无敌战士！",
            "You forgot your AK-47! Too bad.\n你忘记了你的AK-47！太糟糕了。",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "You caught a fox, but someone stole it from you!\n您捉住了一只狐狸，但有人偷走了它！",
            "A bear caught you and you lost 30HP!\n一只熊抓住了您，您损失了30HP", "You caught an elephant, but the ads you placed was found by someone, and he called the cops on you! You got fined 100 beastcoins. Maybe try the black market next time?\n您抓到一头大象，但您的猎物被某人发现，他叫了警察！您被罚款100野兽币。",
            "You DIED while fighting the basilisk!\n您在与蛇怪战斗时死了！",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
            "LMAO you are so BAD, you didn't bring back anything!\n哈哈哈 你好烂，你什么也没抓到！",
            "U suck, you didn't bring back anything!\n你好烂，你什么也没抓到！"],
            'bcoins':0,
            'gametime':datetime.now(),
            'riflelvl':0,
            'lvluprifle':""
        }

animals = config.CONFIG["hunt"]
def save():
    config.CONFIG["hunt"] = animals
    config.save_config()

def check_animal(user):
    huntArr = huntgame[user]['huntArr']
    result = random.choice(huntArr)
    if result == huntArr[0] or result == huntArr[1]:
        huntgame[user]['bcoins'] += 10
    elif result == huntArr[2] or result == huntArr[3] or result == huntArr[5]:
        huntgame[user]['bcoins'] += 25
    elif result == huntArr[4]:
        huntgame[user]['bcoins'] += 30
    elif result == huntArr[6]:
        huntgame[user]['bcoins'] += 100
    elif result == huntArr[7]:
        huntgame[user]['bcoins'] += 250
    elif result == huntArr[11]:
        coins.add_hp(user,-30)
    elif result == huntArr[12]:
        huntgame[user]['bcoins'] -= 100
    elif result == huntArr[13]:
        coins.add_hp(user,-100)
    save()
    return result

def hunt(update, context):
    user = update.effective_user
    check_user(user)
    t = datetime.now() 
    if t >= huntgame[user]['gametime']:
        result = check_animal(user)
        update.message.reply_text("%s\n/huntbal to see the number of beastcoins you have!\n/huntbal 来看看你有多少野兽币！\nCreator/作者: Sichengthebest"%result)
        huntgame[user]['gametime'] = datetime.now() + timedelta(seconds=30)
        save()
    else:
        update.message.reply_text("Slow it down, cmon!!! The forest seems a little empty right now, try again in a few more seconds!\nCreator/作者: Sichengthebest")

def check_rifle(user): 
    check_user(user) 
    if huntgame[user]['riflelvl'] == 0:
        huntgame[user]['lvluprifle'] = "120"
    elif huntgame[user]['riflelvl'] == 1:
        huntgame[user]['lvluprifle'] = "160"
    elif huntgame[user]['riflelvl'] == 2:
        huntgame[user]['lvluprifle'] = "213"
    elif huntgame[user]['riflelvl'] == 3:
        huntgame[user]['lvluprifle'] = "279"
    elif huntgame[user]['riflelvl'] == 4:
        huntgame[user]['lvluprifle'] = "358"
    elif huntgame[user]['riflelvl'] == 5:
        huntgame[user]['lvluprifle'] = "Sorry, you are already at max level"

def shop(update, context):
    user = update.effective_user
    check_rifle(user)
    markets = ["The Hunter's House","The Trap Territory","The Deer Master","Mr.Rutland's Hunter Corner"]
    if len(context.args) == 0:
        update.message.reply_text("""Here's some stuff you can buy at %s.
--------------------------------------
Upgrade your hunting rifle! %s fishcoins for upgrade.
/huntshop rifle
Current level: %s"""%(random.choice(markets),huntgame[user]['lvluprifle'],huntgame[user]['riflelvl']))
    elif context.args[0] == "rifle":
        update.message.reply_text("%s"%buy_rifle(user))
    else:
        update.message.reply_text("Bruh what are you doing this item isn't even in the shop!")
    save()

def buy_rifle(user):
    check_user(user)
    if huntgame[user]['lvluprifle'].isdigit:
        if huntgame[user]['bcoins'] >= int(huntgame[user]['lvluprifle']):
            huntgame[user]['bcoins'] -= int(huntgame[user]['lvluprifle'])
            huntgame[user]['riflelvl'] += 1
            huntgame[user]['huntArr'].remove(huntgame[user][14])
            save()
            return "Nice! Your current level: %s\nYou still have %s fishcoins"%(huntgame[user]['riflelvl'],huntgame[user]['bcoins'])
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT"
    else:
        return "Bruh stop being so greedy ur already at max level"

def bal(update,context):
    user = update.effective_user
    check_user(user)
    update.message.reply_text("Your balance: %s beastcoins.\n/huntshop to buy items that increase your chances of catching animals!\n/huntshop 来购买可以增加您抓到动物的机会的物品！"%huntgame[user]['bcoins'])

def get_command():
    return [BotCommand('hunt','Gain XP by catching animals. // 以捕捉动物的方式获得XP。')]

def addHandler(dispatcher):
    huntHandler = CommandHandler('hunt', hunt)
    dispatcher.add_handler(huntHandler)
    dispatcher.add_handler(CommandHandler('huntbal', bal))
    dispatcher.add_handler(CommandHandler('huntshop', shop))