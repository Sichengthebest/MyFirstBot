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
#       'dailytime' : time
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
        coins[uid] = {'name':user.first_name,'coins':0,'dailytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'hourlytime':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'hp':100,'items':[],'bank':0,'bankspace':1000,'total':0}
        save()

def check_hp(user):
    check_user(user)
    uid = str(user.id)
    if coins[uid]['hp'] == 0:
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
        update.message.reply_text("Here are your hourly coins, %s\n%s coins were placed in your wallet."%(user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one hour hasn't passed yet!")
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
        dailytime = datetime.now() + timedelta(hours=24)
        update.message.reply_text("Here are your daily coins, %s\n%s coins were placed in your wallet."%(user.first_name,c))
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one day hasn't passed yet!")
    coins[uid]['dailytime'] = dailytime.strftime("%Y/%m/%d %H:%M:%S")    
    save()

def shop(update, context):
    user = update.effective_user
    check_user(user)
    markets = ["Walmart","Costco","Super C","Central Supermarket+"]
    if len(context.args) == 0:
        update.message.reply_text("""Here are some stuff you can buy at %s.
FOOD:
--------------------------------------
Buy apples! 🍎:
Description: An apple a day keeps the doctors away! When you eat one, gain 10HP!
500GP per 🍎
/shop apple
--------------------------------------
Buy brocolis! 🥦:
Description: Eat your vegetables, it's actually good for you, you can gain 20HP!
900GP per 🥦
/shop brocoli
--------------------------------------
Buy ramen! 🍜:
Description: Good hot ramen is great for your health! You can gain 35HP per bowl!
1500GP per 🍜
/shop ramen
--------------------------------------
Buy Super Interesting Magic Potions! 🍾:
Description: Several Snap has developed a new potion that actually doesn't kill you! Instead, it makes you gain 50HP!
2000GP per 🍾
/shop simp
--------------------------------------
TOOLS:
--------------------------------------
Buy lifesavers! 💖:
Description: When you accidentally chug down some Clorox or blindly enter the Chamber of Secrets, have no fear, the lifesaver is here! You can avoid death (and avoid losing all your coins in your wallet)
3000GP per 💖
/shop lifesaver
--------------------------------------
Buy banknotes! 💸:
Description: When your account in Gringotts can't handle the flow of coins, you can use the banknote to increase the amount of coins that you can stuff into it (1000 GP).
1800GP per 💸
/shop banknote
_______________________________________

您可以在%s购买一些东西。
餐饮：
--------------------------------------
买苹果！ 🍎：
描述：每天一个苹果能让健康顶呱呱！当您吃一个时，获得10HP！
每GP 500GP
/shop apple
--------------------------------------
买西兰花！ 🥦：
描述：多吃蔬菜，实际上对您有好处，您可以获得20HP！
每磅900GP
/shop brocoli
--------------------------------------
买拉面！ 🍜：
描述：好的热拉面对您的健康有益！每碗可获得35HP！
每🍜1500GP
/shop ramen
--------------------------------------
购买超级有趣的魔药！ 🍾：
描述：西弗勒·斯纳普开发了一种新药水，实际上它并不会杀死您！相反，它使您获得50HP！
每磅2000GP
/shop simp
--------------------------------------
工具：
--------------------------------------
购买救生器！ 💖：
描述：当您不小心喝掉一些高乐氏或盲目的进入密室时，不用担心，救生器就在这里！您可以避免死亡（并避免丢失钱包中的所有GP）
每💖3000GP
/shop lifesaver
--------------------------------------
买钞票！ 💸：
描述：当您的古灵阁帐户无法处理您过多的钱时，可以使用钞票增加可放入其中的硬币数量（1000 GP）。
每💸1800GP
/shop banknote
"""%(random.choice(markets),random.choice(markets)))
    elif context.args[0] == "apple":
        update.message.reply_text("%s"%buy_stuff(user,"apple",500))
    elif context.args[0] == "brocoli":
        update.message.reply_text("%s"%buy_stuff(user,"brocoli",900))
    elif context.args[0] == "ramen":
        update.message.reply_text("%s"%buy_stuff(user,"ramen",1500))
    elif context.args[0] == "simp":
        update.message.reply_text("%s"%buy_stuff(user,"simp",2000))
    elif context.args[0] == "lifesaver":
        update.message.reply_text("%s"%buy_stuff(user,"lifesaver",3000))
    elif context.args[0] == "banknote":
        update.message.reply_text("%s"%buy_stuff(user,"banknote",1800))
    else:
        update.message.reply_text("Bruh this item doesn't even exist")

def banknote(update, context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    if "banknote" in coins[uid]['items']:
        coins[uid]['bankspace'] += 1000
        coins[uid]['items'].remove("banknote")
        update.message.reply_text("Success! You now have %s GP of storage in your bank!"%coins[uid]['bankspace'])
    else:
        update.message.reply_text("You do not own a banknote lol\nYou can buty a banknote at the /shop")

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
    elif context.args[0] == "rhino":
        update.message.reply_text("%s"%eat_stuff(user,"rhino",45))
    elif context.args[0] == "basilisk":
        update.message.reply_text("%s"%eat_stuff(user,"basilisk",69))
    else:
        update.message.reply_text("Bruh the thing you want to eat is not edible!")
        
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

def show_items(update,context):
    user = update.effective_user
    check_user(user)
    uid = str(user.id)
    update.message.reply_text("%s"%coins[uid]['items'])

def buy_stuff(user,object,c):
    uid = str(user.id)
    if coins[uid]['coins'] < c:
        return "No disrespect but... LMFAO ur so poor u need %s more GP "%(c-coins[uid]['coins'])
    coins[uid]['items'].append(object)
    coins[uid]['coins'] -= c
    coins[uid]['total'] -= c
    save()
    return "Success! You have bought a/an/some %s! You still have %s GP."%(object,coins[uid]['coins'])

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
    elif context.args[0] == "gptofc":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > coins[str(uid)]['coins']:
                update.message.reply_text("Ur too poor u can't convert that many GP")
            elif int(context.args[1]) <= 0 or int(context.args[1]) % 5 != 0:
                update.message.reply_text("You need to enter a valid amount that can be divisible by 5!")
            else:
                add_coins(user,-(int(context.args[1])))
                fish.fishgame[str(uid)]['fcoins'] += int(int(context.args[1]) / 5)
                update.message.reply_text("Success! You now have %s GP and %s fishcoins!"%(coins[str(uid)]['coins'],fish.fishgame[str(uid)]['fcoins']))
        else:
            update.message.reply_text("You need to enter a valid amount!")
    elif context.args[0] == "gptobc":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > coins[str(uid)]['coins']:
                update.message.reply_text("Ur too poor u can't convert that many GP")
            elif int(context.args[1]) <= 0 or int(context.args[1]) % 5 != 0:
                update.message.reply_text("You need to enter a valid amount that can be divisible by 5!")
            else:
                add_coins(user,-(int(context.args[1])))
                hunt.huntgame[str(uid)]['bcoins'] += int(int(context.args[1]) / 5)
                update.message.reply_text("Success! You now have %s GP and %s beastcoins!"%(coins[str(uid)]['coins'],hunt.huntgame[str(uid)]['bcoins']))
    elif context.args[0] == "fctobc":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > fish.fishgame[str(uid)]['fcoins']:
                update.message.reply_text("Ur too poor u can't convert that many fishcoins")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount")
            else:
                fish.fishgame[str(uid)]['fcoins'] -= int(context.args[1])
                hunt.huntgame[str(uid)]['bcoins'] += int(context.args[1])
                update.message.reply_text("Success! You now have %s fishcoins and %s beastcoins!"%(fish.fishgame[str(uid)]['fcoins'],hunt.huntgame[str(uid)]['bcoins']))
        else:
            update.message.reply_text("You need to enter a valid amount!")
    elif context.args[0] == "bctofc":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > hunt.huntgame[str(uid)]['bcoins']:
                update.message.reply_text("Ur too poor u can't convert that many beastcoins")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount")
            else:
                fish.fishgame[str(uid)]['fcoins'] += int(context.args[1])
                hunt.huntgame[str(uid)]['bcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s fishcoins and %s beastcoins!"%(fish.fishgame[str(uid)]['fcoins'],hunt.huntgame[str(uid)]['bcoins']))
        else:
            update.message.reply_text("You need to enter a valid amount!")
    elif context.args[0] == "fctogp":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > fish.fishgame[str(uid)]['fcoins']:
                update.message.reply_text("Ur too poor u can't convert that many fishcoins")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount")
            else:
                add_coins(user,int(int(context.args[1]) * 5))
                fish.fishgame[str(uid)]['fcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s GP and %s fishcoins!"%(coins[str(uid)]['coins'],fish.fishgame[str(uid)]['fcoins']))
        else:
            update.message.reply_text("You need to enter a valid amount!")
    elif context.args[0] == "bctogp":
        if len(context.args) == 1:
            update.message.reply_text("You need to enter a valid amount!")
        elif context.args[1].isdigit():
            if int(context.args[1]) > hunt.huntgame[str(uid)]['bcoins']:
                update.message.reply_text("Ur too poor u can't convert that many fishcoins")
            elif int(context.args[1]) <= 0:
                update.message.reply_text("You need to enter a valid amount")
            else:
                add_coins(user,int(int(context.args[1]) * 5))
                hunt.huntgame[str(uid)]['bcoins'] -= int(context.args[1])
                update.message.reply_text("Success! You now have %s GP and %s beastcoins!"%(coins[str(uid)]['coins'],hunt.huntgame[str(uid)]['bcoins']))
        else:
            update.message.reply_text("You need to enter a valid amount!")
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
                if remspace > coins[uid]['coins']:
                    coins[uid]['bank'] += coins[uid]['coins']
                    coins[uid]['coins'] = 0
                    update.message.reply_text("Success! You have deposited %s GP and now have %s GP in your wallet and %s GP in your bank."%(coins[uid]['coins'],coins[uid]['coins'],coins[uid]['bank']))
                elif remspace <= coins[uid]['coins']:
                    coins[uid]['coins'] -= remspace
                    coins[uid]['bank'] += remspace
                    update.message.reply_text("Success! You have deposited %s GP and now have %s GP in your wallet and %s GP in your bank."%(remspace,coins[uid]['coins'],coins[uid]['bank']))
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
        BotCommand('shop',' Buy nice useful stuff! // 购买有用的东西！'),
        BotCommand('eat','Eat to gain HP // 吃东西来增加HP'),
        BotCommand('inv','[BETA] Check the items you have in your inventory. // [测试] 检查库存中的物品。'),
        BotCommand('convert','Convert one currency into another! // 将一种货币转换为另一种货币！'),
        BotCommand('dep','Deposit money from your wallet to your bank! // 从钱包里存钱到银行！'),
        BotCommand('banknote','Increase the amount of GP you can stuff into your bank! // 增加您可以存入银行的GP数量！'),
        BotCommand('withdraw','Withdraw money from your bank to your wallet! // 从银行提款！')
    ]

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('bal', get_coins))
    dp.add_handler(CommandHandler('daily', daily))
    dp.add_handler(CommandHandler('hourly', hourly))
    dp.add_handler(CommandHandler('shop', shop))
    dp.add_handler(CommandHandler('eat', eat))
    dp.add_handler(CommandHandler('inv', show_items))
    dp.add_handler(CommandHandler('convert', convert))
    dp.add_handler(CommandHandler('dep', dep))
    dp.add_handler(CommandHandler('banknote', banknote))
    dp.add_handler(CommandHandler('withdraw', withdraw))