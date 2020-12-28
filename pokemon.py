import random
import config
import util
from telegram.ext import CommandHandler, dispatcher, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from datetime import datetime,timedelta


pokemons = {
    'c': [["Nidoran-♀",'https://img.pokemondb.net/artwork/nidoran-f.jpg'],["Voltorb",'https://img.pokemondb.net/artwork/voltorb.jpg'],["Rattata",'https://img.pokemondb.net/artwork/rattata.jpg'],["Gastly",'https://img.pokemondb.net/artwork/gastly.jpg'],["Psyduck",'https://img.pokemondb.net/artwork/psyduck.jpg'],["Meowth",'https://img.pokemondb.net/artwork/meowth.jpg'],["Sandshrew",'https://img.pokemondb.net/artwork/sandshrew.jpg'],["Magnemite",'https://img.pokemondb.net/artwork/magnemite.jpg'],["Shellder",'https://img.pokemondb.net/artwork/shellder.jpg'],["Geodude",'https://img.pokemondb.net/artwork/geodude.jpg'],["Mankey",'https://img.pokemondb.net/artwork/mankey.jpg'],["Bellsprout",'https://img.pokemondb.net/artwork/bellsprout.jpg'],["Seel",'https://img.pokemondb.net/artwork/seel.jpg'],["Machop",'https://img.pokemondb.net/artwork/machop.jpg'],["Grimer",'https://img.pokemondb.net/artwork/grimer.jpg'],["Slowpoke",'https://img.pokemondb.net/artwork/slowpoke.jpg'],["Poliwag",'https://img.pokemondb.net/artwork/poliwag.jpg'],["Diglett",'https://img.pokemondb.net/artwork/diglett.jpg'],["Abra",'https://img.pokemondb.net/artwork/abra.jpg'],["Drowzee",'https://img.pokemondb.net/artwork/drowzee.jpg'],["Paras",'https://img.pokemondb.net/artwork/paras.jpg'],["Caterpie",'https://img.pokemondb.net/artwork/caterpie.jpg'],["Oddish",'https://img.pokemondb.net/artwork/oddish.jpg'],["Venonat",'https://img.pokemondb.net/artwork/venonat.jpg'],["Nidoran-♂",'https://img.pokemondb.net/artwork/nidoran-m.jpg'],["Weedle",'https://img.pokemondb.net/artwork/weedle.jpg'],["Pidgey",'https://img.pokemondb.net/artwork/pidgey.jpg'],["Spearow",'https://img.pokemondb.net/artwork/spearow.jpg'],["Ekans",'https://static.pokemonpets.com/images/monsters-images-800-800/23-Ekans.png'],["Zubat",'https://img.pokemondb.net/artwork/zubat.jpg'],["Exeggcute",'https://img.pokemondb.net/artwork/exeggcute.jpg'],["Cubone",'https://img.pokemondb.net/artwork/cubone.jpg'],["Koffing",'https://img.pokemondb.net/artwork/koffing.jpg'],["Rhyhorn",'https://img.pokemondb.net/artwork/rhyhorn.jpg'],["Tangela",'https://img.pokemondb.net/artwork/tangela.jpg'],["Horsea",'https://img.pokemondb.net/artwork/horsea.jpg'],["Goldeen",'https://img.pokemondb.net/artwork/goldeen.jpg'],["Staryu",'https://img.pokemondb.net/artwork/staryu.jpg'],["Porygon",'https://img.pokemondb.net/artwork/porygon.jpg']],
    'u': [["Pikachu",'https://img.pokemondb.net/artwork/pikachu.jpg'],["Vulpix",'https://img.pokemondb.net/artwork/vulpix.jpg'],["Electrode",'https://img.pokemondb.net/artwork/electrode.jpg['],["Growlithe",'https://img.pokemondb.net/artwork/growlithe.jpg'],["Haunter",'https://img.pokemondb.net/artwork/haunter.jpg'],["Golduck",'https://img.pokemondb.net/artwork/golduck.jpg'],["Persian",'https://img.pokemondb.net/artwork/persian.jpg'],["Nidorina",'https://img.pokemondb.net/artwork/nidorina.jpg'],["Nidorino",'https://img.pokemondb.net/artwork/nidorino.jpg'],["Sandslash",'https://img.pokemondb.net/artwork/sandslash.jpg'],["Magneton",'https://img.pokemondb.net/artwork/magneton.jpg'],["Ponyta",'https://img.pokemondb.net/artwork/ponyta.jpg'],["Primeape",'https://img.pokemondb.net/artwork/primeape.jpg'],["Bulbasaur",'https://img.pokemondb.net/artwork/bulbasaur.jpg'],["Charmander",'https://img.pokemondb.net/artwork/charmander.jpg'],["Squirtle",'https://img.pokemondb.net/artwork/squirtle.jpg'],["Krabby",'https://img.pokemondb.net/artwork/krabby.jpg'],["Hypno",'https://img.pokemondb.net/artwork/hypno.jpg'],["Cloyster",'https://img.pokemondb.net/artwork/cloyster.jpg'],["Muk",'https://img.pokemondb.net/artwork/muk.jpg'],["Dewgong",'https://img.pokemondb.net/artwork/dewgong.jpg'],["Weepinbell",'https://img.pokemondb.net/artwork/weepinbell.jpg'],["Machoke",'https://img.pokemondb.net/artwork/machoke.jpg'],["Kadabra",'https://static.pokemonpets.com/images/monsters-images-300-300/64-Kadabra.png'],["Poliwhirl",'https://img.pokemondb.net/artwork/poliwhirl.jpg'],["Dugtrio",'https://img.pokemondb.net/artwork/dugtrio.jpg'],["Venomoth",'https://img.pokemondb.net/artwork/venomoth.jpg'],["Metapod",'https://img.pokemondb.net/artwork/metapod.jpg'],["Kakuna",'https://img.pokemondb.net/artwork/kakuna.jpg'],["Pidgeotto",'https://img.pokemondb.net/artwork/pidgeotto.jpg'],["Raticate",'https://img.pokemondb.net/artwork/raticate.jpg'],["Arbok",'https://img.pokemondb.net/artwork/arbok.jpg'],["Fearow",'https://img.pokemondb.net/artwork/fearow.jpg'],["Clefairy",'https://img.pokemondb.net/artwork/clefairy.jpg'],["Jigglypuff",'https://img.pokemondb.net/artwork/jigglypuff.jpg'],["Golbat",'https://img.pokemondb.net/artwork/golbat.jpg'],["Doduo",'https://img.pokemondb.net/artwork/doduo.jpg'],["Slobro",'https://img.pokemondb.net/artwork/slowbro.jpg'],["Gloom",'https://img.pokemondb.net/artwork/gloom.jpg'],["Parasect",'https://img.pokemondb.net/artwork/parasect.jpg'],["Tentacool",'https://img.pokemondb.net/artwork/tentacool.jpg'],["Graveler",'https://img.pokemondb.net/artwork/graveler.jpg'],["Marowak",'https://img.pokemondb.net/artwork/marowak.jpg'],["Weezing",'https://img.pokemondb.net/artwork/weezing.jpg'],["Rhydon",'https://img.pokemondb.net/artwork/rhydon.jpg'],["Chansey",'https://img.pokemondb.net/artwork/chansey.jpg'],["Seadra",'https://img.pokemondb.net/artwork/seadra.jpg'],["Seaking",'https://img.pokemondb.net/artwork/seaking.jpg'],["Scyther",'https://img.pokemondb.net/artwork/scyther.jpg'],["Magikarp",'https://img.pokemondb.net/artwork/magikarp.jpg'],["Eevee",'https://img.pokemondb.net/artwork/eevee.jpg'],["Omanyte",'https://img.pokemondb.net/artwork/omanyte.jpg'],["Kabuto",'https://img.pokemondb.net/artwork/kabuto.jpg'],["Dratini",'https://img.pokemondb.net/artwork/dratini.jpg']],
    'r': [["Raichu",'https://img.pokemondb.net/artwork/raichu.jpg'],["Nidoqueen",'https://img.pokemondb.net/artwork/nidoqueen.jpg'],["Nidoking",'https://img.pokemondb.net/artwork/nidoking.jpg'],["Ivysaur",'https://img.pokemondb.net/artwork/ivysaur.jpg'],["Wartortle",'https://img.pokemondb.net/artwork/wartortle.jpg'],["Charmeleon",'https://img.pokemondb.net/artwork/charmeleon.jpg'],["Butterfree",'https://img.pokemondb.net/artwork/butterfree.jpg'],["Beedrill",'https://img.pokemondb.net/artwork/beedrill.jpg'],["Pidgeot",'https://img.pokemondb.net/artwork/pidgeot.jpg'],["Clefable",'https://img.pokemondb.net/artwork/clefable.jpg'],["Wigglytuff",'https://img.pokemondb.net/artwork/wigglytuff.jpg'],["Vileplume",'https://img.pokemondb.net/artwork/vileplume.jpg'],["Golem",'https://img.pokemondb.net/artwork/golem.jpg'],["Victreebel",'https://img.pokemondb.net/artwork/victreebel.jpg'],["Poliwrath",'https://img.pokemondb.net/artwork/poliwrath.jpg'],["Tentacruel",'https://img.pokemondb.net/artwork/tentacruel.jpg'],["Rapidash",'https://img.pokemondb.net/artwork/rapidash.jpg'],["Dodrio",'https://img.pokemondb.net/artwork/dodrio.jpg'],["Kingler",'https://img.pokemondb.net/artwork/kingler.jpg'],["Exeggutor",'https://img.pokemondb.net/artwork/exeggutor.jpg'],["Hitmonlee",'https://img.pokemondb.net/artwork/hitmonlee.jpg'],["Hitmonchan",'https://img.pokemondb.net/artwork/hitmonchan.jpg'],["Lickitung",'https://img.pokemondb.net/artwork/lickitung.jpg'],["Starmie",'https://img.pokemondb.net/artwork/starmie.jpg'],["Mr.Mime",'https://img.pokemondb.net/artwork/mr-mime.jpg'],["Jynx",'https://img.pokemondb.net/artwork/jynx.jpg'],["Electabuzz",'https://img.pokemondb.net/artwork/electabuzz.jpg'],["Magmar",'https://img.pokemondb.net/artwork/magmar.jpg'],["Gyarados",'https://img.pokemondb.net/artwork/gyarados.jpg'],["Omastar",'https://img.pokemondb.net/artwork/omastar.jpg'],["Kabutops",'https://img.pokemondb.net/artwork/kabutops.jpg'],["Dragonair",'https://img.pokemondb.net/artwork/drangonair.jpg']],
    's': [["Venusaur",'https://img.pokemondb.net/artwork/venusaur.jpg'],["Charizard",'https://img.pokemondb.net/artwork/charizard.jpg'],["Blastoise",'https://img.pokemondb.net/artwork/blastoise.jpg'],["Alakazam",'https://img.pokemondb.net/artwork/alakazam.jpg'],["Onix",'https://img.pokemondb.net/artwork/onix.jpg'],["Machamp",'https://img.pokemondb.net/artwork/machamp.jpg'],["Farfetch'd",'https://img.pokemondb.net/artwork/farfetchd.jpg'],["Gengar",'https://img.pokemondb.net/artwork/gengar.jpg'],["Ninetales",'https://img.pokemondb.net/artwork/ninetales.jpg'],["Kangaskhan",'https://img.pokemondb.net/artwork/kangaskhan.jpg'],["Pinsir",'https://img.pokemondb.net/artwork/pinsir.jpg'],["Tauros",'https://img.pokemondb.net/artwork/tauros.jpg'],["Lapras",'https://img.pokemondb.net/artwork/lapras.jpg'],["Ditto",'https://img.pokemondb.net/artwork/ditto.jpg'],["Vaporeon",'https://img.pokemondb.net/artwork/vaporeon.jpg'],["Jolteon",'https://img.pokemondb.net/artwork/jolteon.jpg'],["Flareon",'https://img.pokemondb.net/artwork/flareon.jpg'],["Aerodactyl",'https://img.pokemondb.net/artwork/aerodactyl.jpg'],["Snorlax",'https://img.pokemondb.net/artwork/snorlax.jpg'],["Dragonite",'https://img.pokemondb.net/artwork/dragonite.jpg']],
    'l': [["Articuno",'https://img.pokemondb.net/artwork/articuno.jpg'],["Zapdos",'https://img.pokemondb.net/artwork/zapdos.jpg'],["Moltres",'https://img.pokemondb.net/artwork/moltres.jpg'],["Mewtwo",'https://img.pokemondb.net/artwork/mewtwo.jpg'],["Mew",'https://img.pokemondb.net/artwork/mew.jpg'],["Raikou",'https://img.pokemondb.net/artwork/raikou.jpg'],["Entei",'https://img.pokemondb.net/artwork/entei.jpg'],["Suicune",'https://img.pokemondb.net/artwork/suicune.jpg'],["Lugia",'https://img.pokemondb.net/artwork/lugia.jpg'],["Ho-oh",'https://img.pokemondb.net/artwork/ho-oh.jpg'],["Celebi",'https://img.pokemondb.net/artwork/celebi.jpg']]
}

