import random
import config
import util
from TESTING import place
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand,CallbackQuery,InputMediaPhoto
from datetime import datetime,timedelta

game = config.CONFIG["pk"]

def pokemon(update,context):
    user = update.effective_user
    uid = user.id
    places = place.find_place()
    falsekb = []
    for p in places:
        falsekb.append({p.name:f'pkmon:{p.id}:{uid}'})    
    kb = util.getkb(falsekb)
    #update.message.reply_text(f"我是一个大bug！！！\n{places[0]}\n{places[1]}",reply_markup=kb)
    update.message.reply_photo('https://nianticlabs.com/img/support/inapp-pokemongo-step1.jpg',caption=f"Where do you want to go?",reply_markup=kb)

def pokemonCallback(update,context):
    _, placeid, curruid = update.callback_query.data.split(':')
    user = update.effective_user
    uid = user.id
    query = update.callback_query
    if str(uid) != curruid:
        query.answer("你是谁？你在哪儿？你想做啥？这是别人的，大笨蛋！",show_alert=True)
        return
    p = place.Place(placeid)
    pokemons = p.pokemon
    id = random.choice(pokemons)
    pk = place.Pokemon(id)
    balls = []
    if game[str(uid)]['pb'] > 0:
        balls.append({'Pokeball':f'pk:pb-{uid}'})
    if game[str(uid)]['gb'] > 0:
        balls.append({'Greatball':f'pk:gb-{uid}'})
    if game[str(uid)]['ub'] > 0:
        balls.append({'Ultraball':f'pk:ub-{uid}'})
    if game[str(uid)]['mb'] > 0:
        balls.append({'Masterball':f'pk:mb-{uid}'})
    kb = util.getkb(balls)
    query.edit_message_caption(f"""You have found a wild {pk.name}!
Choose which ball you want to use to capture it!
Catch rate with pokeball: {pk.catchrate[0]}
Catch rate with greatball: {pk.catchrate[1]}
Catch rate with ultraball: {pk.catchrate[2]}
Catch rate with masterball: 100""",reply_markup=kb)
    query.edit_message_media(media=InputMediaPhoto(open(pk.getPhoto(),'rb')))

def pokemonCatchCallback(update,context):
    pass

def getCommand():
    return [BotCommand('newpokemon','thing')]

def add_handler(dp):
    dp.add_handler(CommandHandler('newpokemon',pokemon))
    dp.add_handler(CallbackQueryHandler(pokemonCallback,pattern="^pkmon:[A-Za-z0-9_]*"))
    dp.add_handler(CallbackQueryHandler(pokemonCatchCallback,pattern="^pkcatch:[A-Za-z0-9_]*"))