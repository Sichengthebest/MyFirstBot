import config
import random
import fish
import hunt
from datetime import datetime,timedelta
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand

# {
#   uid : {
#       'coins': 123,
#       'hourlytime' : time
#       'dailytime' : time
#       'weeklytime' : time
#       'yearlytime' : time
#       'hp' : 56
#       'items' : ["herring","trout","shark","boar","fox","deer","skunk","basilisk"]
#       'bank' : 456
#       'bankspace' : 458
#       'total' : 579
#       }
# }

coins = config.CONFIG["coins"]

def save():
    config.CONFIG["coins"] = coins
    config.save_config()

def check_user(user):
    uid = str(user.id)
    if not uid in coins.keys():
        coins[uid] = {'name':user.first_name,'coins':0,'yearlytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'weeklytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'dailytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'hourlytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'hp':100,'items':[],'bank':0,'bankspace':1000,'total':0}
        save()

def check_hp(user):
    check_user(user)
    uid = str(user.id)
    if coins[uid]['hp'] == 0:
        coins[uid]['total'] -= coins[uid]['coins']
        coins[uid]['coins'] = 0
        coins[uid]['hp'] = 100
        save()

def show_user(user):
    uid = str(user.id)
    check_user(user)
    return f"""{coins[uid]['name']}'s Balance:
In wallet: {coins[uid]['coins']} GP
In bank: {coins[uid]['bank']} GP / {coins[uid]['bankspace']} total bank space
Total: {coins[uid]['total']} GP
You have {coins[uid]['hp']} HP
---------------------------------------
{coins[uid]['name']} 的金钱数额： 
钱包：{coins[uid]['coins']} GP
银行：{coins[uid]['bank']} GP / {coins[uid]['bankspace']} 总银行空间
总额：{coins[uid]['total']} GP
你有 {coins[uid]['hp']} HP"""

def add_coins(user,c):
    check_user(user)
    uid = str(user.id)
    coins[uid]['coins'] += c
    if c > 0:
        coins[uid]['bankspace'] += int(c/5)
    coins[uid]['total'] += c
    save()

def add_item(user,c,times):
    check_user(user)
    uid = str(user.id)
    for _i in range(0,times):
        coins[uid]['items'].append("%s"%c)
    save()

def add_hp(user,c):
    check_user(user)
    uid = str(user.id)
    if c == -100:
        if not "lifesaver" in coins[uid]['items']:
            coins[uid]['hp'] = 0
            check_hp(user)
        else:
            coins[uid]['items'].remove("lifesaver")
    else:
        coins[uid]['hp'] += c
        check_hp(user)
    save()

