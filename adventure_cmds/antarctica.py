import util
from telegram.ext import dispatcher, CallbackQueryHandler

startkba = [{"WTH??? I thought this would be an adventure!":'ant:no1'},{"Sure! Penguins are soooooooooooooooo cute!":'ant:yes1'}]
startkb = util.getkb(startkba)

no1kba = [{"Fine, fine, I'll keep going...":'ant:yes1'},{"YES, I'm 1000% sure!":'antquit'}]
no1kb = util.getkb(no1kba)

blizzard = ""

restartkba = [{"Sure! Let's fly!":'ant:yes1'},{"Nah, I'll stay home.":'antstop'}]
restartkb = util.getkb(restartkba)

def antarctica(user,query):
    query.edit_message_text("Your friend (even if u have none ahahahahahahahaha) called you to join him in Antarctica... to count penguins! What do you do now?",reply_markup=startkb)

def check1(update,context):
    query = update.callback_query
    if query.data == 'ant:no1':
        query.edit_message_text("Are you sure you want to exit now? There seems to be some gold deep in Antarctica...",reply_markup=no1kb)
    else:
        query.edit_message_text("So you took a plane to Antarctica and landed safely at Davis Station. You and your imaginary friend (probably Siri) took to snowmobiles to explore the surrounding landscape. Suddenly, a blizzard came out of nowhere and trapped you and Siri inside it! What do you do?")
        
def quitCallback(update,context):
    query = update.callback_query
    query.edit_message_text("You stayed nice and warm inside your home and chatted with your friend (who turned out to be Siri), but you still have regretted your decision, since there turned out to have a maximum of 50000 GP in the heart of the continent. Are you ready to go back there to claim your lost reward?",reply_markup=restartkb)

def stop(update,context):
    query = update.callback_query
    query.edit_message_text("Aight, even though Quebec did not have the cold of Antarctica, and not the gold neither...")

def add_handler(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(check1,pattern="^ant:[A-Za-z0-9_-]*"))
    dispatcher.add_handler(CallbackQueryHandler(quitCallback,pattern="^antquit[A-Za-z0-9_-]*"))
    dispatcher.add_handler(CallbackQueryHandler(stop,pattern="^antstop[A-Za-z0-9_-]*"))