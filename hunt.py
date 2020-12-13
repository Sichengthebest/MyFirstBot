from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta
import random
import coins
import config

huntgame = config.CONFIG["hunt"]
# {
# uid:
#   {
#       huntArr: [],
#       bcoins: int,
#       gametime: datetime,
#       riflelvl: int
#   }
# }

translater = {
    "skunk1":{
        "msg":"You brought back a skunk! Gain 10 beastcoins. BTW I wonder who would want a skunk...\n你带回了一只臭鼬！获得10兽币。顺便说一句，我想知道谁会想要臭鼬...",
        "gif":'https://thumbs.gfycat.com/DeepSpryJanenschia-small.gif',
        "bcoins":10
    },
    "skunk2":{
        "msg":"You brought back a skunk! Gain 10 beastcoins. You STINK!\n你带回了一只臭鼬！获得10兽币。你好臭！",
        "gif":'https://thumbs.gfycat.com/DeepSpryJanenschia-small.gif',
        "bcoins":10
    },
    "deer1":{
        "msg":"You have caught a deer! Gain 25 beastcoins. Good thing you didn't get lost in the forest!\n你抓到了一头鹿！获得25兽币。很好，你没有在森林里迷路！",
        "gif":'https://media1.tenor.com/images/1100bff4414c3328797c3f39422e347e/tenor.gif?itemid=7246228',
        "bcoins":25
    },
    "deer2":{
        "msg":"You have caught a deer! Gain 25 beastcoins. Good thing you brought your compass!\n你抓到了一头鹿！获得25兽币。很好，你带了指南针！",
        "gif":'https://media1.tenor.com/images/1100bff4414c3328797c3f39422e347e/tenor.gif?itemid=7246228',
        "bcoins":25
    },
    "deer3":{
        "msg":"You have caught a deer! Gain 25 beastcoins.\n你抓到了一头鹿！获得25兽币。",
        "gif":'https://media1.tenor.com/images/1100bff4414c3328797c3f39422e347e/tenor.gif?itemid=7246228',
        "bcoins":25
    },
    "fox":{
        "msg":"You have caught a fox! Nice work! Gain 30 beastcoins.\n你抓到了一只狐狸！干得好！获得30兽币",
        "gif":'https://i.imgur.com/NSxU6zi.gif',
        "bcoins":30
    },
    "rhino":{
        "msg":"You have caught a rhinoceros! Was that even legal? Anyways, the buyer gave you 100 beastcoins.\n你抓到了犀牛！那合法吗？无论如何，卖家给了你100兽币。",
        "gif":'https://thumbs.gfycat.com/SnivelingInsidiousAfricanmolesnake-size_restricted.gif',
        "bcoins":100
    },
    "basilisk":{
        "msg":"You have caught a BASILISK!! Where in the world did you find that??? These 250 beastcoins are for you, you earned them!!!\n您抓到了蛇怪！您在哪里找到的？？？这250兽币是给你的，无敌战士！",
        "gif":'https://pa1.narvii.com/6313/78f72b6a49d0b52d862f339ce9c957b9d1224ffb_hq.gif',
        "bcoins":250
    },
    "not1":{
        "msg":"You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！",
        "gif":"https://i.imgur.com/A7JObT4.gif",
        "bcoins":0
    },
    "not2":{
        "msg":"U suck, you didn't bring back anything!\n你好烂，你什么也没抓到！",
        "gif":"https://i.imgur.com/A7JObT4.gif",
        "bcoins":0
    },
    "not3":{
        "msg":"LMAO you are so BAD, you didn't bring back anything!\n哈哈哈 你好烂，你什么也没抓到！",
        "gif":"https://i.imgur.com/A7JObT4.gif",
        "bcoins":0
    },
    "not4":{
        "msg":"You forgot your AK-47! Too bad.\n你忘记了你的AK-47！太糟糕了。",
        "gif":"https://i.imgur.com/A7JObT4.gif",
        "bcoins":0
    },
    "not5":{
        "msg":"You have caught a fox, but some stole it from you!\n您捉住了一只狐狸，但是有人偷走了它！",
        "gif":'https://i.imgur.com/NSxU6zi.gif',
        "bcoins":0
    },
    "bear":{
        "msg":"A bear caught you and you lost 30HP!\n一只熊抓住了您，您损失了30HP",
        "gif":"https://media.tenor.com/images/b56c248026025ffb4677957bc9079c40/tenor.gif",
        "bcoins":0
    },
    "basiliskdead":{
        "msg":"You DIED while fighting the basilisk!\n您在与蛇怪战斗时死了！",
        "gif":"https://i.pinimg.com/originals/35/97/03/359703d544dc70bb1a12852888198e66.gif",
        "bcoins":0
    },
    "elephant":{
        "msg":"You have caught an elephant, but some annoying dude found your ads, and called the cops on you! You got fined 100 beastcoins.\n您抓到了一头大象，但是一些恼人的家伙找到了您的广告，并叫了警察！您被罚款100枚野兽币。",
        "gif":"https://static.wikia.nocookie.net/farcry/images/9/92/Giphy.gif/revision/latest/top-crop/width/220/height/220?cb=20180906101132",
        "bcoins":-100
    }
}

translater2 = {
    "skunk1": "skunk",
    "skunk2": "skunk",
    "deer1": "deer",
    "deer2": "deer",
    "deer3": "deer"
}

def check_user(uid):
    if not uid in huntgame:
