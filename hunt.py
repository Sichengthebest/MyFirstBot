from telegram.ext import CommandHandler, dispatcher
import random

def hunt(update, context):
    huntArr = ["You brought back a skunk and gained 10 XP! BTW I wonder who would want a skunk...\n你带回了一只臭鼬，获得了10XP！顺便说一句，我想知道谁会想要臭鼬...","You brought back a skunk and gained 10 XP! You STINK!\n你带回了一只臭鼬，获得了10XP！你好臭！","You have caught a deer! Good thing you didn't get lost in the forest! You got 25XP!\n你抓到了一头鹿！很好，你没有在森林里迷路！你获得了25XP！", "You have caught a deer! Good thing you brought your compass! You got 25XP!\n你抓到了一头鹿！很好，你带了指南针！你获得了25XP！", "You have caught a fox! Nice work! Gain 30XP.\n你抓到了一只狐狸！干得好！获得30XP。", "You have caught a deer! You got 25XP!\n你抓到了一头鹿！您获得了25XP！", "You have caught a rhinoceros! Was that even legal? Anyways, the buyer gave you 50XP.\n你抓到了犀牛！那合法吗？无论如何，买家给了你50XP。", "You have caught a BASILISK!! Where in the world did you find that??? +225XP!\n您抓到了蛇怪！您在哪里找到的？？？ + 225XP！", "You forgot your AK-47! Too bad.\n你忘记了你的AK-47！太糟糕了。", "You are so BAD, you didn't bring back anything!\n你好烂，你什么也没抓到！", "You caught a fox, but someone stole it from you!\n您捉住了一只狐狸，但有人偷走了它！", "A bear caught you and you lost 30HP!\n一只熊抓住了您，您损失了30HP", "You caught an elephant, but the ads you placed were found by someone, and he called the cops on you! You got fined 100GP. Try the black market next time?\n您抓到一头大象，但您发的广告被某人发现，他叫了警察！您被罚款100GP。下次尝试一下黑市场？", "You DIED while fighting the basilisk! Would your CLASSMATE WARRIOR be your phoenix? -80HP.\n您在与蛇怪战斗时死了！您的同学战士会成为您的凤凰吗？ -80HP。"]
    result = random.choice(huntArr)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)

def addHandler(dispatcher):
    huntHandler = CommandHandler('hunt', hunt)
    dispatcher.add_handler(huntHandler)