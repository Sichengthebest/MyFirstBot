import random
import pokeconfig
import pokemon_new
import pokelist
import pokeutils
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand,InputMediaPhoto
from datetime import datetime,timedelta

typeTrans = {
    'Grass': '🌱',
    'Fire': '🔥',
    'Water': '💧',
    'Electric': '⚡',
    'Normal': '🌐',
    'Ice': '❄️',
    'Fighting': '🥊',
    'Poison': '☠️',
    'Ground': '⛰',
    'Flying': '🕊',
    'Psychic': '🌀',
    'Bug': '🐛',
    'Rock': '🪨',
    'Ghost': '👻',
    'Dragon': '🐉',
    'Dark': '🌑',
    'Steel': '⚙️',
    'Fairy': '🦄'
}

game = pokeconfig.CONFIG["pk"]

def save():
    pokeconfig.CONFIG["pk"] = game
    pokeconfig.save_config()

def check_time(uid):
    if not uid in game:
        game[uid] = {
            'gametime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'pb': 10,
            'gb': 5,
            'ub': 3,
            'mb': 1,
            'pokecoins': 0,
            'box': [],
            'bud': {},
            'dailytime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'spawn': False,
            'inv': []
        }

def add_bud(uid,p):  
    pdict = {'id':p.id,'name':p.name,'hp':p.hp,'atk':p.atk,'lvl':p.lvl,'xp':p.xp,'pktype':p.pktype,'upgrade':p.upgrade,'speed':p.speed,'evolvewith':p.evolvewith,'friendship':p.friendship}
    game[uid]['bud'] = pdict

