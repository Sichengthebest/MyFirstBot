import random
import os
import logging
import guess
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

def start(update, context):
    msg = "I'M THE GOD OF BOTS...\n我是机器人的上帝..."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
def echo(update, context):
    msg = "%s, yOu sAId %s, YOur uid iS %s, I hAte You." %(
        update.message.from_user.first_name,
        update.message.text,
        update.message.from_user.id,)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
def hunt(update, context):
    huntArr = ["You brought back a skunk and gained 10 XP! BTW I wonder who would want a skunk...\n你带回了一只臭鼬，获得了10XP！顺便说一句，我想知道谁会想要臭鼬...","You brought back a skunk and gained 10 XP! You STINK!\n你带回了一只臭鼬，获得了10XP！你好臭！","You have caught a deer! Good thing you didn't get lost in the forest! You got 25XP!\n你抓到了一头鹿！很好，你没有在森林里迷路！你获得了25XP！", "You have caught a deer! Good thing you brought your compass! You got 25XP!\n你抓到了一头鹿！很好，你带了指南针！你获得了25XP！", "You have caught a fox! Nice work! Gain 30XP.\n你抓到了一只狐狸！干得好！获得30XP。", "You have caught a deer! You got 25XP!\n你抓到了一头鹿！您获得了25XP！", "You have caught a rhinoceros! Was that even legal? Anyways, the buyer gave you 50XP.\n你抓到了犀牛！那合法吗？无论如何，买家给了你50XP。", "You have caught a BASILISK!! Where in the world did you find that??? +225XP!\n您抓到了蛇怪！您在哪里找到的？？？ + 225XP！", "You forgot your AK-47! Too bad.\n你忘记了你的AK-47！太糟糕了。", "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！", "You caught a fox, but someone stole it from you!\n您捉住了一只狐狸，但有人偷走了它！", "A bear caught you and you lost 30HP!\n一只熊抓住了您，您损失了30HP", "You caught an elephant, but the ads you placed were found by someone, and he called the cops on you! You got fined 100GP. Try the black market next time?\n您抓到一头大象，但您发的广告被某人发现，他叫了警察！您被罚款100GP。下次尝试一下黑市场？", "You DIED while fighting the basilisk! Would your CLASSMATE WARRIOR be your phoenix? -80HP.\n您在与蛇怪战斗时死了！您的同学战士会成为您的凤凰吗？ -80HP。"]
    result = random.choice(huntArr)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)
def search(update, context):
    searchArr = ["You searched the COVID testing centre and found a box full of masks! You sold them for 55GP!\n您搜索了COVID测试中心，发现里面装满了口罩！您以55GP的价格出售了它们","You searched the COVID testing centre. BAD IDEA, you got infected! Lose 40GP for hospital fees.\n您搜索了COVID测试中心。坏主意，您被感染了！损失40GP的住院费。", "You found 20GP in the basement. How long had it been here?\n您在地下室发现了20GP。已经在这里有多久了？", "You tried to rob Gringotts, but a random dude named The One Who Must Not Be Named said Avada Kedavra and you died.\n您试图抢劫古灵阁，但是一个名叫连名字都不能提的的家伙说阿瓦达索命，您死了。", "You decided to rob Gringotts. You chose the vault 713, which has nothing in it! Didn't you read The Philospher's Stone? Duh.\n您决定抢劫古灵阁。您选择了其中空的713号金库！您没读过《魔法石》吗？咄。", "You decided to rob Gringotts, and got 300GP! HOP ON THE DRAGON, QUICK!\n您决定抢劫古灵阁，并获得300GP！往龙上跳，快！", "You searched Le Parc National des L, not knowing it's a park for losers. Anyway, at least you got 9 GP from a bet with another loser.\n您搜索了 L 国家公园，却不知道它是输家的公园。无论如何，至少您与另一个失败者的下注获得9 GP。", "You searched a desert island and found buried treasure worth 270GP. GG!\n您搜索了一个荒岛，发现了价值270GP的埋藏宝藏。 棒棒哒！", "You searched the White House and found a secret vault. You opened it and found 400GP! Luckily there was no guards inside.\n您搜索了白宫，并找到了一个秘密保险库。您打开它，找到400GP！幸运的是里面没有警卫。", "You searched the White House, but came face-to-face with Donald Trump! You got fined 400GP.\n您搜索了白宫，但是与唐纳德·特朗普面对面了！您被罚款400GP。"]
    result = random.choice(searchArr)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/start - Random command that makes the bot say \"I'm THE GOD OF BOTS...\" // 使机器人说“我是机器人的上帝”的随机命令。\n/hunt - Gain XP by catching animals. // 以捕捉动物的方式获得XP。\n/search - Go fetch the GP falling from the sky!!! // 去获取从天上掉下来的GP吧！！！\n/searchap - Go to Hogwarts to fetch the AP falling from the sky!!! // 去霍格沃茨获取从天上掉下来的AP吧！！！\n/fish -  Gain XP by fishing. // 以钓鱼的方式获得XP。\n\nFor Classcraft users // 对于Classcraft用户:\n-------------\n/gainxp - Use when you get a reward in Classcraft. // 当您在Classcraft中获得奖励时使用。\n/losexp - Use when you die in Classcraft. // 当您在Classcraft中死亡时使用。")
