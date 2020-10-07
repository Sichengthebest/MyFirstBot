from telegram.ext import CommandHandler, dispatcher
import random

def hunt(update, context):
    huntArr = ["You brought back a skunk! Gain 10GP. BTW I wonder who would want a skunk...\n你带回了一只臭鼬！获得10GP。顺便说一句，我想知道谁会想要臭鼬...","You brought back a skunk! Gain 10GP. You STINK!\n你带回了一只臭鼬！获得10GP。你好臭！","You have caught a deer! Gain 25GP. Good thing you didn't get lost in the forest!\n你抓到了一头鹿！获得25GP。很好，你没有在森林里迷路！", "You have caught a deer! Gain 25GP. Good thing you brought your compass!\n你抓到了一头鹿！获得25GP。很好，你带了指南针！", "You have caught a fox! Nice work! Gain 30GP.\n你抓到了一只狐狸！干得好！获得30GP", "You have caught a deer! Gain 25GP.\n你抓到了一头鹿！获得25GP。", "You have caught a rhinoceros! Was that even legal? Anyways, the buyer gave you 100GP.\n你抓到了犀牛！那合法吗？无论如何，卖家给了你100GP。", "You have caught a BASILISK!! Where in the world did you find that??? These 250GP are for you, you earned them!!!\n您抓到了蛇怪！您在哪里找到的？？？这250GP是给你的，无敌战士！", "You forgot your AK-47! Too bad.\n你忘记了你的AK-47！太糟糕了。", "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！", "You caught a fox, but someone stole it from you!\n您捉住了一只狐狸，但有人偷走了它！", "A bear caught you and you lost 30HP!\n一只熊抓住了您，您损失了30HP", "You caught an elephant, but the ads you placed was found by someone, and he called the cops on you! You got fined 100GP. Maybe try the black market next time?\n您抓到一头大象，但您的猎物被某人发现，他叫了警察！您被罚款100GP。", "You DIED while fighting the basilisk!\n您在与蛇怪战斗时死了！"]
    result = random.choice(huntArr)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)

def addHandler(dispatcher):
    huntHandler = CommandHandler('hunt', hunt)
    dispatcher.add_handler(huntHandler)