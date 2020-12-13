import coins
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand

def buy(update, context):
    user = update.effective_user
    coins.check_user(user)
    if len(context.args) == 0:
        update.message.reply_text("""Here are some stuff you can buy at the shop.
FOOD:
--------------------------------------
Buy apples! 🍎:
Description: An apple a day keeps the doctors away! When you eat one, gain 10HP!
500GP per 🍎
/buy apple
--------------------------------------
Buy brocolis! 🥦:
Description: Eat your vegetables, it's actually good for you, you can gain 20HP!
900GP per 🥦
/buy brocoli
--------------------------------------
Buy ramen! 🍜:
Description: Good hot ramen is great for your health! You can gain 35HP per bowl!
1500GP per 🍜
/buy ramen
--------------------------------------
Buy Super Interesting Magic Potions! 🍾:
Description: Several Snap has developed a new potion that actually doesn't kill you! Instead, it makes you gain 50HP!
2000GP per 🍾
/buy simp
--------------------------------------
TOOLS:
--------------------------------------
Buy lifesavers! 💖:
Description: When you accidentally chug down some Clorox or blindly enter the Chamber of Secrets, have no fear, the lifesaver is here! You can avoid death (and avoid losing all your coins in your wallet)
3000GP per 💖
/buy lifesaver
--------------------------------------
Buy banknotes! 💸:
Description: When your account in Gringotts can't handle the flow of coins, you can use the banknote to increase the amount of coins that you can stuff into it (1000 GP).
1800GP per 💸
/buy banknote
_______________________________________

您可以在商店购买一些东西。
餐饮：
--------------------------------------
买苹果！🍎：
描述：每天一个苹果能让健康顶呱呱！当您吃一个时，获得10HP！
每🍎500GP
/buy apple
--------------------------------------
买西兰花！🥦：
描述：多吃蔬菜，实际上对您有好处，您可以获得20HP！
每🥦900GP
/buy brocoli
--------------------------------------
买拉面！🍜：
描述：好的热拉面对您的健康有益！每碗可获得35HP！
每🍜1500GP
/buy ramen
--------------------------------------
购买超级有趣的魔药！🍾：
描述：西弗勒·斯纳普开发了一种新药水，实际上它并不会杀死您！相反，它使您获得50HP！
每🍾2000GP
/buy simp
--------------------------------------
工具：
--------------------------------------
购买救生器！💖：
描述：当您不小心喝掉一些高乐氏或盲目的进入密室时，不用担心，救生器就在这里！您可以避免死亡（并避免丢失钱包中的所有GP）
每💖3000GP
/buy lifesaver
--------------------------------------
买钞票！ 💸：
描述：当您的古灵阁帐户无法处理您过多的钱时，可以使用钞票增加可放入其中的硬币数量（1000 GP）。
每💸1800GP
/buy banknote
""")
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
        update.message.reply_text("Bruh this item doesn't even exist\n这个东西根本不存在")

def buy_stuff(user,object,c):
    uid = str(user.id)
    if coins.coins[uid]['coins'] < c:
        return "No disrespect but... LMFAO ur so poor u need %s more GP\n没什么不尊重，但是...哈哈哈哈哈哈哈哈哈哈哈您如此贫穷，您需要多%s的GP"%(c-coins.coins[uid]['coins'],c-coins.coins[uid]['coins'])
    coins.coins[uid]['items'].append(object)
    coins.add_coins(user,-c)
    coins.save()
    return "Success! You have bought a/an/some %s! You still have %s GP.\n成功！您已经购买了一个/一些%s！您仍然有%sGP。"%(object,coins.coins[uid]['coins'],object,coins.coins[uid]['coins'])


