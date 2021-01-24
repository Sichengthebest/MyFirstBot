import random
import config
import pokemons
from utils import util
from utils import place
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
    'c': 'Common (50% encounter rate)',
    'u': 'Uncommon (26% encounter rate)',
    'r': 'Rare (19% encounter rate)',
    's': 'Super Rare (4.3% encounter rate)',
    'l': 'Legendary (0.7% encounter rate)'
}

def add_pokemon(uid,p):
    pdict = {'name':p.name,'hp':p.hp,'atk':p.atk,'lvl':p.lvl,'pktype':p.pktype,'upgrade':p.upgrade}
    game[uid]['box'].append(pdict)

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
    pokemons.check_time(str(uid))
    if game[str(uid)]['spawn'] == True:
        update.message.reply_text("You already spawned a pokemon! Catch that pokemon first. Use /reset if you think this is a bug.")
        return
    t = datetime.now() 
    if t < datetime.strptime(game[str(uid)]['gametime'],"%Y/%m/%d %H:%M:%S"):
        difference = datetime.strptime(game[str(uid)]['gametime'],"%Y/%m/%d %H:%M:%S") - datetime.now() 
        seconds = int(difference.total_seconds())
        update.message.reply_text(f"Slow it down, cmon!!! You have caught every single pokemon around you, please wait {seconds} seconds!\n放慢速度，呆瓜！！！您已经抓到身边的每只宠物小精灵，请等待{seconds}秒！\nCreator/作者: Sichengthebest")
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
        msg2 = '🚧 Bud command in development, sorry~ 🚧'
        game[str(uid)]['pokecoins'] += money
        add_pokemon(str(uid),p)
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
    game[str(uid)]['spawn'] = False
    game[str(uid)]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=10),"%Y/%m/%d %H:%M:%S")
    save()

def add_handler(dp):
    dp.add_handler(CommandHandler('pokemon',pokemon))
    dp.add_handler(CallbackQueryHandler(pokemonCatchCallback,pattern="^pkcatch:[A-Za-z0-9_]*"))