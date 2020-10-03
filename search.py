from telegram.ext import CommandHandler, dispatcher
import random

def search(update, context):
    searchArr = ["You searched the COVID testing centre and found a box full of masks! You sold them for 55GP!\n您搜索了COVID测试中心，发现里面装满了口罩！您以55GP的价格出售了它们","You searched the COVID testing centre. BAD IDEA, you got infected! Lose 40GP for hospital fees.\n您搜索了COVID测试中心。坏主意，您被感染了！损失40GP的住院费。", "You found 20GP in the basement. How long had it been here?\n您在地下室发现了20GP。已经在这里有多久了？", "You tried to rob Gringotts, but a random dude named The One Who Must Not Be Named said Avada Kedavra and you died.\n您试图抢劫古灵阁，但是一个名叫连名字都不能提的的家伙说阿瓦达索命，您死了。", "You decided to rob Gringotts. You chose the vault 713, which has nothing in it! Didn't you read The Philospher's Stone? Duh.\n您决定抢劫古灵阁。您选择了其中空的713号金库！您没读过《魔法石》吗？咄。", "You decided to rob Gringotts, and got 300GP! HOP ON THE DRAGON, QUICK!\n您决定抢劫古灵阁，并获得300GP！往龙上跳，快！", "You searched Le Parc National des L, not knowing it's a park for losers. Anyway, at least you got 9 GP from a bet with another loser.\n您搜索了 L 国家公园，却不知道它是输家的公园。无论如何，至少您与另一个失败者的下注获得9 GP。", "You searched a desert island and found buried treasure worth 270GP. GG!\n您搜索了一个荒岛，发现了价值270GP的埋藏宝藏。 棒棒哒！", "You searched the White House and found a secret vault. You opened it and found 400GP! Luckily there was no guards inside.\n您搜索了白宫，并找到了一个秘密保险库。您打开它，找到400GP！幸运的是里面没有警卫。", "You searched the White House, but came face-to-face with... A Random Orange Dude? You got fined 400GP.\n您搜索了白宫，但是与唐纳德·特朗普面对面了！您被罚款400GP。"]
    result = random.choice(searchArr)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)

def addHandler(dispatcher):
    srchHandler = CommandHandler('search', search)
    dispatcher.add_handler(srchHandler)