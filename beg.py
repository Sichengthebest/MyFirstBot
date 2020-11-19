from telegram.ext import CommandHandler, dispatcher
from telegram import BotCommand
from datetime import datetime,timedelta
import random
import coins

gametimes = {}

def get_users(user):
    if not user in gametimes:
        gametimes[user] = datetime.now()

def beg(update,context):
    ppl = ["BOTGOD","@TheRandomDudeHimself","Brad Pitt","A Discord mod","A Random Orange Dude","Joe","Bob","Spongebob","The Red Dude In Among Us","Ur mom","Meryl Streep","Google Translate","A Homeless Man"]
    pplCH = ["BOTGOD","@TheRandomDudeHimself","布拉德·皮特","一个Discord管理员","唐纳德·特朗普","乔","鲍勃","海绵宝宝","《我们之中》红色的家伙","你老妈","梅丽尔·斯特里普","谷歌翻译","一个无家可归的人"]
    badstuff = ["Sorry I used all my money to fund the Pfizer vaccine","Sorry I used all my money to fund the Moderna vaccine","Stop begging","NO","Of course not","Oh dang I forgot my purse","Let me think...NO","Yes...maybe...nvr mind","NEVER","Nah","I used all my money to fund the Biden campaign","I donated too much to @ZahJmPvjo3Hjz6CDNceG","Sorry I have no more money cuz I bought 10,000 rolls of toilet paper at the start of the pandemic"]
    index = random.randint(0,12)
    yesorno = random.randint(1,2)
    user = update.effective_user
    get_users(user)
    t = datetime.now()
    if t < gametimes[user]:
        update.message.reply_text("Slow it down, cmon!!! Stop begging so much, it makes you look like a little baby.\nCreator/作者: Sichengthebest")
        return
    if index == 0:
        rwbotgod = random.randint(10,250)
        update.message.reply_text("%s donated %s GP to you!\nCreator/作者: Sichengthebest"%(ppl[index],rwbotgod))
        coins.add_coins(user,rwbotgod)
    elif index == 1:
        rwsicheng = random.randint(50,400)
        update.message.reply_text("%s donated %s GP to you!\nCreator/作者: Sichengthebest"%(ppl[index],rwsicheng))
        coins.add_coins(user,rwsicheng)
    elif index == 2 or index == 3 or index == 5 or index == 6 or index == 7 or index == 10 or index == 11:
        if yesorno == 1:
            rwbrad = random.randint(10,100)
            update.message.reply_text("%s donated %s GP to you!\nCreator/作者: Sichengthebest"%(ppl[index],rwbrad))
            coins.add_coins(user,rwbrad)
        else:
            update.message.reply_text("%s: %s"%(ppl[index],badstuff[index]))
    elif index == 4:
        update.message.reply_text("%s: STOP THE STEAL! STOP THE STEAL! STOP THE STEAL!\nCreator/作者: Sichengthebest"%(ppl[index]))
    elif index == 8:
        amongus = ["Ur sus","You died","Shut up, or I'll sabotage the lights"]
        amongusCH = ["我怀疑你","你死了","闭嘴，不然的话我会把灯关上"]
        auindex = random.randint(0,2)
        if auindex == 0 or auindex == 2:
            update.message.reply_text("%s: %s\nCreator/作者: Sichengthebest"%(ppl[index],amongus[auindex]))
        else:
            update.message.reply_text("%s: %s\nCreator/作者: Sichengthebest"%(ppl[index],amongus[auindex]))
            coins.add_hp(user,-100)
    elif index == 9:
        update.message.reply_text("%s: I'm your mom, and too bad if ur poor\nCreator/作者: Sichengthebest"%(ppl[index]))
    else:
        update.message.reply_text("%s: Bruh I need money why would you want some from me\nCreator/作者: Sichengthebest"%(ppl[index]))
    gametimes[user] = datetime.now() + timedelta(seconds=45)

def get_command():
    return [BotCommand('beg','Go beg, peasant // 去讨钱吧，穷人')]

def add_handler(dispatcher):
    dispatcher.add_handler(CommandHandler('beg',beg))

        