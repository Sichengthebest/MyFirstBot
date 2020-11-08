from telegram.ext import CommandHandler, dispatcher, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime,timedelta
import random
import coins

msg = """A game you play to gain GP.
为了获得GP而玩的游戏。
--------------------------------------------
Please choose one // 请选一个:
"""
gametime = datetime.now()
gametime2 = datetime.now()
buttons = ["covid testing centre","garage","gringotts","le parc national des l","island","white house","space","castle","zoo","neighbour","jungle","mountains","car"]
buttonsCH = ["covid测试中心","修车厂","古灵阁","L 国家公园","荒岛","白宫","宇宙","城堡","动物园","邻居","热带雨林","山","汽车"]
index = random.randint(0,12)
index1 = random.randint(0,12)
index2 = random.randint(0,12)
while index == index1:
    index1 = random.randint(0,12)
while index == index2:
    index2 = random.randint(0,12)
while index1 == index2:
    index2 = random.randint(0,12)
chosen = [buttons[index],buttons[index1],buttons[index2]]

def search(update, context):
    global buttons,chosen,index,index1,index2,gametime,gametime2
    index = random.randint(0,12)
    index1 = random.randint(0,12)
    index2 = random.randint(0,12)
    uid = update.effective_user.id
    while index == index1:
        index1 = random.randint(0,12)
    while index == index2:
        index2 = random.randint(0,12)
    while index1 == index2:
        index2 = random.randint(0,12)
    chosen = [buttons[index],buttons[index1],buttons[index2]]
    kb = InlineKeyboardMarkup([[InlineKeyboardButton("%s // %s"%(chosen[0],buttonsCH[index]), callback_data="searched: %s-%s"%(chosen[0],uid))],[InlineKeyboardButton("%s // %s"%(chosen[1],buttonsCH[index1]), callback_data="searched: %s-%s"%(chosen[1],uid))],[InlineKeyboardButton("%s // %s"%(chosen[2],buttonsCH[index2]), callback_data="searched: %s-%s"%(chosen[2],uid))]])
    gametime = datetime.now() + timedelta(seconds=1)
    t = datetime.now() 
    if t >= gametime2:
        update.message.reply_text("%s"%msg, reply_markup = kb)
        gametime2 = datetime.now() + timedelta(seconds=1)
    else:
        update.message.reply_text("Slow it down, cmon!!! You've already scouted the area for GP, try again in a few more seconds!\nCreator/作者: Sichengthebest")
    