rarityTrans = {
    'c': 'Common (50%)',
    'u': 'Uncommon (26%)',
    'r': 'Rare (19%)',
    's': 'Super Rare (4.333%)',
    'l': 'Legendary (0.667%)'
}

ballTrans = {
    'pk:pb': 'Pokeball',
    'pk:gb': 'Greatball',
    'pk:ub': 'Ultraball',
    'pk:mb': 'Masterball'
}

budinfo = {
    'Bulbasaur': {
        '16': 'Ivysaur',
        '32': 'Venusaur'
    },
    'Charmander': {
        '16': 'Charmeleon',
        '36': 'Charizard'
    },
    'Squirtle': {
        '16': 'Wartortle',
        '36': 'Blastoise'
    }
}

rate = ['c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','u','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','r','s','s','s','s','l']
rarity = random.choice(rate)

game = config.CONFIG["pk"]

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
            'bud': '',
            'budnow': '',
            'budxp': 0,
            'dailytime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'spawn': False,
            'currentpk': random.choice(pokemons[rarity])
        }

budskb = [{'Bulbasaur':'pkbud:bulb'},{'Charmander':'pkbud:char'},{"Squirtle":'pkbud:sqir'}]
budkb = util.getkb(budskb)

buyskb = [{'Pokeball':'pkbuy:pb','Greatball':'pkbuy:gb'},{'Ultraball':'pkbuy:ub','Masterball':'pkbuy:mb'}]
buykb = util.getkb(buyskb)

