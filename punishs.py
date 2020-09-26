from telegram.ext import CommandHandler, dispatcher
import random

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

def addHandler(dispatcher):
    guessHandler = CommandHandler('losexp', penalties)
    dispatcher.add_handler(guessHandler)