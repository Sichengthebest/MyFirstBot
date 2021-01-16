from telegram import InlineKeyboardButton, InlineKeyboardMarkup,BotCommand
from telegram.ext import CommandHandler, CallbackQueryHandler
from datetime import datetime,timedelta
import random
import coins
from utils import util

gametimes = {}

def get_users(user):
    if not user in gametimes:
        gametimes[user] = datetime.now()

def pm(update,context):
    user = update.effective_user
    uid = user.id
    buttonsa = [{"Normie meme":f'pm:n-{uid}'},{"Edgy meme":f'pm:e-{uid}'},{"Reposted meme":f'pm:r-{uid}'},{"Dank meme":f'pm:d-{uid}'}]
    buttons = util.getkb(buttonsa)
    get_users(user)
    t = datetime.now()
    if t < gametimes[user]:
        update.message.reply_text("Slow it down, cmon!!! If you post memes too much, you look like a normie. Wait a few more seconds! The default cooldown time is 1 minute.\nCreator/作者: Sichengthebest")
        return
    update.message.reply_text(f"OK, {user.first_name}, what type of meme do you want to post?",reply_markup=buttons)

def pmCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    meme,curruid = query.data.split('-')
    uid = str(user.id)
    yourchance = random.randint(1,100)
    if not curruid == uid:
        query.answer("Sorry but someone else is posting memes, not you so don't press these buttons",show_alert=True)
        return
    if meme == 'pm:n':
        memerollmin = 25
        memerollmax = 80
    elif meme == 'pm:e':
        memerollmin = 45
        memerollmax = 55
    elif meme == 'pm:r':
        memerollmin = 50
        memerollmax = 80
    else:
        memerollmin = 30
        memerollmax = 75
    if yourchance < memerollmin:
        query.edit_message_text(f"Lol, {user.first_name}, everyone hates your meme. You get 0 GP sucks to be you.")
    elif yourchance > memerollmin and yourchance < memerollmax:
        memeint = random.randint(400,750)
        query.edit_message_text(f"Not bad, {user.first_name}. Your meme got a decent response online. You get {memeint} GP from the ads.")
        coins.add_coins(user,memeint)
    else:
        memeint = random.randint(800,1150)
        query.edit_message_text(f"GG, {user.first_name}! Your meme is TRENDING online. You get {memeint} GP, nice meme bro!")
        coins.add_coins(user,memeint)
    gametimes[user] = datetime.now() + timedelta(seconds=60)

def getCommand():
    return [BotCommand('pm','Post a meme to earn GP! // 发布模因来赚取GP！')]

def add_handler(dp):
    dp.add_handler(CommandHandler('pm',pm))      
    dp.add_handler(CallbackQueryHandler(pmCallback,pattern="^pm:[A-Za-z0-9_]*"))