from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta
import random
import coins
import config

# {
# uid:
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

fishgame = config.CONFIG["fish"]

def check_fishes(uid):
    if not uid in fishgame:
        fishgame[uid] = {
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
            'gametime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
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

def save():
    config.CONFIG["fish"] = fishgame
    config.save_config()

def check_gif(uid,fish):
    gif = ''
    if fish == fishgame[uid]['fishes'][0] or fish == fishgame[uid]['fishes'][1]or fish == fishgame[uid]['fishes'][2] or fish == fishgame[uid]['fishes'][3] or fish == fishgame[uid]['fishes'][4] or fish == fishgame[uid]['fishes'][5]:
        gif = 'https://i.gifer.com/E4kx.gif'
    elif fish == fishgame[uid]['fishes'][6] or fish == fishgame[uid]['fishes'][7] :
        gif = 'https://i.chzbgr.com/full/8263044608/h8FC3F6E6/gone-fishing'
    elif fish == fishgame[uid]['fishes'][10]:
        gif = 'https://wp.usatodaysports.com/wp-content/uploads/sites/90/2015/12/shark.gif'
    elif fish == fishgame[uid]['fishes'][11]:
        gif = 'https://64.media.tumblr.com/ea4c7dafe8b69ab42401c03722d37cc1/tumblr_nabynen64k1sqmphzo5_400.gifv'
    elif fish == fishgame[uid]['fishes'][12]:
        gif = 'https://i.pinimg.com/originals/3a/a8/68/3aa86868b40faf961541c3d8e6dac375.gif'
    else:
        gif = 'https://i.gifer.com/3kcZ.gif'
    return gif

def check_fish(uid,user,fish):
    check_fishes(uid)
    if fish == fishgame[uid]['fishes'][0]:
        fishgame[uid]['fcoins'] += 8
        coins.add_item(user,"herring",1)
    elif fish == fishgame[uid]['fishes'][3]:
        fishgame[uid]['fcoins'] += 16
        coins.add_item(user,"herring",2)
    elif fish == fishgame[uid]['fishes'][4]:
        fishgame[uid]['fcoins'] += 24
        coins.add_item(user,"herring",3)
    elif fish == fishgame[uid]['fishes'][5]:
        fishgame[uid]['fcoins'] += 32
        coins.add_item(user,"herring",4)
    elif fish == fishgame[uid]['fishes'][6]:
        fishgame[uid]['fcoins'] += 50
        coins.add_item(user,"trout",1)
    elif fish == fishgame[uid]['fishes'][7]:
        fishgame[uid]['fcoins'] += 100
        coins.add_item(user,"trout",2)
    elif fish == fishgame[uid]['fishes'][10]:
        fishgame[uid]['fcoins'] += 250
        coins.add_item(user,"shark",1)
    elif fish == fishgame[uid]['fishes'][11]:
        coins.add_hp(user,-100)
    elif fish == fishgame[uid]['fishes'][12]:
        fishgame[uid]['fcoins'] -= 40
    save()

def check_fishpole(uid): 
    check_fishes(uid) 
    if fishgame[uid]['fpolelvl'] == 0:
        fishgame[uid]['lvlupfpole'] = "100"
    elif fishgame[uid]['fpolelvl'] == 1:
        fishgame[uid]['lvlupfpole'] = "140"
    elif fishgame[uid]['fpolelvl'] == 2:
        fishgame[uid]['lvlupfpole'] = "193"
    elif fishgame[uid]['fpolelvl'] == 3:
        fishgame[uid]['lvlupfpole'] = "259"
    elif fishgame[uid]['fpolelvl'] == 4:
        fishgame[uid]['lvlupfpole'] = "338"
    elif fishgame[uid]['fpolelvl'] == 5:
        fishgame[uid]['lvlupfpole'] = "Sorry, you are already at max level"
    save()

def buy_fishpole(uid):
    check_fishes(uid)
    if fishgame[uid]['lvlupfpole'].isdigit:
        if fishgame[uid]['fcoins'] >= int(fishgame[uid]['lvlupfpole']):
            fishgame[uid]['fcoins'] -= int(fishgame[uid]['lvlupfpole'])
            fishgame[uid]['fpolelvl'] += 1
            fishgame[uid]['fishes'].remove(fishgame[uid]['fishes'][13])
            return "Nice! Your current level: %s\nYou still have %s fishcoins\n耶！您当前的级别：%s \n您还有%s鱼币"%(fishgame[uid]['fpolelvl'],fishgame[uid]['fcoins'],fishgame[uid]['fpolelvl'],fishgame[uid]['fcoins'])
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT\n不想冒犯你，但是...哈哈哈哈哈，您太穷了，您无法购买此物品"
    else:
        return "Bruh stop being so greedy ur already at max level\n傻瓜不要这么贪婪，您已经处于最高等级"
    save()

def buy_baitherring(uid):
    check_fishes(uid)
    if fishgame[uid]['herringlvl'] == 0:
        if fishgame[uid]['fcoins'] >= 50:
            fishgame[uid]['fcoins'] -= 50
            fishgame[uid]['fishes'].append("You caught a herring! +8 fishcoins!\n你钓到了一条鲱鱼！+8鱼币！")
            fishgame[uid]['fishes'].append("You caught two herrings! +16 fishcoins!\n你钓到了两条鲱鱼！+16鱼币！")
            fishgame[uid]['herringlvl'] += 1
            save()
            return "Nice! Your current level: 1\n耶！您当前的等级：1"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT\n不想冒犯你，但是...哈哈哈哈哈，您太穷了，您无法购买此物品"
    else:
        return "Bruh stop being so greedy ur already at max level\n傻瓜不要这么贪婪，您已经处于最高等级"

def buy_baittrout(uid):
    check_fishes(uid)
    if fishgame[uid]['troutlvl'] == 0:
        if fishgame[uid]['fcoins'] >= 200:
            fishgame[uid]['fcoins'] -= 200
            fishgame[uid]['fishes'].append("You caught a lake trout! +50 fishcoins!\n你钓到了一条湖鳟！+50鱼币！")
            fishgame[uid]['troutlvl'] += 1
            save()
            return "Nice! Your current level: 1\n耶！您当前的等级：1"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT\n不想冒犯你，但是...哈哈哈哈哈，您太穷了，您无法购买此物品"
    else:
        return "Bruh stop being so greedy ur already at max level\n傻瓜不要这么贪婪，您已经处于最高等级"

def buy_baitshark(uid):
    check_fishes(uid)
    if fishgame[uid]['sharklvl'] == 0:
        if fishgame[uid]['fcoins'] >= 500:
            fishgame[uid]['fcoins'] -= 500
            fishgame[uid]['fishes'].append("YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250 fishcoins!\n您钓到了一条大白鲨！你是怎么做到的？+250鱼币！")
            fishgame[uid]['fishes'].append("You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。")
            fishgame[uid]['sharklvl'] += 1
            save()
            return "Nice! Your current level: 1\n耶！您当前的等级：1"
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT\n不想冒犯你，但是...哈哈哈哈哈，您太穷了，您无法购买此物品"
    else:
        return "Bruh stop being so greedy ur already at max level\n傻瓜不要这么贪婪，您已经处于最高等级"

def fish(update, context):
    user = update.effective_user
    uid = str(update.effective_user.id)
    check_fishes(uid)
    result = random.choice(fishgame[uid]['fishes'])
    t = datetime.now() 
    if t >= datetime.strptime(fishgame[uid]['gametime'],"%Y/%m/%d %H:%M:%S"):
        update.message.reply_animation('%s'%check_gif(uid,result),caption="%s\n/fishbal to see the number of fishcoins you have!\n/fishbal 来看看你有多少鱼币！\nCreator/作者: Sichengthebest"%result)
        check_fish(uid,user,result)
        fishgame[uid]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=30),"%Y/%m/%d %H:%M:%S")
        save()
    else:
        difference = datetime.strptime(fishgame[uid]['gametime'],"%Y/%m/%d %H:%M:%S") - datetime.now() 
        seconds = int(difference.total_seconds())
        update.message.reply_text(f"Slow it down, cmon!!! The fish seem weary of fishermen right now, wait {seconds} seconds!\n放慢速度，呆瓜！！！鱼现在似乎知道哪个是鱼饵哪个是鱼，还要再等{seconds}秒钟他们才变傻！\nCreator/作者: Sichengthebest")