def set_bud(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if game[uid]['bud'] == {}:
        kb = pokeutils.getkb([{'Bulbasaur':'pkbudstart:bulb'},{'Charmander':'pkbudstart:char'},{'Squirtle':'pkbudstart:squi'}])
        update.message.reply_photo('https://img.pokemondb.net/images/red-blue/kanto-starters.jpg',caption="Hi! My name is pokemon trainer BOTGOD. Someone told me that you wanted to become a master pokemon trainer. Well, I'm the person to seek. You can choose between 3 Kanto starter pokemon and return for more advice. Now, which pokemon would you like to have?",reply_markup=kb)
        return
    kblist = []
    for pkdict in game[uid]['box']:
        kblist.append({f"{pkdict['name']}, XP: {pkdict['xp']}":f"pkbudset:{game[uid]['box'].index(pkdict)}"})
    kb = pokeutils.getkb(kblist)
    update.message.reply_text("Which pokemon would you like to have as your buddy?",reply_markup=kb)

def budNewCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,index = query.data.split(':')
    game[uid]['bud'] = game[uid]['box'][int(index)]
    query.edit_message_text(f"{game[uid]['box'][int(index)]['name']}? He/she will be your best buddy! Use /view_bud@sichengpokemonbot to have the details!")
    save()

def bud(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if game[uid]['bud'] == {}:
        update.message.reply_text('You do not have a buddy! Use /set_bud@sichengpokemonbot to get one!')
    id = game[uid]['bud']['id']
    pk = pokelist.Pokemon(id,random.randint(pokelist.pokemon[id]['lvl'][0],pokelist.pokemon[id]['lvl'][1])*1000,game[uid]['bud']['friendship'])
    if game[uid]['bud']['upgrade'] == '':
        evo = 'This pokemon does not evolve.'
    else:
        if pokelist.pokemon[game[uid]['bud']['upgrade']]['evolvewith'] == '1':
            evo = f"Evolves at level {pokelist.pokemon[game[uid]['bud']['id']]['lvl'][1]+1} into {pokelist.pokemon[game[uid]['bud']['upgrade']]['name']}. To evolve, use /evolve ."
        elif pokelist.pokemon[game[uid]['bud']['upgrade']]['evolvewith'] == '3':
            evo = 'Evolves with high friendship'
        else:
            _,stone = game[uid]['bud']['evolvewith'].split(':')
            evo = f"Evolves by using a/an {pokemon_new.stoneTrans[stone]}. To evolve, use /evolve."
    types = ''
    for type in game[uid]['bud']['pktype']:
        types += f'{typeTrans[type]}'
    if game[uid]['bud']['lvl'] == 100:
        nextlvlmsg = ' {MAX}'
    else:
        nextlvlmsg = f"\nXP to next level: {game[uid]['bud']['lvl']*1000-game[uid]['bud']['xp']}"
    update.message.reply_photo(open(pk.getPhoto(),'rb'),caption=f"""Your {game[uid]['bud']['name']} {types}:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
💞 Friendship: {game[uid]['bud']['friendship']}/255
~~~~~~~~~~~~~~~~~~~~~~~~~~~
XP: {game[uid]['bud']['xp']}
Level: {game[uid]['bud']['lvl']}{nextlvlmsg}
🆙 Evolution: {evo}
~~~~~~~~~~~~~~~~~~~~~~~~~~~
💖 HP: {game[uid]['bud']['hp']}
💥 Atk: {game[uid]['bud']['atk']}
⚡️ Speed: {game[uid]['bud']['speed']}""")

def budStartCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,pk = query.data.split(':')
    if pk == 'bulb':
        budpk = pokelist.Pokemon('001',0,-1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/bulbasaur.jpg'))
        query.edit_message_caption('Bulbasaur? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    elif pk == 'char':
        budpk = pokelist.Pokemon('004',0,-1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/charmander.jpg'))
        query.edit_message_caption('Charmander? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    elif pk == 'squi':
        budpk = pokelist.Pokemon('007',0,-1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/squirtle.jpg'))
        query.edit_message_caption('Squirtle? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    save()

def evolve(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if game[uid]['bud'] == {}:
        update.message.reply_text('You do not have a buddy! Use /set_bud@sichengpokemonbot to get one!')
        return
    if pokelist.pokemon[game[uid]['bud']['id']]['upgrade'] == '':
        update.message.reply_text(f"Your buddy does not evolve!")
        return
    if pokelist.pokemon[game[uid]['bud']['upgrade']]['evolvewith'] == '1':
        if game[uid]['bud']['lvl'] < pokelist.pokemon[game[uid]['bud']['upgrade']]['lvl'][0]:
            update.message.reply_text(f"Your buddy is not ready to evolve yet! Your buddy evolves into {pokelist.pokemon[game[uid]['bud']['upgrade']]['name']} at level {pokelist.pokemon[game[uid]['bud']['upgrade']]['lvl'][0]}.")
            return
        update.message.reply_text(f"🎉 Success! Your {game[uid]['bud']['name']} evolved into a {pokelist.pokemon[game[uid]['bud']['upgrade']]['name']}! 🎉")
        game[uid]['box'].remove(game[uid]['bud'])
        p = pokelist.Pokemon(game[uid]['bud']['upgrade'],game[uid]['bud']['xp'],game[uid]['bud']['friendship'])
        game[uid]['box'].append(p)
        add_bud(uid,p)
    elif pokelist.pokemon[game[uid]['bud']['upgrade']]['evolvewith'] == '3':
        update.message.reply_text('🚧 Friendship is still in development. Please try evolving this pokemon later, and follow https://t.me/botgodupdates for the latest updates! 🚧')
    else:
        _,stone = pokelist.pokemon[game[uid]['bud']['upgrade']]['evolvewith'].split(':')
        if not stone in game[uid]['inv']:
            update.message.reply_text(f"You do not have the stone needed! Your buddy needs a {pokemon_new.stoneTrans[stone]} to evolve!")
            return
        update.message.reply_text(f"🎉 Success! Your {game[uid]['bud']['name']} evolved into a {pokelist.pokemon[game[uid]['bud']['upgrade']]['name']}! 🎉")
        game[uid]['box'].remove(game[uid]['bud'])
        p = pokelist.Pokemon(game[uid]['bud']['upgrade'],game[uid]['bud']['xp'],game[uid]['bud']['friendship'])
        add_bud(uid,p)
        game[uid]['box'].append(p)
        game[uid]['inv'].remove(stone)
    save()

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('view_bud',bud))
    dispatcher.add_handler(CommandHandler('set_bud',set_bud))
    dispatcher.add_handler(CommandHandler('evolve',evolve))
    dispatcher.add_handler(CallbackQueryHandler(budStartCallback,pattern="^pkbudstart:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(budNewCallback,pattern="^pkbudset:[A-Za-z0-9_]*"))