#       item = random.choice(hg[uid]['huntArr'])
#       send_msg( translater[item]['msg'] )
#       send_anim( translater[item]['gif']  caption=translater[item]['msg'] )
        huntgame[uid] = {
            'huntArr': ["skunk1","skunk2","deer1","deer2","deer3","fox","rhino","basilisk","not1","not1","not1","not1","not1","not2","not3","not4","not5","bear","basiliskdead","elephant"],
            'bcoins':0,
            'gametime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'riflelvl':0,
            'lvluprifle':""
        }

def save():
    config.CONFIG["hunt"] = huntgame
    config.save_config()

def hunt(update, context):
    user = update.effective_user
    uid = str(user.id)
    check_user(uid)
    t = datetime.now() 
    if t >= datetime.strptime(huntgame[uid]['gametime'],"%Y/%m/%d %H:%M:%S"):
        item = random.choice(huntgame[uid]['huntArr'])
        update.message.reply_animation('%s'%translater[item]["gif"],caption="%s\n/huntbal to see the number of beastcoins you have!\n/huntbal 来看看你有多少兽币！\nCreator/作者: Sichengthebest"%translater[item]['msg'])
        huntgame[uid]['bcoins'] += translater[item]["bcoins"]
        if item == "skunk1" or item == "skunk2" or item == "deer1" or item == "deer2" or item == "deer3":
            coins.add_item(user,translater2[item],1)
        elif item == "rhino" or item == "fox" or item == "basilisk":
            coins.add_item(user,item,1)
        elif item == "bear":
            coins.add_hp(user,-30)
        elif item == "basilisk":
            coins.add_hp(user,-100)
        huntgame[uid]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=30),"%Y/%m/%d %H:%M:%S")
        save()
    else:
        update.message.reply_text("Slow it down, cmon!!! The forest seems a little empty right now, try again in a few more seconds!\n慢下来，呆瓜！森林里的动物似乎已经都被杀了，请在几秒钟后再试一次！\nCreator/作者: Sichengthebest")

def check_rifle(uid): 
    check_user(uid) 
    if huntgame[uid]['riflelvl'] == 0:
        huntgame[uid]['lvluprifle'] = "120"
    elif huntgame[uid]['riflelvl'] == 1:
        huntgame[uid]['lvluprifle'] = "160"
    elif huntgame[uid]['riflelvl'] == 2:
        huntgame[uid]['lvluprifle'] = "213"
    elif huntgame[uid]['riflelvl'] == 3:
        huntgame[uid]['lvluprifle'] = "279"
    elif huntgame[uid]['riflelvl'] == 4:
        huntgame[uid]['lvluprifle'] = "358"
    elif huntgame[uid]['riflelvl'] == 5:
        huntgame[uid]['lvluprifle'] = "Sorry, ur already at max level"

def shop(update, context):
    uid = str(update.effective_user.id)
    check_rifle(uid)
    markets = ["The Hunter's House","The Trap Territory","The Deer Master","Mr.Rutland's Hunter Corner"]
    marketsCH = ["猎人之家","陷阱领土","鹿王","拉特兰先生的猎人之角"]
    if len(context.args) == 0:
        update.message.reply_text("""Here's some stuff you can buy at %s.
--------------------------------------
Upgrade your hunting rifle! %s beastcoins for upgrade.
/huntshop rifle
Current level: %s
--------------------------------------
您可以在%s购买一些东西。
--------------------------------------
升级您的狩猎步枪！%s兽币进行升级。
/huntshop rifle
当前等级：%s"""%(random.choice(markets),huntgame[uid]['lvluprifle'],huntgame[uid]['riflelvl'],random.choice(marketsCH),huntgame[uid]['lvluprifle'],huntgame[uid]['riflelvl']))
    elif context.args[0] == "rifle":
        update.message.reply_text("%s"%buy_rifle(uid))
    else:
        update.message.reply_text("Bruh what are you doing this item isn't even in the shop!\n你真parker，你在做什么？这个东西不在商店里！")
    save()

def buy_rifle(uid):
    check_user(uid)
    if huntgame[uid]['lvluprifle'].isdigit:
        if huntgame[uid]['bcoins'] >= int(huntgame[uid]['lvluprifle']):
            huntgame[uid]['bcoins'] -= int(huntgame[uid]['lvluprifle'])
            huntgame[uid]['riflelvl'] += 1
            huntgame[uid]['huntArr'].remove("not1")
            save()
            return "Nice! Your current level: %s\nYou still have %s beastcoins\n耶！您当前的级别：%s \n您还有%s兽币"%(huntgame[uid]['riflelvl'],huntgame[uid]['bcoins'],huntgame[uid]['riflelvl'],huntgame[uid]['bcoins'])
        else:
            return "No offense but... HAHAHAHAHA YOU ARE SO POOR YOU CANNOT BUY THIS OBJECT\n不想冒犯你，但是...哈哈哈哈哈，您太穷了，您无法购买此物品"
    else:
        return "Bruh stop being so greedy ur already at max level\n傻瓜不要这么贪婪，您已经处于最高等级"
    save()

def bal(update,context):
    uid = str(update.effective_user.id)
    check_user(uid)
    update.message.reply_text("Your balance: %s beastcoins/兽币.\n/huntshop to buy items that increase your chances of catching animals!\n/huntshop 来购买可以增加您抓到动物的机会的物品！"%huntgame[uid]['bcoins'])

def get_command():
    return [BotCommand('hunt','Gain XP by catching animals. // 以捕捉动物的方式获得XP。')]

def addHandler(dispatcher):
    huntHandler = CommandHandler('hunt', hunt)
    dispatcher.add_handler(huntHandler)
    dispatcher.add_handler(CommandHandler('huntbal', bal))
    dispatcher.add_handler(CommandHandler('huntshop', shop))