def shop(update, context):
    uid = str(update.effective_user.id)
    check_fishpole(uid)
    markets = ["The Fisher's BFF","The Ultimate Fishing Shop","Canadian Tire","Alfred-The-Angler's Hangar Of Magnificent Fishing Accessories At A Very Very Low Price","Mr.Loïc's Fishing Grounds"]
    marketsCH = ["渔民的BFF","终极钓鱼店","加拿大轮胎","阿尔弗雷德·安格勒的华丽渔具机库，价格非常低廉","洛伊克先生的渔场"]
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
--------------------------------------
您可以在%s购买一些东西。
--------------------------------------
升级您的钓鱼竿！ %s鱼币进行升级。
/fishshop fishingpole
当前级别：%s
--------------------------------------
购买特殊的诱饵来吸引不同类型的鱼！
鲱鱼饵：50枚鱼币可供购买。
/fishshop baitherring
鳟鱼饵：200枚鱼币可供购买。
/fishshop baittrout
鲨鱼饵：500枚鱼币可供购买。
/fishshop baitshark
警告：诱饵不会增加生存率
"""%(random.choice(markets),fishgame[uid]['lvlupfpole'],fishgame[uid]['fpolelvl'],random.choice(marketsCH),fishgame[uid]['lvlupfpole'],fishgame[uid]['fpolelvl']))
    elif context.args[0] == "fishingpole":
        update.message.reply_text("%s"%buy_fishpole(uid))
    elif context.args[0] == "baitherring":
        update.message.reply_text("%s"%buy_baitherring(uid))
    elif context.args[0] == "baittrout":
        update.message.reply_text("%s"%buy_baittrout(uid))
    elif context.args[0] == "baitshark":
        update.message.reply_text("%s"%buy_baitshark(uid))
    else:
        update.message.reply_text("Bruh what are you doing this item isn't even in the shop!\n你真parker，你在做什么？这个东西不在商店里！")
    save()

def bal(update,context):
    global fishgame
    uid = str(update.effective_user.id)
    check_fishes(uid)
    update.message.reply_text("Your balance: %s fishcoins/鱼币.\n/fishshop to buy items that increase your chances of catching fish!\n/fishshop 来购买可以增加您钓到鱼的机会的物品！"%fishgame[uid]['fcoins'])

def get_command():
    return [BotCommand('fish','Gain fishcoins by fishing. // 以钓鱼的方式获得鱼币。')]

def addHandler(dispatcher):
    fsHandler = CommandHandler('fish', fish)
    shopHandler = CommandHandler('fishshop', shop)
    balHandler = CommandHandler('fishbal',bal)
    dispatcher.add_handler(fsHandler)
    dispatcher.add_handler(shopHandler)
    dispatcher.add_handler(balHandler)