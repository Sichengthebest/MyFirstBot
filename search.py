from telegram.ext import CommandHandler, dispatcher
import random

buttons = ["covid","garage","gringotts","lpark","island","whitehouse","space","castle","zoo","neighbour","jungle","mountains","car"]
chosen = random.choices(buttons, k=3)

def search(update, context):
    global buttons
    global chosen
    if len(context.args) == 0 :
        chosen = random.choices(buttons, k=3)
        update.message.reply_text("""A game you play to gain GP.
为了获得GP而玩的游戏。
-------------------------------------------------------------------------------------
Choices // 选项: /search %s, /search %s, /search %s
Choices are reset after each round! // 每轮结束后，选项会重置！
"""%(chosen[0],chosen[1],chosen[2]))
    else :
        place = str(context.args[0])
        if place == chosen[0] or place == chosen[1] or place == chosen[2]:
            if place == "covid":
                covidArr = ["You searched the COVID testing centre and found a box full of masks! You sold them for 55GP!\n您搜索了COVID测试中心，发现里面装满了口罩！您以55GP的价格出售了它们","You searched the COVID testing centre. BAD IDEA, you got infected! Lose 40GP for hospital fees.\n您搜索了COVID测试中心。坏主意，您被感染了！损失40GP的住院费。"]
                covid19r = random.choice(covidArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%covid19r)
                chosen = random.choices(buttons, k=3)
            elif place == "garage":
                garagenum = random.randint(10,50)
                garageArr =["You found %sGP in the abandoned garage. How long had it been here?\n您在废弃的修车厂里发现了%sGP。已经在这里有多久了？"%(garagenum, garagenum), "You searched the abandoned garage, when suddenly the roof collapsed! You lost 25HP.\n您搜索了废弃的修车厂，突然屋顶塌了！您丧失了25HP。"]
                gResult = random.choice(garageArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%gResult)
                chosen = random.choices(buttons, k=3)
            elif place == "gringotts":
                banknum = random.randint(200,500)
                bankArr =["You tried to rob Gringotts, but a random dude named The One Who Must Not Be Named said Avada Kedavra and you died.\n您试图抢劫古灵阁，但是一个名叫连名字都不能提的的家伙说阿瓦达索命，您死了。", "You decided to rob Gringotts. You chose the vault 713, which has nothing in it! Didn't you read The Philospher's Stone? Duh.\n您决定抢劫古灵阁。您选择了其中空的713号金库！您没读过《魔法石》吗？咄。", "You decided to rob Gringotts, and got %sGP! HOP ON THE DRAGON, QUICK!\n您决定抢劫古灵阁，并获得%sGP！往龙上跳，快！"%(banknum, banknum)]
                bankResult = random.choice(bankArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%bankResult)
                chosen = random.choices(buttons, k=3)
            elif place == "lpark":
                betnum = random.randint(0,10)
                lArr ="You searched Le Parc National des L, not knowing it's a park for losers. Anyway, at least you got %s GP from a bet with another loser.\n您搜索了 L 国家公园，却不知道它是输家的公园。无论如何，至少您与另一个失败者的下注获得了%s GP。"%(betnum, betnum)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%lArr)
                chosen = random.choices(buttons, k=3)
            elif place == "island":
                treasurenum = random.randint(50,300)
                islandArr = ["You searched a desert island and found buried treasure worth %sGP!\n您搜索了一个荒岛，发现了价值%sGP的埋藏宝藏！"%(treasurenum, treasurenum), "You searched a desert island and... found out that coconut crabs are really aggressive! Lose 20HP due to their deadly pincers.\n您搜索了一个荒岛，发现椰子蟹确实具有侵略性！由于他们致命的钳子而损失20HP。"]
                islandR = random.choice(islandArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%islandR)
                chosen = random.choices(buttons, k=3)
            elif place == "whitehouse":
                whArr =["You searched the White House and found a secret vault. You opened it and found 400GP! Luckily there was no guards inside.\n您搜索了白宫，并找到了一个秘密保险库。您打开它，找到400GP！幸运的是里面没有警卫。", "You searched the White House, but came face-to-face with... A Random Orange Dude? You got corona and died.\n您搜索了白宫，但是与唐纳德·特朗普面对面了！您被感染新型冠状病毒然后挂了。"]
                whResult = random.choice(whArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%whResult)
                chosen = random.choices(buttons, k=3)
            elif place == "space":
                spaceArr = ["You photographed an alien! You gained 250GP!\n你拍到了一个外星人！您获得了250GP！", "Your spaceship blew up just after you saw the alien! Your photo got burnt, and so did you...\n刚看到外星人后，您的飞船爆炸了！您的照片被烧毁了，您也是...", "You photographed an alien, but everyone thought it was photoshop, and so you got nothing.\n您拍摄了一个外星人，但所有人都认为这是假的，所以您一无所获。"]
                spaceR = random.choice(spaceArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%spaceR)
                chosen = random.choices(buttons, k=3)
            elif place == "castle":
                serial = random.randint(25,70)
                castleArr = ["You found a treasure chest! Gain 500GP!\n您发现了一个宝藏箱！获得500GP！", "A serial killer was hiding behind the throne, and you lost %s HP.\n一个连环杀手躲在王位后面，您失去了%sHP。"%(serial, serial), "You got lost in the corridors of the castle, and you starved to death.\n您在城堡的走廊里迷路了，饿死了。"]
                castleR = random.choice(castleArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%castleR)
                chosen = random.choices(buttons, k=3)
            elif place == "zoo":
                zooArr = ["You killed a zebra and sold its skin for 225GP!\n您杀死了斑马，并以225GP的价格出售了它的皮！", "You tried to kill a giraffe, but a random dude saw you! You got arrested and got fined 260GP.\n您试图杀死长颈鹿，但一个随机的家伙看见了您！您被捕并被罚款260GP。", "You got ate by a tiger.\n你被老虎吃了。", "You killed a goldfish, but no one wanted to buy a DEAD pet...\n您杀死了一条金鱼，但没人愿意买一个死的金鱼。"]
                zooResult = random.choice(zooArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%zooResult)
                chosen = random.choices(buttons, k=3)
            elif place == "neighbour":
                neiArr = ["You found 200GP under the master bed!\n您在主床下找到200GP！", "You penetrated in a mansion, but then realize that the dude who lived here was broke! HAAAHAHAHAHAA...\n您进入了一个豪宅，但随后意识到住在这里的那个家伙已经把钱都花了！哈哈哈哈哈哈...", "You got seen by another neighbor, and he called the cops on you! You got fined 400GP and lost 45HP.\n你被另一个邻居看见了，他叫了警察！您被罚款400GP，损失了45HP。"]
                nResult = random.choice(neiArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%nResult)
                chosen = random.choices(buttons, k=3)
            elif place == "jungle":
                jungleNum = random.randint(10,90)
                jungleArr = ["You found treasure on a tree! Gain %sGP.\n您在树上发现了宝藏！获得%sGP。"%(jungleNum, jungleNum), "You got eaten by an alligator.\n你被鳄鱼咬死了。"]
                jResult = random.choice(jungleArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%jResult)
                chosen = random.choices(buttons, k=3)
            elif place == "mountains":
                mountArr = ["You shot a mountain goat and sold it for 60GP!\n您宰杀了一只山羊，并以60GP的价格将其出售！", "You fell off a cliff and bumped your head. Lose 30HP.\n您从悬崖上摔下来并且撞了头。损失30HP。"]
                mtResult = random.choice(mountArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%mtResult)
                chosen = random.choices(buttons, k=3)
            elif place == "car":
                normalgp = random.randint(500,2000)
                badgp = random.randint(150,250)
                year = random.randint(2008,2017)
                badyear = random.randint(1985,1994)
                greatyear = random.randint(2016,2020)
                carsluxe = ["Tesla Model S","BMW 750i","Mercedes-Benz S63 AMG","Audi A8","Jaguar XJ","Rolls-Royce Phantom","Lamborghini Aventador","Ferrari GTC4Lusso","Range Rover","Infiniti Q70","Maserati Quattroporte","Volvo XC90"]
                carsbad = ["Toyota Tercel","Honda Civic","Chevrolet Cavalier","Ford Escort","Mazda 323","Nissan Sentra","Pontiac Grand Am","Hyundai Pony","Dodge Ram","Ford Taurus","Mercury Topaz"]
                carsnormal = ["Ford F-150","Honda Pilot","Toyota Camry","Chevrolet Malibu","Kia Sorento","Mitsubishi Lancer","Toyota Pruis","Hyundai Elantra","Mini Cooper","Dodge Durango","Infiniti G35 / Q50","Subaru Impreza"]
                normalcar = random.choice(carsnormal)
                badcar = random.choice(carsbad)
                shiningcar = random.choice(carsluxe)
                carArr = ["You stole a %s %s, worth %sGP!"%(normalcar,year,normalgp),"You stole a totally broken and useless %s %s, nobody wanted to buy it."%(badcar,badyear),"You got caught while trying to steal a %s %s. You got fined %sGP. Next time try doing it with less noice."%(shiningcar,greatyear,badgp)]
                carResult = random.choice(carArr)
                update.message.reply_text("%s\nCreator/作者: Sichengthebest"%carResult)
                chosen = random.choices(buttons, k=3)
        else:
           update.message.reply_text("Bruh what are you doing this place isn't even in the list!\n呃，您在做什么？这个地点都不在列表中！\nCreator/作者: Sichengthebest") 

def addHandler(dispatcher):
    srchHandler = CommandHandler('search', search)
    dispatcher.add_handler(srchHandler)