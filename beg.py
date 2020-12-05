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
    ppl = ["BOTGOD","@TheRandomDudeHimself","Brad Pitt","A Discord mod","A Random Orange Dude","Joe","Bob","Spongebob","The Red Dude In Among Us","Ur mom","Meryl Streep","Google Translate","A Homeless Man","@dankpbot"]
    pplCH = ["BOTGOD","@TheRandomDudeHimself","布拉德·皮特","一个Discord管理员","唐纳德·特朗普","乔","鲍勃","海绵宝宝","《我们之中》红色的家伙","你老妈","梅丽尔·斯特里普","谷歌翻译","一个无家可归的人","@dankpbot"]
    badstuff = ["Sorry I used all my money to fund the Pfizer vaccine","Sorry I used all my money to fund the Moderna vaccine","Stop begging","NO","NO","Of course not","Oh dang I forgot my purse","Let me think...NO","Yes...maybe...nvr mind","NEVER","Nah","I used all my money to fund the Biden campaign","I donated too much to @ZahJmPvjo3Hjz6CDNceG","Sorry I have no more money cuz I bought 10,000 rolls of toilet paper at the start of the pandemic"]
    badstuffCH = ["对不起，我用我所有的钱来资助辉瑞疫苗了","对不起，我用我的所有钱来资助Moderna疫苗了","快停止乞求","不","不","当然不","哦不，我忘记了钱包","让我想想...不","好...也许...算了吧","从不","不","我用我所有的钱来资助拜登竞选活动了","我对@ZahJmPvjo3Hjz6CDNceG捐赠过多了","对不起，我没有更多的钱，因为在疫情开始时我买了10,000卷厕所纸"]

    index = random.randint(0,13)
    yesorno = random.randint(1,2)
    user = update.effective_user
    get_users(user)
    t = datetime.now()
    if t < gametimes[user]:
        update.message.reply_text("Slow it down, cmon!!! Stop begging so much, it makes you look like a little baby.\n放慢速度，呆瓜！！！别再乞讨了，这会让你看起来像个小婴儿。\nCreator/作者: Sichengthebest")
        return
    if index == 0:
        rwbotgod = random.randint(10,250)
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s donated %s GP to you!\n%s 给了你 %s GP!\nCreator/作者: Sichengthebest"%(ppl[index],rwbotgod,pplCH[index],rwbotgod))
        coins.add_coins(user,rwbotgod)
    elif index == 1:
        rwsicheng = random.randint(50,400)
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s donated %s GP to you!\n%s 给了你 %s GP!\nCreator/作者: Sichengthebest"%(ppl[index],rwsicheng,pplCH[index],rwsicheng))
        coins.add_coins(user,rwsicheng)
    elif index == 2 or index == 3 or index == 5 or index == 6 or index == 7 or index == 10 or index == 11:
        if yesorno == 1:
            rwbrad = random.randint(10,100)
            update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s donated %s GP to you!\n%s 给了你 %s GP!\nCreator/作者: Sichengthebest"%(ppl[index],rwbrad,pplCH[index],rwbrad))
            coins.add_coins(user,rwbrad)
        else:
            update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: %s\n%s: %s\nCreator/作者: Sichengthebest"%(ppl[index],badstuff[index],pplCH[index],badstuffCH[index]))
    elif index == 4:
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: STOP THE STEAL! STOP THE STEAL! STOP THE STEAL!\n%s: 停止窃取！停止窃取！停止窃取！\nCreator/作者: Sichengthebest"%(ppl[index],pplCH[index]))
    elif index == 8:
        amongus = ["Ur sus","You died","Shut up and go fix the wiring in Electrical"]
        amongusCH = ["我怀疑你","你死了","闭嘴然后去修修电站的电线"]
        auindex = random.randint(0,2)
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: %s\n%s: %s\nCreator/作者: Sichengthebest"%(ppl[index],amongus[auindex],pplCH[index],amongusCH[auindex]))
        if auindex == 1:
            coins.add_hp(user,-100)
    elif index == 9:
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: I'm your mom, and too bad if ur poor\n%s: 我是你老妈，如果你穷，那就太可惜了\nCreator/作者: Sichengthebest"%(ppl[index],pplCH[index]))
    elif index == 12:
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: Bruh I need money why would you want some from me\n%s: 你真noah，我需要钱，为什么你还要找我\nCreator/作者: Sichengthebest"%(ppl[index],pplCH[index]))
    elif index == 13:
        update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif',caption="%s: No cuz I'm evil\n%s: 不，因为我很坏\nCreator/作者: Sichengthebest"%(ppl[index],pplCH[index]))
    gametimes[user] = datetime.now() + timedelta(seconds=45)
    

def get_command():
    return [BotCommand('beg','Go beg, peasant // 去讨钱吧，穷人')]

def add_handler(dispatcher):
    dispatcher.add_handler(CommandHandler('beg',beg))