buynumspbkb = [{'1':'pkbuynum:1:pb','2':'pkbuynum:2:pb','3':'pkbuynum:3:pb','4':'pkbuynum:4:pb'},{'5':'pkbuynum:5:pb','6':'pkbuynum:6:pb','7':'pkbuynum:7:pb','8':'pkbuynum:8:pb'},{'9':'pkbuynum:9:pb','10':'pkbuynum:10:pb','11':'pkbuynum:11:pb','12':'pkbuynum:12:pb'}]
buynumpbkb = util.getkb(buynumspbkb)

buynumsgbkb = [{'1':'pkbuynum:1:gb','2':'pkbuynum:2:gb','3':'pkbuynum:3:gb','4':'pkbuynum:4:gb'},{'5':'pkbuynum:5:gb','6':'pkbuynum:6:gb','7':'pkbuynum:7:gb','8':'pkbuynum:8:gb'},{'9':'pkbuynum:9:gb','10':'pkbuynum:10:gb'}]
buynumgbkb = util.getkb(buynumsgbkb)

buynumsubkb = [{'1':'pkbuynum:1:ub','2':'pkbuynum:2:ub','3':'pkbuynum:3:ub','4':'pkbuynum:4:ub'},{'5':'pkbuynum:5:ub','6':'pkbuynum:6:ub'}]
buynumubkb = util.getkb(buynumsubkb)

