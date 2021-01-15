import random
import config
import util
from TESTING import place
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand,CallbackQuery,InputMediaPhoto
from datetime import datetime,timedelta

game = config.CONFIG["pk"]

ballTrans = {
    'pb': 'Pokeball',
    'gb': 'Greatball',
    'ub': 'Ultraball',
    'mb': 'Masterball'
}

rarityTrans = {
    'c': 'Common (50%)',
    'u': 'Uncommon (26%)',
    'r': 'Rare (19%)',
    's': 'Super Rare (4.1%)',
    'l': 'Legendary (0.9%)'
}

def getcatchrate(ball,p):
    if ball == 'pb':
        catchrate = p.catchrate[0]
    elif ball == 'gb':
        catchrate = p.catchrate[1]
    elif ball == 'ub':
        catchrate = p.catchrate[2]
    elif ball == 'mb':
        catchrate = 100
    return catchrate

def getadd(rarity):
    if rarity == 'c':
        money = random.randint(35,75)
        xp = random.randint(5,25)
    elif rarity == 'u':
        money = random.randint(75,115)
        xp = random.randint(15,35)
    elif rarity == 'r':
        money = random.randint(200,240)
        xp = random.randint(40,60)
    elif rarity == 's':
        money = random.randint(560,600)
        xp = random.randint(95,115)
    elif rarity == 'l':
        money = 20000
        xp = 333
    return money,xp

def save():
    config.CONFIG["pk"] = game
    config.save_config()

def pokemon(update,context):
    user = update.effective_user
    uid = user.id
    id,rarity = place.getPokemon()
    pk = place.Pokemon(id)
    balls = []
    if game[str(uid)]['spawn'] == True:
        update.message.reply_text("You already spawned a pokemon! Catch that pokemon first. Use /reset if you think this is a bug.")
        return
    game[str(uid)]['spawn'] = True
    if game[str(uid)]['pb'] > 0:
        balls.append({'Pokeball':f'pkcatch:pb:{uid}:{id}:{rarity}'})
    if game[str(uid)]['gb'] > 0:
        balls.append({'Greatball':f'pkcatch:gb:{uid}:{id}:{rarity}'})
    if game[str(uid)]['ub'] > 0:
        balls.append({'Ultraball':f'pkcatch:ub:{uid}:{id}:{rarity}'})
    if game[str(uid)]['mb'] > 0:
        balls.append({'Masterball':f'pkcatch:mb:{uid}:{id}:{rarity}'})
    kb = util.getkb(balls)
    update.message.reply_photo(open(pk.getPhoto(),'rb'), caption=f"""You have found a wild {pk.name}!
Rarity: {rarityTrans[rarity]}
-------------------------
Balls left:
Pokeballs: {game[str(uid)]['pb']}
Greatballs: {game[str(uid)]['gb']}
Ultraballs: {game[str(uid)]['ub']}
Masterballs: {game[str(uid)]['mb']}
-------------------------
Choose which ball you want to use to capture it!""",reply_markup=kb)

def pokemonCatchCallback(update,context):
    _, ball, curruid, pkmonid, rarity = update.callback_query.data.split(':')
    user = update.effective_user
    uid = user.id
    query = update.callback_query
    if str(uid) != curruid:
        query.answer("你是谁？你在哪儿？你想做啥？这是别人的，大笨蛋！",show_alert=True)
        return
    p = place.Pokemon(pkmonid)
    catchrate = getcatchrate(ball,p)
    money,xp = getadd(rarity)
    pokemonroll = random.randint(1,100)
    if pokemonroll > catchrate:
        msg1 = f'❌ {p.name} broke out of the {ballTrans[ball]}!'
        msg2 = ''
    elif pokemonroll <= catchrate:
        msg1 = f'''Congratulations, {user.first_name}!
✅ You have caught a Level {p.lvl} {p.name} with a {ballTrans[ball]}!
You have earned {money} pokecoins!'''
        msg2 = f'Your {game[str(uid)]["budnow"]} gained {xp} XP!'
        game[str(uid)]['pokecoins'] += money
        game[str(uid)]['budxp'] += xp
    game[str(uid)][ball] -= 1
    query.edit_message_caption(f'''{msg1}
Rarity: {rarityTrans[rarity]}
-------------------------
Pokemon roll: {pokemonroll}
Your catch rate: {catchrate}
-------------------------
Balls left:
Pokeballs: {game[str(uid)]['pb']}
Greatballs: {game[str(uid)]['gb']}
Ultraballs: {game[str(uid)]['ub']}
Masterballs: {game[str(uid)]['mb']}
-------------------------
{msg2}''')
    save()

def getCommand():
    return [BotCommand('newpokemon','thing')]

def add_handler(dp):
    dp.add_handler(CommandHandler('newpokemon',pokemon))
    dp.add_handler(CallbackQueryHandler(pokemonCatchCallback,pattern="^pkcatch:[A-Za-z0-9_]*"))