def penalties(update,context):
    penalties = ["Great! You do not have to lose XP! 爽！您不必丢失XP！", "Uh-oh, you lose 400XP! 哎哟，你丢了400XP！", "NOOOOO!!! You lose 900XP! 好惨！您损失了900XP！", "Let BOTGOD decide your fate! 让BOTGOD决定您的命运吧！"]
    randomPenalty = random.choice(penalties)
    randomInt = random.randint(500,1200)
    if randomPenalty == penalties[3]:
        update.message.reply_text("%s\nDear %s, BOTGOD has decided to take %s XP away from you, peace.\n亲爱的%s，BOTGOD已决定夺走您的%s XP。希望您平安。\nCreator/作者: Sichengthebest"%(
            randomPenalty,
            update.message.from_user.first_name,
            randomInt,
            update.message.from_user.first_name,
            randomInt))
    else:
        update.message.reply_text("%s\nCreator/作者: Sichengthebest"%(randomPenalty))
def rewards(update,context):
    rewards = ["COOL! +90XP!\n爽！+90XP！", "Good! +40XP!\n很好！+40XP！", "Sad... Nothing happens.\n好伤心...什么都没发生。", "Let BOTGOD decide your fate!\n让BOTGOD决定您的命运吧！"]
    randomPenalty = random.choice(rewards)
    randomInt = random.randint(50,150)
    if randomPenalty == rewards[3]:
        update.message.reply_text("%s\nDear %s, BOTGOD has decided give you %s, keep up the good work!\n亲爱的%s，BOTGOD已决定奖励您%s XP。继续加油！\nCreator/作者: Sichengthebest"%(
            randomPenalty,
            update.message.from_user.first_name,
            randomInt,
            update.message.from_user.first_name,
            randomInt))
    else:
        update.message.reply_text("%s\nCreator/作者: Sichengthebest"%(randomPenalty))
def fish(update, context):
    fishes = ["You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught two herrings! +15XP!\n你钓到了二条鲱鱼！+15XP！", "You caught three herrings! +25XP!\n你钓到了三条鲱鱼！+25XP！", "You caught four herrings! +32XP!\n你钓到了四条鲱鱼！+32XP！", "You caught a lake trout! +50XP!\n你钓到了一条湖鳟！+50XP！", "You caught two lake trout! Yeah! +100XP!\n你钓到了两条湖鳟！+100XP！耶～", "You forgot your fishing pole!\n你忘了钓鱼竿！", "You forgot your lure!\n你忘了诱饵！", "YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250XP!\n您钓到了一条大白鲨！你是怎么做到的？+ 250XP！", "You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。", "You caught a lake trout, but it was too large and the police fined you 40GP!\n您抓到一条鳟鱼，但是它太大了，警察罚款了您40GP！", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～"]
    result = random.choice(fishes)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)
def potions(update, context):
    potions = ["You searched the Gryffindor common room and found a COMMON potion! +3AP!\n您搜索了格兰芬多公共休息室，发现了一瓶普通药水！+3AP！", "You searched the Gryffindor common room and found two COMMON potions! +6AP!\n您搜索了格兰芬多公共休息室，发现了两瓶普通药水！+6AP！", "You searched the Gryffindor common room, and found... nothing.\n您搜索了格兰芬多公共休息室，却发现……一无所获。", "You searched the Great Hall, and found a COMMON potion! +3AP!\n您搜索了大厅，发现了一瓶普通药水！+3AP！", "You searched the Great Hall, and Errol crashed into your face! You spent the rest of the day cleaning your hair.\n您搜索了大厅，但是埃罗尔撞到了您的脸上！您在一天的剩余时间里都在清理头发。", "You searched the Potions classroom, and found a COMMON potion! +3AP!\n您搜索了魔药教室，发现了一瓶普通药水！+3AP！", "You searched the Potions classroom, and found three COMMON potions! +9AP!\n您搜索了魔药教室，发现三瓶普通药水！+9AP！", "You searched the Potions classroom, and found one RARE potion! 20AP!\n您搜索了魔药教室，发现了一瓶稀有药水！+20AP！", "You searched the Potions classroom, and found Severus Snape! You lost 20HP!\n您搜索了魔药教室，发现了西弗勒斯·斯内普！您损失了20HP"]
    result = random.choice(potions)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)
def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text
TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
hunt_handler = CommandHandler('hunt', hunt)
search_handler = CommandHandler('search', search)
help_handler = CommandHandler('help', help)
badHandler = CommandHandler('losexp', penalties)
goodHandler = CommandHandler('gainxp', rewards)
fish_handler = CommandHandler('fish', fish)
apHandler = CommandHandler('searchap', potions)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hunt_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(badHandler)
dispatcher.add_handler(goodHandler)
dispatcher.add_handler(fish_handler)
dispatcher.add_handler(apHandler)
guess.addHandler(dispatcher)

updater.start_polling()