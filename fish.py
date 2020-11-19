from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta
import random
import coins
import config

# {
# user:
#   {
#       fishes: [],
#       fcoins: int,
#       gametime: datetime,
#       fpolelvl: int,
#       herringlvl: int,
#       troutlvl: int,
#       sharklvl: int,
#       lvlupfpole: str
#   }
# }
fishgame = {}

def check_fishes(user):
    if not user in fishgame:
        fishgame[user] = {
            'fishes':[
                "You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！",
                "You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！",
                "You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！",
                "You caught two herrings! +16 fishcoins!\n你钓到了两条鲱鱼！+16鱼币！", 
                "You caught three herrings! +24 fishcoins!\n你钓到了三条鲱鱼！+24鱼币！", 
                "You caught four herrings! +32 fishcoins!\n你钓到了四条鲱鱼！+32鱼币！", 
                "You caught a lake trout! +50 fishcoins!\n你钓到了一条湖鳟！+50鱼币！", 
                "You caught two lake trouts! Yeah! +100 fish coins!\n你钓到了两条湖鳟！+100鱼币！耶～", 
                "You forgot your fishing pole!\n你忘了钓鱼竿！", "You forgot your lure!\n你忘了诱饵！", 
                "YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250 fishcoins!\n您钓到了一条大白鲨！你是怎么做到的？+250鱼币！", 
                "You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。", 
                "You caught a lake trout, but it was too large and the police fined you 40 fishcoins!\n您抓到一条鳟鱼，但是它太大了，警察罚款了您40鱼币！", 
                "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", 
                "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", 
                "LMAO you caught nothing. Keep working on it...\n嘻嘻嘻 你什么都没钓到。在修炼一万年吧～", 
                "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", 
                "LMFAO you caught nothing. Keep working on it...\n哈哈哈哈哈哈哈哈哈哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～", 
                "LMAO you caught nothing. Keep working on it...\n哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～"
                ],
            'fcoins':0,
            'gametime':datetime.now(),
            'fpolelvl':0,
            'herringlvl':0,
            'troutlvl':0,
            'sharklvl':0,
            'lvlupfpole':""
        }

# sicheng.old
# {uid: ["You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！","You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！","You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！","You caught two herrings! +16 fishcoins!\n你钓到了两条鲱鱼！+16鱼币！", "You caught three herrings! +24 fishcoins!\n你钓到了三条鲱鱼！+24鱼币！", "You caught four herrings! +32 fishcoins!\n你钓到了四条鲱鱼！+32鱼币！", "You caught a lake trout! +50 fishcoins!\n你钓到了一条湖鳟！+50鱼币！", "You caught two lake trouts! Yeah! +100 fish coins!\n你钓到了两条湖鳟！+100鱼币！耶～", "You forgot your fishing pole!\n你忘了钓鱼竿！", "You forgot your lure!\n你忘了诱饵！", "YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250 fishcoins!\n您钓到了一条大白鲨！你是怎么做到的？+250鱼币！", "You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。", "You caught a lake trout, but it was too large and the police fined you 40 fishcoins!\n您抓到一条鳟鱼，但是它太大了，警察罚款了您40鱼币！", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "LMAO you caught nothing. Keep working on it...\n嘻嘻嘻 你什么都没钓到。在修炼一万年吧～", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "LMFAO you caught nothing. Keep working on it...\n哈哈哈哈哈哈哈哈哈哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～", "LMAO you caught nothing. Keep working on it...\n哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～"]}
# fishes = {}
# {uid: 234234}
# fcoins = {}
# {uid: datetime}
# gametime = {}
# {uid: datetime}
# gametime2 = {}
# {uid: 4}
# fpolelvl = {}

fishes = config.CONFIG["fish"]
def save():
    config.CONFIG["fish"] = fishes
    config.save_config()

def check_fish(user,fish):
    check_fishes(user)
    if fish == fishgame[user]['fishes'][0]:
        fishgame[user]['fcoins'] += 8
    elif fish == fishgame[user]['fishes'][3]:
        fishgame[user]['fcoins'] += 16
    elif fish == fishgame[user]['fishes'][4]:
        fishgame[user]['fcoins'] += 24
    elif fish == fishgame[user]['fishes'][5]:
        fishgame[user]['fcoins'] += 32
    elif fish == fishgame[user]['fishes'][6]:
        fishgame[user]['fcoins'] += 50
    elif fish == fishgame[user]['fishes'][7]:
        fishgame[user]['fcoins'] += 100
    elif fish == fishgame[user]['fishes'][10]:
        fishgame[user]['fcoins'] += 250
    elif fish == fishgame[user]['fishes'][11]:
        coins.add_hp(user,-100)
    elif fish == fishgame[user]['fishes'][12]:
        fishgame[user]['fcoins'] -= 40
    save()

def check_fishpole(user): 
    check_fishes(user) 
    if fishgame[user]['fpolelvl'] == 0:
        fishgame[user]['lvlupfpole'] = "100"
    elif fishgame[user]['fpolelvl'] == 1:
        fishgame[user]['lvlupfpole'] = "140"
    elif fishgame[user]['fpolelvl'] == 2:
        fishgame[user]['lvlupfpole'] = "193"
    elif fishgame[user]['fpolelvl'] == 3:
        fishgame[user]['lvlupfpole'] = "259"
    elif fishgame[user]['fpolelvl'] == 4:
        fishgame[user]['lvlupfpole'] = "338"
    elif fishgame[user]['fpolelvl'] == 5:
        fishgame[user]['lvlupfpole'] = "Sorry, you are already at max level"
    save()

