from telegram.ext import CommandHandler, dispatcher

def guess(update, context):
    if len(context.args) == 0 :
        update.message.reply_text("""猜一个0-100之间的数字。You guessed a number from 0 - 100.
        /guess 查看现在的状态和获取帮助。Check your current status and get help.
        /guess *your number here* 输入数字，看谁用的次数最少就能猜到。Enter number and see who uses it the least often to guess the number.
        """)
    else :
        number = int(context.args[0])
        update.message.reply_text("""Your number is: %s
        """%number)

def addHandler(dispatcher):
    guessHandler = CommandHandler('guess', guess)
    dispatcher.add_handler(guessHandler)