buynumsmbkb = [{'1':'pkbuynum:1:mb','2':'pkbuynum:2:mb','3':'pkbuynum:3:mb'}]
buynummbkb = util.getkb(buynumsmbkb)

def save():
    config.CONFIG["pk"] = game
    config.save_config()

def budadd(uid,c):
    if game[uid]['budnow'] == '':
        return "\nYou do not have a buddy! Use the /bud command to get a buddy!"
    else:
        game[uid]['budxp'] += c
        if game[uid]['budxp'] >= 16000:
            game[uid]['budnow'] = budinfo[game[uid]['bud']]['16']
        elif game[uid]['budxp'] >= 32000:
            if game[uid]['bud'] == 'Bulbasaur':
                game[uid]['budnow'] = budinfo[game[uid]['bud']]['32']
            else:
               if game[uid]['budxp'] >= 36000:
                   game[uid]['budnow'] = budinfo[game[uid]['bud']]['36']
        return f"\nYour {game[uid]['budnow']} has gained {c} XP!"

def pokemon(update,context):
    global rarity
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    t = datetime.now()
    balls = []
    if not 'spawn' in game[uid]:
        game[uid]['spawn'] = False
    if not 'currentpk' in game[uid]:
        game[uid]['currentpk'] = random.choice(pokemons[rarity])
    if game[uid]['spawn'] == True:
        update.message.reply_text("You already spawned a pokemon! Catch that pokemon first. Use /reset if you think this is a bug.")
        return
    game[uid]['currentpk'] = random.choice(pokemons[rarity])
    game[uid]['spawn'] = True
    if t >= datetime.strptime(game[uid]['gametime'],"%Y/%m/%d %H:%M:%S"):
        if game[uid]['pb'] > 0:
            balls.append(InlineKeyboardButton('Pokeball',callback_data='pk:pb'))
        if game[uid]['gb'] > 0:
            balls.append(InlineKeyboardButton('Greatball',callback_data='pk:gb'))
        if game[uid]['ub'] > 0:
            balls.append(InlineKeyboardButton('Ultraball',callback_data='pk:ub'))
        if game[uid]['mb'] > 0:
            balls.append(InlineKeyboardButton('Masterball',callback_data='pk:mb'))
        kb = InlineKeyboardMarkup([balls,[InlineKeyboardButton('Abandon',callback_data='pk:run')]])
        update.message.reply_photo(game[uid]["currentpk"][1], caption=f"""You have found a wild {game[uid]['currentpk'][0]}!
Rarity: {rarityTrans[rarity]}
-------------------------
Balls left:
Pokeballs: {game[uid]['pb']}
Greatballs: {game[uid]['gb']}
Ultraballs: {game[uid]['ub']}
Masterballs: {game[uid]['mb']}""",reply_markup=kb)
        game[uid]['gametime'] = datetime.strftime(datetime.now() + timedelta(seconds=5),"%Y/%m/%d %H:%M:%S")
    else:
        update.message.reply_text("Slow it down, cmon!!! You have caught every single Pokemon around you, wait a few more seconds for them to respawn!")

