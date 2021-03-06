import random
import pokeconfig
import pokemons
import pokeutils
import pokelist
import bud
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand,CallbackQuery,InputMediaPhoto
from datetime import datetime,timedelta

game = pokeconfig.CONFIG["pk"]

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
    's': 'Super Rare (4.7% encounter rate)',
    'l': 'Legendary (0.29% encounter rate)',
    'ss': 'Special Spawn (1/10000 encounter rate)'
}

stoneTrans = {
    'daw': 'Dawn Stone',
    'dra': 'Dragon Scale',
    'dss': 'Deep Sea Scale',
    'dst': 'Deep Sea Tooth',
    'dub': 'Dubious Disc',
    'dus': 'Dusk Stone',
    'ele': 'Electirizer',
    'fir': 'Fire Stone',
    'ice': 'Ice Stone',
    'icr': 'Icy Rock',
    'kin': 'King\'s Rock',
    'lea': 'Leaf Stone',
    'mag': 'Magmarizer',
    'mst': 'Magnet Stone',
    'met': 'Metal Coat',
    'moo': 'Moon Stone',
    'mor': 'Mossy Rock',
    'ova': 'Oval Stone',
    'pri': 'Prism Scale',
    'pro': 'Protector',
    'rac': 'Razor Claw',
    'raf': 'Razor Fang',
    'rea': 'Reaper Cloth',
    'sac': 'Sachet',
    'shi': 'Shiny Stone',
    'sun': 'Sun Stone',
    'thu': 'Thunder Stone',
    'tra': 'Trade',
    'upg': 'Upgrade',
    'wat': 'Water Stone',
    'whi': 'Whipped cream'
}

def add_pokemon(uid,p):
    pdict = {'id':p.id,'name':p.name,'hp':p.hp,'currhp':p.currhp,'atk':p.atk,'def':p.defence,'lvl':p.lvl,'xp':p.xp,'pktype':p.pktype,'upgrade':p.upgrade,'speed':p.speed,'evolvewith':p.evolvewith,'friendship':p.friendship,'moves':p.moves}
    game[uid]['box'].append(pdict)

def add_xp(uid,xp):
    game[uid]['box'].remove(game[uid]['bud'])
    game[uid]['bud']['xp'] += xp
    if game[uid]['bud'] in game[uid]['party']:
        position = game[uid]['party'].index(game[uid]['bud'])
        if game[uid]['bud']['xp'] >= game[uid]['bud']['lvl'] * 1000:
            if game[uid]['bud']['xp'] >= 100000:
                game[uid]['bud']['lvl'] = 100
                msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP!"
                game[uid]['box'].append(game[uid]['bud'])
                game[uid]['party'][position] = game[uid]['bud']
                return msg
            game[uid]['bud']['lvl'] = int(game[uid]['bud']['xp'] / 1000)
            p = pokelist.Pokemon(game[uid]['bud']['id'],game[uid]['bud']['xp'],game[uid]['bud']['friendship'],game[uid]['bud']['moves'])
            bud.add_bud(uid,p)
            msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP! Congratutions! Your {game[uid]['bud']['name']} is now level {game[uid]['bud']['lvl']}!"
        else:
            msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP!"
        game[uid]['box'].append(game[uid]['bud'])
        game[uid]['party'][position] = game[uid]['bud']
    else:
        if game[uid]['bud']['xp'] >= game[uid]['bud']['lvl'] * 1000:
            if game[uid]['bud']['xp'] >= 100000:
                game[uid]['bud']['lvl'] = 100
                msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP!"
                game[uid]['box'].append(game[uid]['bud'])
                return msg
            game[uid]['bud']['lvl'] = int(game[uid]['bud']['xp'] / 1000)
            p = pokelist.Pokemon(game[uid]['bud']['id'],game[uid]['bud']['xp'],game[uid]['bud']['friendship'],game[uid]['bud']['moves'])
            bud.add_bud(uid,p)
            msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP! Congratutions! Your {game[uid]['bud']['name']} is now level {game[uid]['bud']['lvl']}!"
        else:
            msg = f"\n-------------------------\nYour {game[uid]['bud']['name']} gained {xp} XP!"
        game[uid]['box'].append(game[uid]['bud'])
    return msg
        

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
        money = random.randint(60,100)
        xp = random.randint(5,10)
    elif rarity == 'u':
        money = random.randint(250,300)
        xp = random.randint(15,25)
    elif rarity == 'r':
        money = random.randint(530,590)
        xp = random.randint(30,40)
    elif rarity == 's':
        money = random.randint(1140,1210)
        xp = random.randint(135,150)
    elif rarity == 'l':
        money = 20000
        xp = 500
    elif rarity == 'ss':
        money = 50000
        xp = 1000
    return money,xp

def save():
    pokeconfig.CONFIG["pk"] = game
    pokeconfig.save_config()

def pokemon(update,context):
    user = update.effective_user
    uid = user.id
    id,rarity = pokelist.getPokemon()
    lvlxp = random.randint(pokelist.pokemon[id]['lvl'][0],pokelist.pokemon[id]['lvl'][1])*1000
    pk = pokelist.Pokemon(id,lvlxp,-1,[])
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
    spawnbool = random.randint(0,3)
    if spawnbool > 1:
        update.message.reply_text('You did not find a pokemon.')
        game[str(uid)]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=10),"%Y/%m/%d %H:%M:%S")
        save()
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
    kb = pokeutils.getkb(balls)
    update.message.reply_photo(open(pk.getPhoto(),'rb'), caption=f"""A wild {pk.name} appeared!
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
    lvlxp = random.randint(pokelist.pokemon[pkmonid]['lvl'][0],pokelist.pokemon[pkmonid]['lvl'][1])*1000
    p = pokelist.Pokemon(pkmonid,lvlxp,-1,[])
    catchrate = getcatchrate(ball,p)
    money,xp = getadd(rarity)
    pokemonroll = random.randint(1,100)
    if pokemonroll < 5:
        stones = ['dss','dst','daw','dus','fir','ice','lea','moo','ova','dub','dra','pro','rea','sac','shi','sun','thu','upg','wat','whi','ele','mag','met','tra']
        stonesave = random.choice(stones)
        stoneget = stoneTrans[stonesave]
    if pokemonroll > catchrate:
        msg1 = f'❌ {p.name} broke out of the {ballTrans[ball]}!'
        msg2 = ''
    elif pokemonroll <= catchrate:
        msg1 = f'''Congratulations, {user.first_name}!
✅ You have caught a Level {p.lvl} {p.name} with a {ballTrans[ball]}!
You have earned {money} pokecoins!'''
        if game[str(uid)]['bud'] == {}:
            msg2 = '\n-------------------------\nYou do not have a buddy! Use /set_bud to get one!' 
        else:
            if pokemonroll < 5:
                msg2 = f'{add_xp(str(uid),xp)}\nOh? and you found a/an {stoneget}! Use it to evolve certain pokemon.'
                game[str(uid)]['inv'].append(stonesave)
            else:
                msg2 = f'{add_xp(str(uid),xp)}'
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
Masterballs: {game[str(uid)]['mb']}{msg2}''')
    game[str(uid)]['spawn'] = False
    game[str(uid)]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=10),"%Y/%m/%d %H:%M:%S")
    save()

def add_handler(dp):
    dp.add_handler(CommandHandler('pokemon',pokemon))
    dp.add_handler(CallbackQueryHandler(pokemonCatchCallback,pattern="^pkcatch:[A-Za-z0-9_]*"))