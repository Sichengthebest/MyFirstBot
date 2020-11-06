from telegram import Update,User
from telegram.ext import Dispatcher,CommandHandler
import random
rooms = {}

def guess(update, context):
    chatid = update.message.chat.id
    if not (chatid in rooms):
        rooms[chatid] = {'randomNum': random.randint(1,99), 'tries': {}}
    tries = rooms[chatid]['tries']
    randomNum = rooms[chatid]['randomNum']
    if len(context.args) == 0 :
        update.message.reply_text("""猜一个0-100之间的数字。Guess a number from 0 - 100.
/guessnum 查看现在的状态和获取帮助。Check your current status and get help.
/guessnum *your number here* 输入数字，看谁用的次数最少就能猜到。Enter number and see who uses it the least often to guess the number.
Creator/作者: Sichengthebest
        """)
    else :
        name = update.message.from_user.first_name
        if context.args[0].isdigit():
            number = int(context.args[0])
            if name in tries:
                tries[name] += 1
            else:
                tries[name] = 1
            if number < 100 :
                if randomNum == number :
                    update.message.reply_text("""WOW! you guessed it! Good job, %s! You used %s times.
哇！你猜到了！做得好，%s！你用了%s次。\nCreator/作者: Sichengthebest"""%(name, tries[name], name, tries[name]))
                    randomNum = random.randint(1,99)
                    if name in tries:
                        tries[name] = 0
                elif randomNum > number :
                    update.message.reply_text("""WRONG! %s, you are dumb. Can't you see the number's bigger you idiot??? Number of tries: %s
错！ %s，你真傻。你看不出这个数字更大吗？你已经用了%s次了，你真差。\nCreator/作者: Sichengthebest"""%(name, tries[name], name, tries[name]))
                elif randomNum < number :
                    update.message.reply_text("""WRONG! %s, you are dumb. Can't you see the number's smaller you idiot???  Number of tries: %s
错！ %s，你真傻。你看不出这个数字更小吗？你已经用了%s次了，你真差。\nCreator/作者: Sichengthebest"""%(name, tries[name], name, tries[name]))
            else:
                update.message.reply_text("""WRONG! %s, you are dumb. I SAID BETWEEN 0 AND 100. Going back to elementry school? Number of tries: %s
错！ %s，你真傻。我说的是0和100之间。要回去上小学喽？你已经用了%s次了，你真差。\nCreator/作者: Sichengthebest"""%(name, tries[name], name, tries[name]))
        else:
            update.message.reply_text("""WRONG! %s, you are dumb. CAN'T YOU SEE %s IS NOT A NUMBER? Number of tries: %s          
错！ %s，你真傻。你看不出 %s 都不是数字吗？你已经用了%s次了，你真差。\n\nTips: NO DECIMALS PLS!\n请不要加小数点！\nCreator/作者: Sichengthebest"""%(name, context.args[0], tries[name], name, context.args[0], tries[name]))

def addHandler(dispatcher):
    guessHandler = CommandHandler('guessnum', guess)
    dispatcher.add_handler(guessHandler)