def pokeCallback(update,context):
    global rarity
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    ball = query.data
    proll = random.randint(35,100)
    if ball == 'pk:pb' and rarity == 'c':
        myroll = random.randint(65,80)
        game[uid]['pb'] -= 1
    elif ball == 'pk:pb' and rarity == 'u':
        myroll = random.randint(50,70)
        game[uid]['pb'] -= 1
    elif ball == 'pk:pb' and rarity == 'r':
        myroll = random.randint(35,50)
        game[uid]['pb'] -= 1
    elif ball == 'pk:pb' and rarity == 's':
        myroll = random.randint(20,40)
        game[uid]['pb'] -= 1
    elif ball == 'pk:pb' and rarity == 'l':
        myroll = random.randint(1,35)
        game[uid]['pb'] -= 1
    elif ball == 'pk:gb' and rarity == 'c':
        myroll = random.randint(85,100)
        game[uid]['gb'] -= 1
    elif ball == 'pk:gb' and rarity == 'u':
        myroll = random.randint(70,90)
        game[uid]['gb'] -= 1
    elif ball == 'pk:gb' and rarity == 'r':
        myroll = random.randint(40,65)
        game[uid]['gb'] -= 1
    elif ball == 'pk:gb' and rarity == 's':
        myroll = random.randint(25,50)
        game[uid]['gb'] -= 1
    elif ball == 'pk:gb' and rarity == 'l':
        myroll = random.randint(10,40)
        game[uid]['gb'] -= 1
    elif ball == 'pk:ub' and rarity == 'c':
        myroll = random.randint(90,100)
        game[uid]['ub'] -= 1
    elif ball == 'pk:ub' and rarity == 'u':
        myroll = random.randint(80,95)
        game[uid]['ub'] -= 1
    elif ball == 'pk:ub' and rarity == 'r':
        myroll = random.randint(65,85)
        game[uid]['ub'] -= 1
    elif ball == 'pk:ub' and rarity == 's':
        myroll = random.randint(50,75)
        game[uid]['ub'] -= 1
    elif ball == 'pk:ub' and rarity == 'l':
        myroll = random.randint(20,50)
        game[uid]['ub'] -= 1
    elif ball == 'pk:mb':
        myroll = 100
        game[uid]['mb'] -= 1
    elif ball == 'pk:run':
        query.edit_message_caption("You ran away. HAHAHAHA coward!")
        game[uid]['spawn'] = False
        game[uid]['currentpk'] = random.choice(pokemons[rarity])
        return
    if rarity == 'c':
        coinsadd = random.randint(110,150)
        xpadd = random.randint(90,110)
    elif rarity == 'u':
        coinsadd = random.randint(210,250)
        xpadd = random.randint(240,260)
    elif rarity == 'r':
        coinsadd = random.randint(450,500)
        xpadd = random.randint(390,410)
    elif rarity == 's':
        coinsadd = random.randint(600,666)
        xpadd = random.randint(1490,1510)
    elif rarity == 'l':
        coinsadd = random.randint(19900,20100)
        xpadd = random.randint(9990,10010)
    if myroll > proll:
        game[uid]['pokecoins'] += coinsadd
        query.edit_message_caption(f"""Congratulations, {user.first_name}!
✅ You have caught a {game[uid]['currentpk'][0]} with a {ballTrans[ball]}!
You earned {coinsadd} pokecoins!
Rarity: {rarityTrans[rarity]}
-------------------------
Pokemon roll: {proll}
Your catch rate: {myroll}
-------------------------
Balls left:
Pokeballs: {game[uid]['pb']}
Greatballs: {game[uid]['gb']}
Ultraballs: {game[uid]['ub']}
Masterballs: {game[uid]['mb']}
-------------------------{budadd(uid,xpadd)}""")
        game[uid]['box'].append(game[uid]['currentpk'][0])
    elif myroll == proll:
        game[uid]['pokecoins'] += coinsadd
        query.edit_message_caption(f"""Congratulations, {user.first_name}!
✅ You have caught a {game[uid]['currentpk'][0]} with a {ballTrans[ball]}!
You earned {coinsadd} pokecoins!
Rarity: {rarityTrans[rarity]}
-------------------------
Pokemon roll: {proll}
Your catch rate: {myroll}
-------------------------
Balls left:
Pokeballs: {game[uid]['pb']}
Greatballs: {game[uid]['gb']}
Ultraballs: {game[uid]['ub']}
Masterballs: {game[uid]['mb']}
-------------------------{budadd(uid,xpadd)}""")
        game[uid]['box'].append(game[uid]['currentpk'][0])
    elif proll > myroll:
        query.edit_message_caption(f"""❌ {game[uid]['currentpk'][0]} broke out of the {ballTrans[ball]}!
Rarity: {rarityTrans[rarity]}
-------------------------
Pokemon roll: {proll}
Your catch rate: {myroll}
-------------------------
Balls left:
Pokeballs: {game[uid]['pb']}
Greatballs: {game[uid]['gb']}
Ultraballs: {game[uid]['ub']}
Masterballs: {game[uid]['mb']}""")
    rarity = random.choice(rate)
    game[uid]['currentpk'] = random.choice(pokemons[rarity])
    game[uid]['spawn'] = False
    save()