def hourly(update,context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    hourlytime = datetime.strptime(coins[uid]['hourlytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() > hourlytime:
        c = random.randint(50,200)
        add_coins(user,c)
        hourlytime = datetime.now() + timedelta(hours=1)
        update.message.reply_text("Here are your hourly coins, %s\n%s coins were placed in your wallet.\n这是您的每小时打卡的金币，%s \n%s GP已被放置在您的钱包中。"%(user.first_name,c,user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one hour hasn't passed yet!\n放慢速度，呆瓜！我不是用钱做的，小家伙，一个小时还没有过去！")
    coins[uid]['hourlytime'] = hourlytime.strftime("%Y/%m/%d %H:%M:%S")
    save()

def daily(update,context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    dailytime = datetime.strptime(coins[uid]['dailytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() > dailytime:
        c = random.randint(500,2000)
        add_coins(user,c)
        dailytime = datetime.now() + timedelta(days=1)
        banknote = random.choice(["True","False"])
        if banknote == "True":
            coins[uid]['items'].append("banknote")
            update.message.reply_text("Here are your daily coins, %s\n%s coins were placed in your wallet.\nOh? And Gringotts offered you a free banknote to store your cash!\n这是您的每天打卡的金币，%s\n%s GP已被放置在您的钱包中。\n哦？古灵阁为您提供了免费的钞票来存储您的现金！"%(user.first_name,c,user.first_name,c))
        else:
            update.message.reply_text("Here are your daily coins, %s\n%s coins were placed in your wallet.\n这是您的每天打卡的金币，%s\n%s GP已被放置在您的钱包中。"%(user.first_name,c,user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one day hasn't passed yet!\n放慢速度，呆瓜！我不是用钱做的，小家伙，一天还没有过去！")
    coins[uid]['dailytime'] = dailytime.strftime("%Y/%m/%d %H:%M:%S")    
    save()

def weekly(update,context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    hourlytime = datetime.strptime(coins[uid]['weeklytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() > hourlytime:
        c = random.randint(2000,5000)
        fc = random.randint(20,50)
        bc = random.randint(15,60)
        add_coins(user,c)
        hunt.huntgame[uid]['bcoins'] += bc
        fish.fishgame[uid]['fcoins'] += fc
        hourlytime = datetime.now() + timedelta(days=7)
        update.message.reply_text("Here are your weekly coins, %s\n%s coins were placed in your wallet.\nYou also got %s huntcoins and %s fishcoins!\n这是您的每小时打卡的金币，%s \n%s GP已被放置在您的钱包中。\n您也得到了%s兽币和%s鱼币！"%(user.first_name,c,bc,fc,user.first_name,c,bc,fc))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one week hasn't passed yet!\n放慢速度，呆瓜！我不是用钱做的，小家伙，一个星期还没有过去！")
    coins[uid]['weeklytime'] = hourlytime.strftime("%Y/%m/%d %H:%M:%S")
    save()

def yearly(update,context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    hourlytime = datetime.strptime(coins[uid]['yearlytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() > hourlytime:
        c = 1
        add_coins(user,c)
        hourlytime = datetime.now() + timedelta(weeks=52)
        update.message.reply_text("Here are your yearly coins, %s\n%s GP was placed in your wallet. Didn't you expect more?\n这是您的每年打卡的金币，%s \n%s GP已被放置在您的钱包中。你没期待更多吗？"%(user.first_name,c,user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, maybe you do hate 2020, but New Year did not pass yet!\n放慢速度，呆瓜！我不是用钱做的，也许您确实讨厌2020年，但新年还没有过去！")
    coins[uid]['yearlytime'] = hourlytime.strftime("%Y/%m/%d %H:%M:%S")
    save()

def banknote(update, context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    if "banknote" in coins[uid]['items']:
        coins[uid]['bankspace'] += 1000
        coins[uid]['items'].remove("banknote")
        update.message.reply_text("Success! You now have %s GP of storage in your bank!\n成功！您现在在银行中拥有%s GP的存储空间！"%(coins[uid]['bankspace'],coins[uid]['bankspace']))
    else:
        update.message.reply_text("You do not own a banknote lol\nYou can buy a banknote at the /shop\n您没有钞票哈哈哈\n您可以在 /shop 中购买钞票")

def eat(update, context):
    user = update.effective_user
    check_user(user)
    if len(context.args) == 0:
        update.message.reply_text("""Enjoy your meal! What are you eating tho?
/eat apple for a nice juicy red apple.
Gain 10 HP.
/eat brocoli for some ugly green miniature trees.
Gain 20 HP.
/eat ramen to enjoy some delicious noodles in soup.
Gain 35 HP.
/eat simp to drink Several Snap's new potion.
Gain 50 HP.
/eat herring to eat herring that you caught.
Gain 5 HP.
/eat trout to eat trout that you caught.
Gain 30 HP.
/eat shark to eat sharks that you caught.
Gain 60 HP.
/eat skunk to eat STINKY skunk that you caught.
Gain 20 HP.
/eat deer to eat deer that you caught.
Gain 20 HP.
/eat fox to eat fox that you caught.
Gain 30 HP.
/eat rhino to eat rhinoceros that you caught.
Gain 45 HP.
/eat basilisk to eat basilisk that you caught.
Gain 69 HP.
------------------------------
请享用！但是你在吃什么？
/eat apple 来吃一个好吃的红苹果。
获得10HP。
/eat brocoli 来吃西兰花，一些丑陋的绿色微型树木。
获得20HP。
/eat ramen 来吃拉面，享受汤中的美味的面条。
获得35HP。
/eat simp 来喝一点斯纳普的新药水。
获得50HP。
/eat herring 来吃掉你抓到的鲱鱼。
获得5HP。
/eat trout 来吃掉你抓到的鳟鱼。
获得30HP。
/eat shark 来吃掉你抓到的鲨鱼。
获得60HP。
/eat skunk 来吃掉您抓到的臭臭鼬。
获得20HP。
/eat deer 来吃掉你抓到的鹿。
获得20HP。
/eat fox 来吃掉你抓到的狐狸。
获得30HP。
/eat rhino 来吃您抓到的犀牛。
获得45HP。
/eat basilisk 来吃你抓到的蛇怪。
获得69HP。""")
    elif context.args[0] == "apple":
        update.message.reply_text("%s"%eat_stuff(user,"apple",10))
    elif context.args[0] == "brocoli":
        update.message.reply_text("%s"%eat_stuff(user,"brocoli",20))
    elif context.args[0] == "ramen":
        update.message.reply_text("%s"%eat_stuff(user,"ramen",35))
    elif context.args[0] == "simp":
        update.message.reply_text("%s"%eat_stuff(user,"simp",50))
    elif context.args[0] == "herring":
        update.message.reply_text("%s"%eat_stuff(user,"herring",5))
    elif context.args[0] == "trout":
        update.message.reply_text("%s"%eat_stuff(user,"trout",30))
    elif context.args[0] == "shark":
        update.message.reply_text("%s"%eat_stuff(user,"shark",60))
    elif context.args[0] == "skunk":
        update.message.reply_text("%s"%eat_stuff(user,"skunk",20))
    elif context.args[0] == "deer":
        update.message.reply_text("%s"%eat_stuff(user,"deer",20))
    elif context.args[0] == "fox":
        update.message.reply_text("%s"%eat_stuff(user,"fox",30))
    elif context.args[0] == "rhino":
        update.message.reply_text("%s"%eat_stuff(user,"rhino",45))
    elif context.args[0] == "basilisk":
        update.message.reply_text("%s"%eat_stuff(user,"basilisk",69))
    else:
        update.message.reply_text("Bruh the thing you want to eat is not edible!\n您要吃的东西不能食用！")
        
def eat_stuff(user,aliment,c):
    uid = str(user.id)
    hpmax = 100 - c
    if aliment in coins[uid]['items']:
        if coins[uid]['hp'] < hpmax:
            coins[uid]['items'].remove("%s"%aliment)
            coins[uid]['hp'] += c
        elif coins[uid]['hp'] >= hpmax and coins[uid]['hp'] < 100:
            coins[uid]['items'].remove("%s"%aliment)
            coins[uid]['hp'] = 100
        elif coins[uid]['hp'] >= 100:
            return "Bruh your HP is maxed out, try losing some."
        save()
        return "You ate/drank a/an/some %s! Gain %sHP."%(aliment,c)
    else:
        return "You do not own this item lol" 

def convert(update,context):
    user = update.effective_user
    uid = user.id
    if len(context.args) == 0:
        update.message.reply_animation('https://thumbs.gfycat.com/AliveWelloffAtlanticspadefish-max-1mb.gif',caption="""What are you about to convert?
/convert gptofc {amount of GP} : Convert 5 GP into 1 fishcoin!
/convert gptobc {amount of GP} : Convert 5 GP into 1 beastcoin!
/convert fctobc {amount of fishcoins} : Convert 1 fishcoin into 1 beastcoin!
/convert bctofc {amount of beastcoins} : Convert 1 beastcoin into 1 fishcoin!
/convert fctogp {amount of fishcoins} : Convert 1 fishcoin into 5 GP!
/convert bctogp {amount of beastcoins} : Convert 1 beastcoin into 5 GP!
------------------------------------------
/convert gptofc {GP的数量}：将5 GP转换为1鱼币！
/convert gptobc {GP的数量}：将5 GP转换为1兽币！
/convert fctobc {鱼币的数量}：将1鱼币转换为1兽币！
/convert bctofc {兽币的数量}：将1兽币转换为1鱼币！
/convert fctogp {鱼币的数量}：将1鱼币转换为5GP！
/convert bctogp {兽币的数量}：将1兽币转换为5GP！""")
    if len(context.args) == 1:
        update.message.reply_text("You need to enter a valid amount!\n您需要输入有效的数量！")
        return
    if context.args[1].isdigit():
        if context.args[0] == "gptofc":
            if int(context.args[1]) > coins[str(uid)]['coins']:
                update.message.reply_text("Ur too poor u can't convert that many GP\n您太穷了，您无法兑换那么多GP")
            elif int(context.args[1]) <= 0 or int(context.args[1]) % 5 != 0:
                update.message.reply_text("You need to enter a valid amount that can be divisible by 5!\n您需要输入一个可以被5整除的有效数量！")
            else:
                add_coins(user,-(int(context.args[1])))
                fish.fishgame[str(uid)]['fcoins'] += int(int(context.args[1]) / 5)
                update.message.reply_text("Success! You now have %s GP and %s fishcoins!"%(coins[str(uid)]['coins'],fish.fishgame[str(uid)]['fcoins']))
        elif context.args[0] == "gptobc":
            if int(context.args[1]) > coins[str(uid)]['coins']:
                update.message.reply_text("Ur too poor u can't convert that many GP\n您太穷了，您无法兑换那么多GP")
            elif int(context.args[1]) <= 0 or int(context.args[1]) % 5 != 0:
                update.message.reply_text("You need to enter a valid amount that can be divisible by 5!\n您需要输入一个可以被5整除的有效数量！")
            else:
                add_coins(user,-(int(context.args[1])))
                hunt.huntgame[str(uid)]['bcoins'] += int(int(context.args[1]) / 5)
                update.message.reply_text("Success! You now have %s GP and %s beastcoins!"%(coins[str(uid)]['coins'],hunt.huntgame[str(uid)]['bcoins']))
        elif context.args[0] == "fctobc":
            if int(context.args[1]) > fish.fishgame[str(uid)]['fcoins']:
                update.message.reply_text("Ur too poor u can't convert that many fishcoins\n您太穷了，您无法兑换那么多鱼币")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount\n您需要输入有效的数量")
            else:
                fish.fishgame[str(uid)]['fcoins'] -= int(context.args[1])
                hunt.huntgame[str(uid)]['bcoins'] += int(context.args[1])
                update.message.reply_text("Success! You now have %s fishcoins and %s beastcoins!"%(fish.fishgame[str(uid)]['fcoins'],hunt.huntgame[str(uid)]['bcoins']))
        elif context.args[0] == "bctofc":
            if int(context.args[1]) > hunt.huntgame[str(uid)]['bcoins']:
                update.message.reply_text("Ur too poor u can't convert that many beastcoins\n您太穷了，您无法兑换那么多兽币")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount\n您需要输入有效的数量")
            else:
                fish.fishgame[str(uid)]['fcoins'] += int(context.args[1])
                hunt.huntgame[str(uid)]['bcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s fishcoins and %s beastcoins!"%(fish.fishgame[str(uid)]['fcoins'],hunt.huntgame[str(uid)]['bcoins']))
        elif context.args[0] == "fctogp":
            if int(context.args[1]) > fish.fishgame[str(uid)]['fcoins']:
                update.message.reply_text("Ur too poor u can't convert that many fishcoins\n您太穷了，您无法兑换那么多鱼币")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount\n您需要输入有效的数量")
            else:
                add_coins(user,int(int(context.args[1]) * 5))
                fish.fishgame[str(uid)]['fcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s GP and %s fishcoins!"%(coins[str(uid)]['coins'],fish.fishgame[str(uid)]['fcoins']))
        elif context.args[0] == "bctogp":
            if int(context.args[1]) > hunt.huntgame[str(uid)]['bcoins']:
                update.message.reply_text("Ur too poor u can't convert that many beastcoins\n您太穷了，您无法兑换那么多兽币")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount\n您需要输入有效的数量")
            else:
                add_coins(user,int(int(context.args[1]) * 5))
                hunt.huntgame[str(uid)]['bcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s GP and %s beastcoins!"%(coins[str(uid)]['coins'],hunt.huntgame[str(uid)]['bcoins']))
        else:
            update.message.reply_text("You need to enter a valid conversion!\n您需要输入有效的换算！")
    else:
        update.message.reply_text("You need to enter a valid amount!\n您需要输入有效的数量！")
    save()

def dep(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_user(user)
    remspace = coins[uid]['bankspace'] - coins[uid]['bank']
    if len(context.args) == 0:
        update.message.reply_text("What are you depositing, idiot?")
    elif context.args[0].isdigit():
        num = int(context.args[0])
        if num > remspace :
            update.message.reply_text("Your argument should be no more the amount of storage left in your bank (%s)."%remspace)
        elif coins[uid]['coins'] < num:
            update.message.reply_text("Your argument should be either a number and no more than what you have in your wallet (%s)."%coins[uid]['coins'])
        else:
            coins[uid]['coins'] -= num
            coins[uid]['bank'] += num
            update.message.reply_text("Success! You have deposited %s GP and now have %s GP in your wallet and %s GP in your bank."%(num,coins[uid]['coins'],coins[uid]['bank']))
    else:
        if context.args[0] == "all":
            if remspace == 0:
                update.message.reply_text("Looks like you already have a full bank kiddo")
            else:
                if coins[uid]['coins'] <= 0:
                    update.message.reply_text("Looks like you have no money dude")
                    return
                if remspace > coins[uid]['coins']:
                    coins[uid]['bank'] += coins[uid]['coins']
                    coins[uid]['coins'] = 0
                elif remspace <= coins[uid]['coins']:
                    coins[uid]['coins'] -= remspace
                    coins[uid]['bank'] += remspace
                update.message.reply_text("Success! You now have %s GP in your wallet and %s GP in your bank."%(coins[uid]['coins'],coins[uid]['bank']))
        else:
            update.message.reply_text("Your argument should be a number, or /dep all , dumdum") 
    save()

def withdraw(update, context):
    user = update.effective_user
    uid = str(user.id)
    check_user(user)
    if len(context.args) == 0:
        update.message.reply_text("What are you withdrawing, idiot?")
    elif context.args[0].isdigit():
        num = int(context.args[0])
        if num > coins[uid]['bank'] :
            update.message.reply_text("Your argument should be no more the amount of GP in your bank (%s)."%coins[uid]['bank'])
        else:
            coins[uid]['coins'] += num
            coins[uid]['bank'] -= num
            update.message.reply_text("Success! You have withdrawn %s GP and now have %s GP in your wallet and %s GP in your bank."%(num,coins[uid]['coins'],coins[uid]['bank']))
    else:
        if context.args[0] == "all":
            if coins[uid]['bank'] == 0:
                update.message.reply_text("Looks like you already have an empty bank kiddo")
            else:
                coins[uid]['coins'] += coins[uid]['bank']
                coins[uid]['bank'] = 0
                update.message.reply_text("Success! You now have %s GP in your wallet and %s GP in your bank."%(coins[uid]['coins'],coins[uid]['bank']))
        else:
            update.message.reply_text("Your argument should be a number, or /withdraw all , dumdum") 
    save()

def get_coins(update, context):
    user = update.effective_user
    check_user(user)
    update.message.reply_animation('https://media4.giphy.com/media/3Z1basZxa2mGOSPBzR/200_d.gif',caption=f"{show_user(user)}")

def get_command():
    return [
        BotCommand('bal','Check the amount of money you have. // 检查您有多少GP。'),
        BotCommand('daily','Get daily GP! // 每日打卡！'),
        BotCommand('hourly','Get hourly GP! // 每小时打卡！'),
        BotCommand('weekly','Get weekly GP! // 每星期打卡！'),
        BotCommand('yearly','Get yearly GP! // 每年打卡！'),
        BotCommand('eat','Eat to gain HP // 吃东西来增加HP'),
        BotCommand('convert','Convert one currency into another! // 将一种货币转换为另一种货币！'),
        BotCommand('dep','Deposit money from your wallet to your bank! // 从钱包里存钱到银行！'),
        BotCommand('banknote','Increase the amount of GP you can stuff into your bank! // 增加您可以存入银行的GP数量！'),
        BotCommand('withdraw','Withdraw money from your bank to your wallet! // 从银行提款！')
    ]

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('bal', get_coins))
    dp.add_handler(CommandHandler('daily', daily))
    dp.add_handler(CommandHandler('hourly', hourly))
    dp.add_handler(CommandHandler('weekly', weekly))
    dp.add_handler(CommandHandler('yearly', yearly))
    dp.add_handler(CommandHandler('eat', eat))
    dp.add_handler(CommandHandler('convert', convert))
    dp.add_handler(CommandHandler('dep', dep))
    dp.add_handler(CommandHandler('banknote', banknote))
    dp.add_handler(CommandHandler('withdraw', withdraw))