def srchCallback(update, context): 
    global index,index1,index2,chosen,msg
    place, curruid = update.callback_query.data.split('-')
    uid = update.effective_user.id
    query = update.callback_query
    if str(uid) != curruid:
        query.answer("你是谁？你在哪儿？你想做啥？这是别人的，大笨蛋！",show_alert=True)
        return
    if place == "searched: covid testing centre":
        covidArr = ["You searched the COVID testing centre and found a box full of masks! You sold them for 55GP!\n您搜索了COVID测试中心，发现里面装满了口罩！您以55GP的价格出售了它们","You searched the COVID testing centre. BAD IDEA, you got infected! Lose 40GP for hospital fees.\n您搜索了COVID测试中心。坏主意，您被感染了！损失40GP的住院费。"]
        covid19r = random.choice(covidArr)
        query.edit_message_text("You %s\n\n%s\nCreator/作者: Sichengthebest"%(place,covid19r))
        if covid19r == covidArr[0]:
            coins.add_coins(update.effective_user,55)
        elif covid19r == covidArr[1]:
            coins.add_coins(update.effective_user,-40)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: garage":
        garagenum = random.randint(10,50)
        garageArr =["You found %sGP in the abandoned garage. How long had it been here?\n您在废弃的修车厂里发现了%sGP。已经在这里有多久了？"%(garagenum, garagenum), "You searched the abandoned garage, when suddenly the roof collapsed! You lost 25HP.\n您搜索了废弃的修车厂，突然屋顶塌了！您丧失了25HP。"]
        gResult = random.choice(garageArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,gResult))
        if gResult == garageArr[0]:
            coins.add_coins(update.effective_user,garagenum)
        elif gResult == garageArr[1]:
            coins.add_hp(update.effective_user,-25)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: gringotts":
        banknum = random.randint(200,500)
        bankArr =["You tried to rob Gringotts, but a random dude named The One Who Must Not Be Named said Avada Kedavra and you died.\n您试图抢劫古灵阁，但是一个名叫连名字都不能提的的家伙说阿瓦达索命，您死了。", "You decided to rob Gringotts. You chose the vault 713, which has nothing in it! Didn't you read The Philospher's Stone? Duh.\n您决定抢劫古灵阁。您选择了其中空的713号金库！您没读过《魔法石》吗？咄。", "You decided to rob Gringotts, and got %sGP! HOP ON THE DRAGON, QUICK!\n您决定抢劫古灵阁，并获得%sGP！往龙上跳，快！"%(banknum, banknum)]
        bankResult = random.choice(bankArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,bankResult))
        if bankResult == bankArr[2]:
            coins.add_coins(update.effective_user,banknum)
        elif bankResult == bankArr[0]:
            coins.add_hp(update.effective_user,-100)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: le parc national des l":
        betnum = random.randint(0,10)
        lArr = "You searched Le Parc National des L, not knowing it's a park for losers. Anyway, at least you got %s GP from a bet with another loser.\n您搜索了 L 国家公园，却不知道它是输家的公园。无论如何，至少您与另一个失败者的下注获得了%s GP。"%(betnum, betnum)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,lArr))
        coins.add_coins(update.effective_user,betnum)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: island":
        treasurenum = random.randint(50,300)
        islandArr = ["You searched a desert island and found buried treasure worth %sGP!\n您搜索了一个荒岛，发现了价值%sGP的埋藏宝藏！"%(treasurenum, treasurenum), "You searched a desert island and... found out that coconut crabs are really aggressive! Lose 20HP due to their deadly pincers.\n您搜索了一个荒岛，发现椰子蟹确实具有侵略性！由于他们致命的钳子而损失20HP。"]
        islandR = random.choice(islandArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,islandR))
        if islandR == islandArr[0]:
            coins.add_coins(update.effective_user,treasurenum)
        elif islandR == islandArr[1]:
            coins.add_hp(update.effective_user,-20)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: white house":
        whArr =["You searched the White House and found a secret vault. You opened it and found 400GP! Luckily there was no guards inside.\n您搜索了白宫，并找到了一个秘密保险库。您打开它，找到400GP！幸运的是里面没有警卫。", "You searched the White House, but came face-to-face with... A Random Orange Dude? You got corona and died.\n您搜索了白宫，但是与唐纳德·特朗普面对面了！您被感染新型冠状病毒然后挂了。"]
        whResult = random.choice(whArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,whResult))
        if whResult == whArr[0]:
            coins.add_coins(update.effective_user,400)
        elif whResult == whArr[1]:
            coins.add_hp(update.effective_user,-100)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: space":
        spaceArr = ["You photographed an alien! You gained 250GP!\n你拍到了一个外星人！您获得了250GP！", "Your spaceship blew up just after you saw the alien! Your photo got burnt, and so did you...\n刚看到外星人后，您的飞船爆炸了！您的照片被烧毁了，您也是...", "You photographed an alien, but everyone thought it was photoshop, and so you got nothing.\n您拍摄了一个外星人，但所有人都认为这是假的，所以您一无所获。", "You photographed an alien, but everyone thought it was photoshop, and so you got nothing.\n您拍摄了一个外星人，但所有人都认为这是假的，所以您一无所获。"]
        spaceR = random.choice(spaceArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,spaceR))
        if spaceR == spaceArr[0]:
            coins.add_coins(update.effective_user,250)
        elif spaceR == spaceArr[1]:
            coins.add_hp(update.effective_user,-100)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: castle":
        serial = random.randint(-70,-25)
        castleArr = ["You found a treasure chest! Gain 1000GP!\n您发现了一个宝藏箱！获得1000GP！", "A serial killer was hiding behind the throne, and you lost %s HP.\n一个连环杀手躲在王位后面，您失去了%sHP。"%(abs(serial), abs(serial)), "You got lost in the corridors of the castle, and you starved to death.\n您在城堡的走廊里迷路了，饿死了。"]
        castleR = random.choice(castleArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,castleR))
        if castleR == castleArr[0]:
            coins.add_coins(update.effective_user,1000)
        elif castleR == castleArr[1]:
            coins.add_hp(update.effective_user,serial)
        elif castleR == castleArr[2]:
            coins.add_hp(update.effective_user,-100)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: zoo":
        zooArr = ["You killed a zebra and sold its skin for 225GP!\n您杀死了斑马，并以225GP的价格出售了它的皮！", "You tried to kill a giraffe, but a random dude saw you! You got arrested and got fined 260GP.\n您试图杀死长颈鹿，但一个讨厌的家伙看见了您！您被捕并被罚款260GP。", "You got ate by a tiger.\n你被老虎吃了。", "You killed a goldfish, but no one wanted to buy a DEAD pet...\n您杀死了一条金鱼，但没人愿意买一个死的金鱼。"]
        zooResult = random.choice(zooArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,zooResult))
        if zooResult == zooArr[0]:
            coins.add_coins(update.effective_user,225)
        elif zooResult == zooArr[1]:
            coins.add_coins(update.effective_user,-260)
        elif zooResult == zooArr[2]:
            coins.add_hp(update.effective_user,-100)
        chosen = random.choices(buttons, k=3)
    elif place == "searched: neighbour":
        neiArr = ["You found 200GP under the master bed!\n您在主床下找到200GP！", "You penetrated in a mansion, but then realize that the dude who lived here was broke! HAAAHAHAHAHAA...\n您进入了一个豪宅，但随后意识到住在这里的那个家伙已经把钱都花了！哈哈哈哈哈哈...", "You got seen by another neighbour, and he called the cops on you! You got fined 400GP and lost 45HP.\n你被另一个邻居看见了，他叫了警察！您被罚款400GP，损失了45HP。"]
        nResult = random.choice(neiArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,nResult))
        if nResult == neiArr[0]:
            coins.add_coins(update.effective_user,200)
        elif nResult == neiArr[2]:
            coins.add_coins(update.effective_user,-400)
            coins.add_hp(update.effective_user,-45)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: jungle":
        jungleNum = random.randint(10,90)
        jungleArr = ["You found treasure on a tree! Gain %sGP.\n您在树上发现了宝藏！获得%sGP。"%(jungleNum, jungleNum), "You got eaten by an alligator.\n你被鳄鱼咬死了。"]
        jResult = random.choice(jungleArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,jResult))
        if jResult == jungleArr[0]:
            coins.add_coins(update.effective_user,jungleNum)
        elif jResult == jungleArr[1]:
            coins.add_hp(update.effective_user,-100)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: mountains":
        mountArr = ["You shot a mountain goat and sold it for 60GP!\n您宰杀了一只山羊，并以60GP的价格将其出售！", "You fell off a cliff and bumped your head. Lose 30HP.\n您从悬崖上摔下来并且撞了头。损失30HP。"]
        mtResult = random.choice(mountArr)
        query.edit_message_text("You %s\n%s\nCreator/作者: Sichengthebest"%(place,mtResult))
        if mtResult == mountArr[0]:
            coins.add_coins(update.effective_user,60)
        elif mtResult == mountArr[1]:
            coins.add_hp(update.effective_user,-30)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]
    elif place == "searched: car":
        indexcar = random.randint(0,11)
        normalgp = random.randint(250,1000)
        badgp = random.randint(-250,-150)
        year = random.randint(2008,2017)
        badyear = random.randint(1985,1994)
        greatyear = random.randint(2016,2020)
        carsluxe = ["Tesla Model S","BMW 750i","Mercedes-Benz S63 AMG","Audi A8","Jaguar XJ","Rolls-Royce Phantom","Lamborghini Aventador","Ferrari GTC4Lusso","Range Rover","Infiniti Q70","Maserati Quattroporte","Volvo XC90"]
        carsluxCH = ["特斯拉S系","宝马750i","奔驰S63 AMG","奥迪A8","捷豹XJ","劳斯莱斯 幻影","兰博基尼 Aventador","法拉利GTC4Lusso","路虎揽胜","英菲尼迪Q70","玛莎拉蒂 Quattroporte","沃尔沃 XC90"]
        carsbad = ["Toyota Tercel","Honda Civic","Chevrolet Cavalier","Ford Escort","Mazda 323","Nissan Sentra","Pontiac Grand Am","Hyundai Pony","Dodge Ram","Ford Taurus","Mercury Topaz","Chevrolet S-10"]
        carsbadCH = ["丰田 Tercel","本田 思域","雪佛兰 骑士","福特 护航","马自达323","日产 Sentra","庞蒂亚克 Grand Am","现代 小马","道奇 Ram","福特 金牛座","水星 黄玉","雪弗兰S-10"]
        carsnormal = ["Ford F-150","Honda Pilot","Toyota Camry","Chevrolet Malibu","Kia Sorento","Mitsubishi Lancer","Toyota Pruis","Hyundai Elantra","Mini Cooper","Dodge Durango","Infiniti G35 / Q50","Subaru Impreza"]
        carsnormalCH = ["福特F-150","本田 Pilot","丰田 凯美瑞","雪佛兰 马里布","起亚 索兰托","三菱 蓝瑟","丰田 普鲁斯","现代 Elantra","迷你库珀","道奇 杜兰戈","英菲尼迪G35/Q50","斯巴鲁 翼豹"]
        normalcar = carsnormal[indexcar]
        badcar = carsbad[indexcar]
        shiningcar = carsluxe[indexcar]
        normalcarCH = carsnormalCH[indexcar]
        badcarCH = carsbadCH[indexcar]
        bestcarCH = carsluxCH[indexcar]
        carArr = ["You stole a %s %s, worth %sGP!\n您偷了一个%s %s，价值%sGP！"%(normalcar,year,normalgp,normalcarCH,year,normalgp),"You stole a totally broken and useless %s %s, nobody wanted to buy it.\n您偷了一个完全破碎且无用的%s %s，没人愿意买。"%(badcar,badyear,badcarCH,badyear),"You got caught while trying to steal a %s %s. You got fined %sGP. Next time try doing it with less noice.\n您在尝试窃取一辆%s %s时被抓到。您被罚款%sGP。下次尝试减少杂音吧～"%(shiningcar,greatyear,abs(badgp),bestcarCH,greatyear,abs(badgp))]
        carResult = random.choice(carArr)
        query.edit_message_text("You %s\n\n%s\nCreator/作者: Sichengthebest"%(place,carResult))
        if carResult == carArr[0]:
            coins.add_coins(update.effective_user,normalgp)
        elif carResult == carArr[2]:
            coins.add_coins(update.effective_user,badgp)
        index = random.randint(0,12)
        index1 = random.randint(0,12)
        index2 = random.randint(0,12)
        while index == index1:
            index1 = random.randint(0,12)
        while index == index2:
            index2 = random.randint(0,12)
        while index1 == index2:
            index2 = random.randint(0,12)
        chosen = [buttons[index],buttons[index1],buttons[index2]]

def addHandler(dispatcher):
    srchHandler = CommandHandler('search', search)
    dispatcher.add_handler(srchHandler)
    dispatcher.add_handler(CallbackQueryHandler(srchCallback,pattern="^searched:[A-Za-z0-9_]*"))