def box(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'pokecoins' in game[uid]:
        game[uid]['pokecoins'] = 0
    update.message.reply_text(f"You have {game[uid]['pokecoins']} pokecoins and your inventory is: {game[uid]['box']}")

def bal(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'pokecoins' in game[uid]:
        game[uid]['pokecoins'] = 0
    update.message.reply_text(f"{user.first_name}, you have {game[uid]['pokecoins']} pokecoins!")
    
def shop(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'spawn' in game[uid]:
        game[uid]['spawn'] = False
    if game[uid]['spawn'] == True:
        update.message.reply_text("You already spawned a pokemon! Wait until you've caught it to buy items!")
        return
    update.message.reply_text(f"""Buy some items for your adventure!
{user.first_name}'s pokeCoins: {game[uid]['pokecoins']}
-------------------------
You currently own:
{game[uid]['pb']} Pokeballs
{game[uid]['gb']} Greatballs
{game[uid]['ub']} Ultraballs
{game[uid]['mb']} Masterballs
-------------------------
Pokeball: 50 pokecoins
Greatball: 125 pokecoins
Ultraball: 400 pokecoins
Masterball: 17500 pokecoins""",reply_markup=buykb)

def shopCallback(update,context):
    query = update.callback_query
    object = query.data
    ball = object.split(":")[1]
    if ball == 'pb':
        ballreal = 'Pokeballs'
        query.edit_message_text(f"Aight, you want some {ballreal}. How many? Please choose one.",reply_markup=buynumpbkb)
    elif ball == 'gb':
        ballreal = 'Greatballs'
        query.edit_message_text(f"Aight, you want some {ballreal}. How many? Please choose one.",reply_markup=buynumgbkb)
    elif ball == 'ub':
        ballreal = 'Ultraballs'
        query.edit_message_text(f"Aight, you want some {ballreal}. How many? Please choose one.",reply_markup=buynumubkb)
    elif ball == 'mb':
        ballreal = 'Masterballs'
        query.edit_message_text(f"Aight, you want some {ballreal}. How many? Please choose one.",reply_markup=buynummbkb)
    save()

def shopnumCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,num,ball = query.data.split(':')
    if ball == 'pb':
        c = 50
    elif ball == 'gb':
        c = 125
    elif ball == 'ub':
        c = 400
    elif ball == 'mb':
        c = 17500
    query.edit_message_text(buy_stuff(user,c,num,ball))
    
def buy_stuff(user,c,num,ball):
    uid = str(user.id)
    totalcost = int(c) * int(num)
    if int(totalcost) > game[uid]['pokecoins']:
        return f"Sorry, ur just too poor you need {totalcost} pokecoins but you only have {game[uid]['pokecoins']} pokecoins."
    game[uid]['pokecoins'] -= totalcost
    game[uid][ball] += int(num)
    return f"Success! @{user.username} , you have bought {num} {ballTrans[f'pk:{ball}']}(s) with {totalcost} pokecoins and you have {game[uid]['pokecoins']} pokecoins remaining.\nYou now have {game[uid]['pb']} Pokeballs, {game[uid]['gb']} Greatballs, {game[uid]['ub']} Ultraballs and {game[uid]['mb']} Masterballs."
    

def bud(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'bud' in game[uid]:
        game[uid]['bud'] = ''
    if not 'budnow' in game[uid]:
        game[uid]['budnow'] = ''
    if not 'budxp' in game[uid]:
        game[uid]['budxp'] = 0
    level = int(game[uid]['budxp'] / 1000) + 1
    if game[uid]['bud'] == '':
        update.message.reply_photo('https://miro.medium.com/max/1200/1*y0-zWEUPYi6TRuz0lC-0Ig.jpeg',caption="""Hi! My name is pokemon trainer BOTGOD. Someone told me that you wanted to become a master pokemon trainer. Well, I'm the person to seek. You can choose between 3 starter pokemon and return for more advice. Now which pokemon would you like to have?""", reply_markup=budkb)
        return
    if level >= 16 and level < 32:
        game[uid]['budnow'] = budinfo[game[uid]['bud']]['16']
    elif level >= 32:
        if game[uid]['bud'] == 'Bulbasaur':
            game[uid]['budnow'] = budinfo[game[uid]['bud']]['32']
        elif level >= 36:
            game[uid]['budnow'] = budinfo[game[uid]['bud']]['36']
        else:
            pass
    if game[uid]['budnow'] == 'Bulbasaur':
        update.message.reply_photo('https://img.pokemondb.net/artwork/bulbasaur.jpg',caption=f"""Your Bulbasaur:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Ivysaur':
        update.message.reply_photo('https://img.pokemondb.net/artwork/ivysaur.jpg',caption=f"""Your Ivysaur:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Venusaur':
        update.message.reply_photo('https://img.pokemondb.net/artwork/venusaur.jpg',caption=f"""Your Venusaur:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Charmander':
        update.message.reply_photo('https://img.pokemondb.net/artwork/charmander.jpg',caption=f"""Your Charmander:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Charmeleon':
        update.message.reply_photo('https://img.pokemondb.net/artwork/charmeleon.jpg',caption=f"""Your Charmeleon:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Charizard':
        update.message.reply_photo('https://img.pokemondb.net/artwork/charizard.jpg',caption=f"""Your Charizard:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Squirtle':
        update.message.reply_photo('https://img.pokemondb.net/artwork/squirtle.jpg',caption=f"""Your Squirtle:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Wartortle':
        update.message.reply_photo('https://img.pokemondb.net/artwork/wartortle.jpg',caption=f"""Your Wartortle:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")
    elif game[uid]['budnow'] == 'Blastoise':
        update.message.reply_photo('https://img.pokemondb.net/artwork/blastoise.jpg',caption=f"""Your Blastoise:
Level: {level}
XP: {game[uid]['budxp']}
XP to next level: {level * 1000 - game[uid]['budxp']}""")

def budCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    pk = query.data
    if pk == 'pkbud:bulb':
        game[uid]['bud'] = 'Bulbasaur'
        game[uid]['budnow'] = 'Bulbasaur'
    elif pk == 'pkbud:char':
        game[uid]['bud'] = 'Charmander'
        game[uid]['budnow'] = 'Charmander'
    else:
        game[uid]['bud'] = 'Squirtle'
        game[uid]['budnow'] = 'Squirtle'
    query.edit_message_caption(f"{game[uid]['budnow']}? Nice choice! He will be with you for the rest of your adventure. Have fun!")

def surprise(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'dailytime' in game[uid]:
        game[uid]['dailytime'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    dailytime = datetime.strptime(game[uid]['dailytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() > dailytime:
        c = random.randint(100,500)
        pb = random.randint(5,15)
        gb = random.randint(3,10)
        ub = random.randint(1,5)
        mb = random.randint(0,1)
        game[uid]['pokecoins'] += c
        game[uid]['pb'] += pb
        game[uid]['gb'] += gb
        game[uid]['ub'] += ub
        if mb == 1:
            game[uid]['mb'] += mb
            update.message.reply_text(f"Here are your daily pokecoins, {user.first_name}\n{c} pokecoins were placed in your wallet.\nYou also got:\n{pb} Pokeballs\n{gb} Greatballs\n{ub} Ultraballs\n...and 1 Masterball\n这是您的每天打卡的 pokecoins，{user.first_name}\n{c} pokecoins已被放置在您的钱包中。")
        else:
            update.message.reply_text(f"Here are your daily pokecoins, {user.first_name}\n{c} pokecoins were placed in your wallet.\nYou also got:\n{pb} Pokeballs\n{gb} Greatballs\n...and {ub} Ultraballs\n这是您的每天打卡的 pokecoins，{user.first_name}\n{c} pokecoins已被放置在您的钱包中。")
        dailytime = datetime.now() + timedelta(days=1)
        game[uid]['dailytime'] = dailytime.strftime("%Y/%m/%d %H:%M:%S")
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one day hasn't passed yet!\n放慢速度，呆瓜！我不是用钱做的，小家伙，一天还没有过去！") 
    save()

def reset(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    game[uid]['spawn'] = False
    update.message.reply_text("You have reset your pokemon.")
    save()

def getCommand():
    return [BotCommand('pokemon','Go catch pokemon! // 去捉宠物小精灵！'),
        BotCommand('box','[BETA] Check the pokemon in your box! // [测试] 检查盒子里的宠物小精灵！'),
        BotCommand('pokeshop','Buy useful stuff for your adventure! // 为您的冒险购买有用的东西！'),
        BotCommand('bud','[BETA] Check on your buddy! // [测试] 检查您的好友！'),
        BotCommand('surprise','Get your daily injection of pokecoins! // 每天注射 Pokecoins！'),
        BotCommand('pokebal','Check the amount of pokecoins you have. // 检查您有多少 pokecoins。')
    ]

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('pokemon', pokemon))
    dispatcher.add_handler(CommandHandler('box', box))
    dispatcher.add_handler(CommandHandler('pokeshop',shop))
    dispatcher.add_handler(CommandHandler('bud',bud))
    dispatcher.add_handler(CommandHandler('surprise',surprise))
    dispatcher.add_handler(CommandHandler('pokebal',bal))
    dispatcher.add_handler(CommandHandler('reset',reset))
    dispatcher.add_handler(CallbackQueryHandler(pokeCallback,pattern="^pk:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(shopCallback,pattern="^pkbuy:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(budCallback,pattern="^pkbud:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(shopnumCallback,pattern="^pkbuynum:[A-Za-z0-9_]*"))