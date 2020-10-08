from telegram.ext import CommandHandler, dispatcher
import random

def search(update, context):
    if len(context.args) == 0 :
        update.message.reply_text("""A game you play to gain GP.
为了获得GP而玩的游戏。
-------------------------------------------------------------------------------------
COMMANDS:
/search covid : Search the COVID testing centre! Watch out for infected dudes...  //  搜寻COVID测试中心！当心被感染的家伙...
/search garage : Seach the abandoned garage.  //  搜索废弃的修车厂。
/search gringotts : Go rob the legendary bank in Harry Potter!  //  抢劫哈利·波特里传奇的银行！
/search lpark : Search in the hiking trails of Le Parc National des L!  //  搜索L国家公园的徒步路线吧！
/search island : Land ho!! Set sail for the sandy shores of an island in the tropics, in the hope of finding treasures! Watch out for coconut crabs!  //  陆地！启航前往热带岛屿的沙摊，希望能找到宝藏！当心椰子蟹！
/search whitehouse : Search the President's Residence! Watch out for the Orange-Faced dude himself!  //  搜索总统官邸！提防所有橙色脸蛋的家伙！
/search space : BLAST-OFF! Go fly into space, in the hope of finding aliens!  //  发射！飞入太空，目的是找到外星人！
/search castle : Search the royal palace! You can gain lots of GP, but it's hard to get!  //  搜索皇宫！您可以获得很多GP，但很难获得！
/search zoo : Search the place where animals are held in cages!  //  搜索将动物关在笼子里的地方！
/search neighbour : Break in to your neighbour's house! Is he rich, or is he just a beggar?  //  闯入邻居家！他很有钱吗，还是他只是一个乞钱的？
/search jungle: Search the lush rainforests of Amazonia! Watch out for alligators...  //  搜索亚马逊茂密的热带雨林！当心鳄鱼...""")
    else :
        place = str(context.args[0])
        if place == "covid":
            covidArr = ["You searched the COVID testing centre and found a box full of masks! You sold them for 55GP!\n您搜索了COVID测试中心，发现里面装满了口罩！您以55GP的价格出售了它们","You searched the COVID testing centre. BAD IDEA, you got infected! Lose 40GP for hospital fees.\n您搜索了COVID测试中心。坏主意，您被感染了！损失40GP的住院费。"]
            covid19r = random.choice(covidArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%covid19r)
        elif place == "garage":
            garagenum = random.randint(10,50)
            garageArr =["You found %sGP in the abandoned garage. How long had it been here?\n您在废弃的修车厂里发现了%sGP。已经在这里有多久了？"%(garagenum, garagenum), "You searched the abandoned garage, when suddenly the roof collapsed! You lost 25HP.\n您搜索了废弃的修车厂，突然屋顶塌了！您丧失了25HP。"]
            gResult = random.choice(garageArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%gResult)
        elif place == "gringotts":
            banknum = random.randint(200,500)
            bankArr =["You tried to rob Gringotts, but a random dude named The One Who Must Not Be Named said Avada Kedavra and you died.\n您试图抢劫古灵阁，但是一个名叫连名字都不能提的的家伙说阿瓦达索命，您死了。", "You decided to rob Gringotts. You chose the vault 713, which has nothing in it! Didn't you read The Philospher's Stone? Duh.\n您决定抢劫古灵阁。您选择了其中空的713号金库！您没读过《魔法石》吗？咄。", "You decided to rob Gringotts, and got %sGP! HOP ON THE DRAGON, QUICK!\n您决定抢劫古灵阁，并获得%sGP！往龙上跳，快！"%(banknum, banknum)]
            bankResult = random.choice(bankArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%bankResult)
        elif place == "lpark":
            betnum = random.randint(0,10)
            lArr ="You searched Le Parc National des L, not knowing it's a park for losers. Anyway, at least you got %s GP from a bet with another loser.\n您搜索了 L 国家公园，却不知道它是输家的公园。无论如何，至少您与另一个失败者的下注获得了%s GP。"%(betnum, betnum)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%lArr)
        elif place == "island":
            treasurenum = random.randint(50,300)
            islandArr = ["You searched a desert island and found buried treasure worth %sGP!\n您搜索了一个荒岛，发现了价值%sGP的埋藏宝藏！"%(treasurenum, treasurenum), "You searched a desert island and... found out that coconut crabs are really aggressive! Lose 20HP due to their deadly pincers.\n您搜索了一个荒岛，发现椰子蟹确实具有侵略性！由于他们致命的钳子而损失20HP。"]
            islandR = random.choice(islandArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%islandR)
        elif place == "whitehouse":
            whArr =["You searched the White House and found a secret vault. You opened it and found 400GP! Luckily there was no guards inside.\n您搜索了白宫，并找到了一个秘密保险库。您打开它，找到400GP！幸运的是里面没有警卫。", "You searched the White House, but came face-to-face with... A Random Orange Dude? You got corona and died.\n您搜索了白宫，但是与唐纳德·特朗普面对面了！您被感染新型冠状病毒然后挂了。"]
            whResult = random.choice(whArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%whResult)
        elif place == "space":
            spaceArr = ["You photographed an alien! You gained 250GP!\n你拍到了一个外星人！您获得了250GP！", "Your spaceship blew up just after you saw the alien! Your photo got burnt, and so did you...\n刚看到外星人后，您的飞船爆炸了！您的照片被烧毁了，您也是...", "You photographed an alien, but everyone thought it was photoshop, and so you got nothing.\n您拍摄了一个外星人，但所有人都认为这是假的，所以您一无所获。"]
            spaceR = random.choice(spaceArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%spaceR)
        elif place == "castle":
            serial = random.randint(25,70)
            castleArr = ["You found a treasure chest! Gain 500GP!\n您发现了一个宝藏箱！获得500GP！", "A serial killer was hiding behind the throne, and you lost %s HP.\n一个连环杀手躲在王位后面，您失去了%sHP。"%(serial, serial), "You got lost in the corridors of the castle, and you starved to death.\n您在城堡的走廊里迷路了，饿死了。"]
            castleR = random.choice(castleArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%castleR)
        elif place == "zoo":
            zooArr = ["You killed a zebra and sold its skin for 225GP!\n您杀死了斑马，并以225GP的价格出售了它的皮！", "You tried to kill a giraffe, but a random dude saw you! You got arrested and got fined 260GP.\n您试图杀死长颈鹿，但一个随机的家伙看见了您！您被捕并被罚款260GP。", "You got ate by a tiger.\n你被老虎吃了。", "You killed a goldfish, but no one wanted to buy a DEAD pet...\n您杀死了一条金鱼，但没人愿意买一个死的金鱼。"]
            zooResult = random.choice(zooArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%zooResult)
        elif place == "neighbour":
            neiArr = ["You found 200GP under the master bed!\n您在主床下找到200GP！", "You penetrated in a mansion, but then realize that the dude who lived here was broke! HAAAHAHAHAHAA...\n您进入了一个豪宅，但随后意识到住在这里的那个家伙已经把钱都花了！哈哈哈哈哈哈...", "You got seen by another neighbor, and he called the cops on you! You got fined 400GP and lost 45HP.\n你被另一个邻居看见了，他叫了警察！您被罚款400GP，损失了45HP。"]
            nResult = random.choice(neiArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%nResult)
        elif place == "jungle":
            jungleNum = random.randint(10,90)
            jungleArr = ["You found treasure on a tree! Gain %sGP.\n您在树上发现了宝藏！获得%sGP。"%(jungleNum, jungleNum), "You got eaten by an alligator.\n你被鳄鱼咬死了。"]
            jResult = random.choice(jungleArr)
            update.message.reply_text("%s\nCreator/作者: Sichengthebest"%jResult)

def addHandler(dispatcher):
    srchHandler = CommandHandler('search', search)
    dispatcher.add_handler(srchHandler)