def get_gametime(user):
    check_fishes(user)
    return fishgame[user]['gametime']

def set_gametime(user,time):
    check_fishes(user)
    fishgame[user]['gametime'] = time
    return time

def buy_fishpole(user):
    check_fishes(user)
    if fishgame[user]['lvlupfpole'].isdigit:
        if fishgame[user]['fcoins'] >= int(fishgame[user]['lvlupfpole']):
            fishgame[user]['fcoins'] -= int(fishgame[user]['lvlupfpole'])
            fishgame[user]['fpolelvl'] += 1
            fishgame[user]['fishes'].remove(fishgame[user][13])
            return "Nice! Your current level: %s\nYou still have %s fishcoins"%(fishgame[user]['fpolelvl'],fishgame[user]['fcoins'])
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT"
    else:
        return "Bruh stop being so greedy ur already at max level"
    save()

def buy_baitherring(user):
    check_fishes(user)
    if fishgame[user]['herringlvl'] == 0:
        if fishgame[user]['fcoins'] >= 50:
            fishgame[user]['fcoins'] -= 50
            fishgame[user]['fishes'].append("You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！")
            fishgame[user]['fishes'].append("You caught two herrings! +16 fishcoins!\n你钓到了两条鲱鱼！+16鱼币！")
            fishgame[user]['herringlvl'] += 1
            save()
            return "Nice! Your current level: 1"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT"
    else:
        return "Bruh stop being so greedy ur already at max level"

def buy_baittrout(user):
    check_fishes(user)
    if fishgame[user]['troutlvl'] == 0:
        if fishgame[user]['fcoins'] >= 200:
            fishgame[user]['fcoins'] -= 200
            fishgame[user]['fishes'].append("You caught a lake trout! +50 fishcoins!\n你钓到了一条湖鳟！+50鱼币！")
            fishgame[user]['troutlvl'] += 1
            save()
            return "Nice! Your current level: MAX"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT"
    else:
        return "Bruh stop being so greedy ur already at max level"

def buy_baitshark(user):
    check_fishes(user)
    if fishgame[user]['sharklvl'] == 0:
        if fishgame[user]['fcoins'] >= 500:
            fishgame[user]['fcoins'] -= 500
            fishgame[user]['fishes'].append("YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250 fishcoins!\n您钓到了一条大白鲨！你是怎么做到的？+250鱼币！")
            fishgame[user]['fishes'].append("You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。")
            fishgame[user]['sharklvl'] += 1
            save()
            return "Nice! Your current level: MAX"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT"
    else:
        return "Bruh stop being so greedy ur already at max level"

def fish(update, context):
    user = update.effective_user
    check_fishes(user)
    result = random.choice(fishgame[user]['fishes'])
    t = datetime.now() 
    if t >= get_gametime(user):
        update.message.reply_text("%s\n/fishbal to see the number of fishcoins you have!\n/fishbal 来看看你有多少鱼币！\nCreator/作者: Sichengthebest"%result)
        check_fish(user,result)
        set_gametime(user,datetime.now() + timedelta(seconds=30))
        save()
    else:
        update.message.reply_text("Slow it down, cmon!!! The fish seem weary of fishermen right now, wait a few more seconds!\nCreator/作者: Sichengthebest")

def shop(update, context):
    user = update.effective_user
    check_fishpole(user)
    markets = ["The Fisher's BFF","The Ultimate Fishing Shop","Canadian Tire","Alfred-The-Angler's Hangar Of Magnificent Fishing Accessories At A Very Very Low Price","Mr.Loïc's Fishing Grounds"]
    if len(context.args) == 0:
        update.message.reply_text("""Here are some stuff you can buy at %s.
--------------------------------------
Upgrade your fishing pole! %s fishcoins for upgrade.
/fishshop fishingpole
Current level: %s
--------------------------------------
Buy special baits to attract different types of fish!
Herring baits: 50 fishcoins for buy.
/fishshop baitherring
Trout baits: 200 fishcoins to buy.
/fishshop baittrout
Shark baits: 500 fishcoins to buy.
/fishshop baitshark
WARNING: BAITS DO NOT INCREASE SURVIVAL RATE
--------------------------------------"""%(random.choice(markets),fishgame[user]['lvlupfpole'],fishgame[user]['fpolelvl']))
    elif context.args[0] == "fishingpole":
        update.message.reply_text("%s"%buy_fishpole(user))
    elif context.args[0] == "baitherring":
        update.message.reply_text("%s"%buy_baitherring(user))
    elif context.args[0] == "baittrout":
        update.message.reply_text("%s"%buy_baittrout(user))
    elif context.args[0] == "baitshark":
        update.message.reply_text("%s"%buy_baitshark(user))
    else:
        update.message.reply_text("Bruh what are you doing this item isn't even in the shop!")
    save()

def bal(update,context):
    global fishgame
    user = update.effective_user
    check_fishes(user)
    update.message.reply_text("Your balance: %s fishcoins.\n/fishshop to buy items that increase your chances of catching fish!\n/fishshop 来购买可以增加您钓到鱼的机会的物品！"%fishgame[user]['fcoins'])

def get_command():
    return [BotCommand('fish','Gain fishcoins by fishing. // 以钓鱼的方式获得鱼币。')]

def addHandler(dispatcher):
    fsHandler = CommandHandler('fish', fish)
    shopHandler = CommandHandler('fishshop', shop)
    balHandler = CommandHandler('fishbal',bal)
    dispatcher.add_handler(fsHandler)
    dispatcher.add_handler(shopHandler)
    dispatcher.add_handler(balHandler)