def sell(update,context):
    user = update.effective_user
    coins.check_user(user)
    if len(context.args) == 0:
        update.message.reply_text("""Did you buy anything you do not need? Sell them to me at 2/3 of the original price!
Sell apples 🍎! 333 GP per 🍎
/sell apple
Sell brocolis 🥦! 600 GP per 🥦
/sell brocoli
Sell ramen 🍜! 1000 GP per 🍜
/sell ramen
Sell Super Interesting Magic Potions 🍾! 1333 GP per 🍾
/sell simp
Sell herring 🐟! 150 GP per 🐟
/sell herring
Sell trout 🎏! 800 GP per 🎏
/sell trout
Sell sharks 🦈! 1500 GP per 🦈
/sell shark
Sell skunks 🦨! 250 GP per 🦨
/sell skunk
Sell deers 🦌! 500 GP per 🦌
/sell deer
Sell foxes 🦊! 800 GP per 🦊
/sell fox
Sell rhinoceros 🦏! 1250 GP per 🦏
/sell rhino
Sell basilisk 🐍! 2000 GP per 🐍
/sell basilisk
Sell lifesavers 💖! 2000 GP per 💖
/sell lifesaver
Sell banknote 💸! 1200 GP per 💸
/sell banknote
-----------------------------
您是否购买了不需要的东西？以原始价格的2/3卖给我！
卖苹果🍎！每🍎333GP
/sell apple
卖西兰花！每🥦600GP
/sell brocoli
卖拉面🍜！每🍜1000GP
/sell ramen
卖超级有趣的魔药🍾！每🍾1333GP
/sell simp
卖鲱鱼🐟！每🐟150GP
/sell herring
卖鳟鱼🎏！每🎏800GP
/sell trout
卖鲨鱼🦈！每🦈1500GP
/sell shark
卖臭鼬🦨！每🦨250GP
/sell skunk
卖鹿🦌！每🦌500GP
/sell deer
卖狐狸🦊！每🦊800GP
/sell fox
卖犀牛🦏！每🦏1250GP
/sell rhino
卖蛇怪🐍！每🐍2000GP
/sell basilisk
卖救生器💖！每磅2000GP
/sell lifesaver
卖钞票💸！每💸1200GP
/sell banknote""")
    elif context.args[0] == "apple":
        update.messge.reply_text("%s"%sell_stuff(user,"apple",333))
    elif context.args[0] == "brocoli":
        update.message.reply_text("%s"%sell_stuff(user,"brocoli",600))
    elif context.args[0] == "ramen":
        update.message.reply_text("%s"%sell_stuff(user,"ramen",1000))
    elif context.args[0] == "simp":
        update.message.reply_text("%s"%sell_stuff(user,"simp",1333))
    elif context.args[0] == "herring":
        update.message.reply_text("%s"%sell_stuff(user,"herring",150))
    elif context.args[0] == "trout":
        update.message.reply_text("%s"%sell_stuff(user,"trout",800))
    elif context.args[0] == "shark":
        update.message.reply_text("%s"%sell_stuff(user,"shark",1500))
    elif context.args[0] == "skunk":
        update.message.reply_text("%s"%sell_stuff(user,"skunk",250))
    elif context.args[0] == "deer":
        update.message.reply_text("%s"%sell_stuff(user,"deer",500))
    elif context.args[0] == "fox":
        update.message.reply_text("%s"%sell_stuff(user,"fox",800))
    elif context.args[0] == "rhino":
        update.message.reply_text("%s"%sell_stuff(user,"rhino",1250))
    elif context.args[0] == "basilisk":
        update.message.reply_text("%s"%sell_stuff(user,"basilisk",2000))
    elif context.args[0] == "lifesaver":
        update.message.reply_text("%s"%sell_stuff(user,"lifesaver",2000))
    elif context.args[0] == "banknote":
        update.message.reply_text("%s"%sell_stuff(user,"banknote",1200))
    else:
        update.message.reply_text("Please choose something valid to sell!")

def sell_stuff(user,object,c):
    uid = str(user.id)
    if not object in coins.coins[uid]['items']:
        return "You do not own this item lol"
    else:
        coins.coins[uid]['items'].remove(object)
        coins.add_coins(user,c)
        coins.save()
        return "Success! You have sold a/an/some %s! You now have %s GP.\n成功！您已经卖了一个/一些%s！您现在有%sGP。"%(object,coins.coins[uid]['coins'],object,coins.coins[uid]['coins'])

def check_items(items):
    item_count = {}
    for i in items:
        if not i in item_count:
            item_count[i] = 0
        item_count[i] += 1
    return item_count   # {'herring':6,'trout':3}

liewu = {
    # 我是一个大笨蛋！！！
    'herring': 'Herrings // 鲱鱼 🐟 —— Sellable and edible // 可出售并可食用',
    'trout' : 'Trouts // 鳟鱼 🎏 —— Sellable and edible // 可出售并可食用',
    'shark' : 'Sharks // 鲨鱼 🦈 —— Sellable and edible // 可出售并可食用',
    'skunk' : 'Skunks // 臭鼬🦨 —— Sellable and edible // 可出售并可食用',
    'deer' : 'Deers // 鹿 🦌 —— Sellable and edible // 可出售并可食用',
    'fox' : 'Foxes // 狐狸 🦊 —— Sellable and edible // 可出售并可食用',
    'rhino' : 'Rhinoceros // 犀牛 🦏 —— Sellable and edible // 可出售并可食用',
    'basilisk' : 'Basilisks // 蛇怪 🐍 —— Sellable and edible // 可出售并可食用',
    'apple' : 'Apples // 苹果 🍎 —— Edible // 可食用',
    'brocoli' : 'Brocolis // 西兰花 🥦 —— Edible // 可食用',
    'ramen' : 'Ramen // 拉面 🍜 —— Edible // 可食用',
    'simp' : 'Super Interesting Magic Potions // 超级有趣的魔药 🍾 —— Edible // 可食用',
    'lifesaver' : 'Lifesaver // 救生器 💖 —— Tool // 工具',
    'banknote' : "Banknote // 钞票 💸 —— Tool // 工具"
}

def show_items(update,context):
    # sicheng是个big bug
    user = update.effective_user
    coins.check_user(user)
    uid = str(user.id)
    count = check_items(coins.coins[uid]["items"])
    msg = "Here's %s's inventory\n这是%s的库存\n-----------------------------"%(user.first_name,user.first_name)
    for key in count.keys():
        msg = f"{msg}\n{liewu[key]}: {count[key]}"
    update.message.reply_animation('https://media.tenor.com/images/136906d86850530f58747968eebfb35e/tenor.gif',caption=f"{msg}")

def get_command():
    return [
        BotCommand('buy','Buy nice useful stuff! // 购买有用的东西！'),
        BotCommand('sell','Sell useless stuff. // 出售无用的东西。'),
        BotCommand('inv','Check the items you have in your inventory. // 检查库存中的物品。')
    ]

def add_handler(dp):
    dp.add_handler(CommandHandler('buy', buy))
    dp.add_handler(CommandHandler('sell',sell))
    dp.add_handler(CommandHandler('inv', show_items))