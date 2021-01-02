from telegram.ext import CommandHandler, dispatcher, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from adventure_cmds import antarctica,discord,home,mars,northpole,space
import coins
import util

startkba = [{"The North Pole":'adv:np'},{"Antarctica":'adv:an'},{"Discord":'adv:di'},{"Home":'adv:ho'},{"Mars":'adv:ma'},{"Space":'adv:sp'}]
startkb = util.getkb(startkba)

def adventureMain(update,context):
    user = update.effective_user
    uid = str(user.id)
    if coins.coins[uid]['coins'] < 10000:
        update.message.reply_text("Sorry, but since this command could take lots of money from you, I would recommend you to at least have 10000 GP with you, just in case u don't get in the negatives ;)")
        return
    update.message.reply_text("Nice! We're going on an adventure today! But where? Choose a place in the buttons below.",reply_markup=startkb)

def adventureCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    place = query.data
    if place == "adv:np":
        northpole.northpole(user,query)
    elif place == "adv:an":
        antarctica.antarctica(user,query)
    elif place == "adv:di":
        discord.discord(user,query)
    elif place == "adv:ho":
        home.home(user,query)
    elif place == "adv:sp":
        space.space(user,query)
    elif place == "adv:ma":
        mars.mars(user,query)

def add_handler(dispatcher):
    dispatcher.add_handler(CommandHandler('adv',adventureMain))
    dispatcher.add_handler(CallbackQueryHandler(adventureCallback,pattern="^adv:[A-Za-z0-9_-]*"))