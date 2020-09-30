from telegram import Update,User
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
import random
randomNum = random.randint(1,99)

def guess(update, context):
    if len(context.args) == 0 :
        update.message.reply_text("""猜一个0-100之间的数字。Guess a number from 0 - 100.
/guess 查看现在的状态和获取帮助。Check your current status and get help.
/guess *your number here* 输入数字，看谁用的次数最少就能猜到。Enter number and see who uses it the least often to guess the number.
        """)
    else :
        number = context.args[0]
        if isinstance(number, int) == True:
            global randomNum
            print(randomNum)
            if randomNum == number :
                update.message.reply_text("""WOW! you guessed it! Good job, %s!
哇！你猜到了！做得好，%s！"""%(update.message.from_user.first_name, update.message.from_user.first_name))
            elif randomNum > number :
                update.message.reply_text("""WRONG! %s, you are dumb. Can't you see the number's bigger you idiot???
错！ %s，你真傻。你看不出这个数字更大吗？"""%(update.message.from_user.first_name, update.message.from_user.first_name))
            elif randomNum < number :
                update.message.reply_text("""WRONG! %s, you are dumb. Can't you see the number's bigger you idiot???
错！ %s，你真傻。你看不出这个数字更小吗？"""%(update.message.from_user.first_name, update.message.from_user.first_name))
        else :
            update.message.reply_text("""WRONG! %s, you are dumb. THIS IS NOT EVEN A NUMBER!!!
错！ %s，你真傻。你看不出这个都不是数字吗？"""%(update.message.from_user.first_name, update.message.from_user.first_name))

def addHandler(dispatcher):
    guessHandler = CommandHandler('guess', guess)
    dispatcher.add_handler(guessHandler)