import random
import config
import pokemon_new
from utils import pokelist
from utils import util
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand,InputMediaPhoto
from datetime import datetime,timedelta


pokemons = {
    'c': [["Nidoran-♀",'https://img.pokemondb.net/artwork/nidoran-f.jpg'],["Voltorb",'https://img.pokemondb.net/artwork/voltorb.jpg'],["Rattata",'https://img.pokemondb.net/artwork/rattata.jpg'],["Gastly",'https://img.pokemondb.net/artwork/gastly.jpg'],["Psyduck",'https://img.pokemondb.net/artwork/psyduck.jpg'],["Meowth",'https://img.pokemondb.net/artwork/meowth.jpg'],["Sandshrew",'https://img.pokemondb.net/artwork/sandshrew.jpg'],["Magnemite",'https://img.pokemondb.net/artwork/magnemite.jpg'],["Shellder",'https://img.pokemondb.net/artwork/shellder.jpg'],["Geodude",'https://img.pokemondb.net/artwork/geodude.jpg'],["Mankey",'https://img.pokemondb.net/artwork/mankey.jpg'],["Bellsprout",'https://img.pokemondb.net/artwork/bellsprout.jpg'],["Seel",'https://img.pokemondb.net/artwork/seel.jpg'],["Machop",'https://img.pokemondb.net/artwork/machop.jpg'],["Grimer",'https://img.pokemondb.net/artwork/grimer.jpg'],["Slowpoke",'https://img.pokemondb.net/artwork/slowpoke.jpg'],["Poliwag",'https://img.pokemondb.net/artwork/poliwag.jpg'],["Diglett",'https://img.pokemondb.net/artwork/diglett.jpg'],["Abra",'https://img.pokemondb.net/artwork/abra.jpg'],["Drowzee",'https://img.pokemondb.net/artwork/drowzee.jpg'],["Paras",'https://img.pokemondb.net/artwork/paras.jpg'],["Caterpie",'https://img.pokemondb.net/artwork/caterpie.jpg'],["Oddish",'https://img.pokemondb.net/artwork/oddish.jpg'],["Venonat",'https://img.pokemondb.net/artwork/venonat.jpg'],["Nidoran-♂",'https://img.pokemondb.net/artwork/nidoran-m.jpg'],["Weedle",'https://img.pokemondb.net/artwork/weedle.jpg'],["Pidgey",'https://img.pokemondb.net/artwork/pidgey.jpg'],["Spearow",'https://img.pokemondb.net/artwork/spearow.jpg'],["Ekans",'https://static.pokemonpets.com/images/monsters-images-800-800/23-Ekans.png'],["Zubat",'https://img.pokemondb.net/artwork/zubat.jpg'],["Exeggcute",'https://img.pokemondb.net/artwork/exeggcute.jpg'],["Cubone",'https://img.pokemondb.net/artwork/cubone.jpg'],["Koffing",'https://img.pokemondb.net/artwork/koffing.jpg'],["Rhyhorn",'https://img.pokemondb.net/artwork/rhyhorn.jpg'],["Tangela",'https://img.pokemondb.net/artwork/tangela.jpg'],["Horsea",'https://img.pokemondb.net/artwork/horsea.jpg'],["Goldeen",'https://img.pokemondb.net/artwork/goldeen.jpg'],["Staryu",'https://img.pokemondb.net/artwork/staryu.jpg'],["Porygon",'https://img.pokemondb.net/artwork/porygon.jpg']],
    'u': [["Pikachu",'https://img.pokemondb.net/artwork/pikachu.jpg'],["Vulpix",'https://img.pokemondb.net/artwork/vulpix.jpg'],["Electrode",'https://img.pokemondb.net/artwork/electrode.jpg['],["Growlithe",'https://img.pokemondb.net/artwork/growlithe.jpg'],["Haunter",'https://img.pokemondb.net/artwork/haunter.jpg'],["Golduck",'https://img.pokemondb.net/artwork/golduck.jpg'],["Persian",'https://img.pokemondb.net/artwork/persian.jpg'],["Nidorina",'https://img.pokemondb.net/artwork/nidorina.jpg'],["Nidorino",'https://img.pokemondb.net/artwork/nidorino.jpg'],["Sandslash",'https://img.pokemondb.net/artwork/sandslash.jpg'],["Magneton",'https://img.pokemondb.net/artwork/magneton.jpg'],["Ponyta",'https://img.pokemondb.net/artwork/ponyta.jpg'],["Primeape",'https://img.pokemondb.net/artwork/primeape.jpg'],["Bulbasaur",'https://img.pokemondb.net/artwork/bulbasaur.jpg'],["Charmander",'https://img.pokemondb.net/artwork/charmander.jpg'],["Squirtle",'https://img.pokemondb.net/artwork/squirtle.jpg'],["Krabby",'https://img.pokemondb.net/artwork/krabby.jpg'],["Hypno",'https://img.pokemondb.net/artwork/hypno.jpg'],["Cloyster",'https://img.pokemondb.net/artwork/cloyster.jpg'],["Muk",'https://img.pokemondb.net/artwork/muk.jpg'],["Dewgong",'https://img.pokemondb.net/artwork/dewgong.jpg'],["Weepinbell",'https://img.pokemondb.net/artwork/weepinbell.jpg'],["Machoke",'https://img.pokemondb.net/artwork/machoke.jpg'],["Kadabra",'https://static.pokemonpets.com/images/monsters-images-300-300/64-Kadabra.png'],["Poliwhirl",'https://img.pokemondb.net/artwork/poliwhirl.jpg'],["Dugtrio",'https://img.pokemondb.net/artwork/dugtrio.jpg'],["Venomoth",'https://img.pokemondb.net/artwork/venomoth.jpg'],["Metapod",'https://img.pokemondb.net/artwork/metapod.jpg'],["Kakuna",'https://img.pokemondb.net/artwork/kakuna.jpg'],["Pidgeotto",'https://img.pokemondb.net/artwork/pidgeotto.jpg'],["Raticate",'https://img.pokemondb.net/artwork/raticate.jpg'],["Arbok",'https://img.pokemondb.net/artwork/arbok.jpg'],["Fearow",'https://img.pokemondb.net/artwork/fearow.jpg'],["Clefairy",'https://img.pokemondb.net/artwork/clefairy.jpg'],["Jigglypuff",'https://img.pokemondb.net/artwork/jigglypuff.jpg'],["Golbat",'https://img.pokemondb.net/artwork/golbat.jpg'],["Doduo",'https://img.pokemondb.net/artwork/doduo.jpg'],["Slobro",'https://img.pokemondb.net/artwork/slowbro.jpg'],["Gloom",'https://img.pokemondb.net/artwork/gloom.jpg'],["Parasect",'https://img.pokemondb.net/artwork/parasect.jpg'],["Tentacool",'https://img.pokemondb.net/artwork/tentacool.jpg'],["Graveler",'https://img.pokemondb.net/artwork/graveler.jpg'],["Marowak",'https://img.pokemondb.net/artwork/marowak.jpg'],["Weezing",'https://img.pokemondb.net/artwork/weezing.jpg'],["Rhydon",'https://img.pokemondb.net/artwork/rhydon.jpg'],["Chansey",'https://img.pokemondb.net/artwork/chansey.jpg'],["Seadra",'https://img.pokemondb.net/artwork/seadra.jpg'],["Seaking",'https://img.pokemondb.net/artwork/seaking.jpg'],["Scyther",'https://img.pokemondb.net/artwork/scyther.jpg'],["Magikarp",'https://img.pokemondb.net/artwork/magikarp.jpg'],["Eevee",'https://img.pokemondb.net/artwork/eevee.jpg'],["Omanyte",'https://img.pokemondb.net/artwork/omanyte.jpg'],["Kabuto",'https://img.pokemondb.net/artwork/kabuto.jpg'],["Dratini",'https://img.pokemondb.net/artwork/dratini.jpg']],
    'r': [["Raichu",'https://img.pokemondb.net/artwork/raichu.jpg'],["Nidoqueen",'https://img.pokemondb.net/artwork/nidoqueen.jpg'],["Nidoking",'https://img.pokemondb.net/artwork/nidoking.jpg'],["Ivysaur",'https://img.pokemondb.net/artwork/ivysaur.jpg'],["Wartortle",'https://img.pokemondb.net/artwork/wartortle.jpg'],["Charmeleon",'https://img.pokemondb.net/artwork/charmeleon.jpg'],["Butterfree",'https://img.pokemondb.net/artwork/butterfree.jpg'],["Beedrill",'https://img.pokemondb.net/artwork/beedrill.jpg'],["Pidgeot",'https://img.pokemondb.net/artwork/pidgeot.jpg'],["Clefable",'https://img.pokemondb.net/artwork/clefable.jpg'],["Wigglytuff",'https://img.pokemondb.net/artwork/wigglytuff.jpg'],["Vileplume",'https://img.pokemondb.net/artwork/vileplume.jpg'],["Golem",'https://img.pokemondb.net/artwork/golem.jpg'],["Victreebel",'https://img.pokemondb.net/artwork/victreebel.jpg'],["Poliwrath",'https://img.pokemondb.net/artwork/poliwrath.jpg'],["Tentacruel",'https://img.pokemondb.net/artwork/tentacruel.jpg'],["Rapidash",'https://img.pokemondb.net/artwork/rapidash.jpg'],["Dodrio",'https://img.pokemondb.net/artwork/dodrio.jpg'],["Kingler",'https://img.pokemondb.net/artwork/kingler.jpg'],["Exeggutor",'https://img.pokemondb.net/artwork/exeggutor.jpg'],["Hitmonlee",'https://img.pokemondb.net/artwork/hitmonlee.jpg'],["Hitmonchan",'https://img.pokemondb.net/artwork/hitmonchan.jpg'],["Lickitung",'https://img.pokemondb.net/artwork/lickitung.jpg'],["Starmie",'https://img.pokemondb.net/artwork/starmie.jpg'],["Mr.Mime",'https://img.pokemondb.net/artwork/mr-mime.jpg'],["Jynx",'https://img.pokemondb.net/artwork/jynx.jpg'],["Electabuzz",'https://img.pokemondb.net/artwork/electabuzz.jpg'],["Magmar",'https://img.pokemondb.net/artwork/magmar.jpg'],["Gyarados",'https://img.pokemondb.net/artwork/gyarados.jpg'],["Omastar",'https://img.pokemondb.net/artwork/omastar.jpg'],["Kabutops",'https://img.pokemondb.net/artwork/kabutops.jpg'],["Dragonair",'https://img.pokemondb.net/artwork/drangonair.jpg'],["Arcanine",'https://img.pokemondb.net/artwork/arcanine.jpg']],
    's': [["Venusaur",'https://img.pokemondb.net/artwork/venusaur.jpg'],["Charizard",'https://img.pokemondb.net/artwork/charizard.jpg'],["Blastoise",'https://img.pokemondb.net/artwork/blastoise.jpg'],["Alakazam",'https://img.pokemondb.net/artwork/alakazam.jpg'],["Onix",'https://img.pokemondb.net/artwork/onix.jpg'],["Machamp",'https://img.pokemondb.net/artwork/machamp.jpg'],["Farfetch'd",'https://img.pokemondb.net/artwork/farfetchd.jpg'],["Gengar",'https://img.pokemondb.net/artwork/gengar.jpg'],["Ninetales",'https://img.pokemondb.net/artwork/ninetales.jpg'],["Kangaskhan",'https://img.pokemondb.net/artwork/kangaskhan.jpg'],["Pinsir",'https://img.pokemondb.net/artwork/pinsir.jpg'],["Tauros",'https://img.pokemondb.net/artwork/tauros.jpg'],["Lapras",'https://img.pokemondb.net/artwork/lapras.jpg'],["Ditto",'https://img.pokemondb.net/artwork/ditto.jpg'],["Vaporeon",'https://img.pokemondb.net/artwork/vaporeon.jpg'],["Jolteon",'https://img.pokemondb.net/artwork/jolteon.jpg'],["Flareon",'https://img.pokemondb.net/artwork/flareon.jpg'],["Aerodactyl",'https://img.pokemondb.net/artwork/aerodactyl.jpg'],["Snorlax",'https://img.pokemondb.net/artwork/snorlax.jpg'],["Dragonite",'https://img.pokemondb.net/artwork/dragonite.jpg']],
    'l': [["Articuno",'https://img.pokemondb.net/artwork/articuno.jpg'],["Zapdos",'https://img.pokemondb.net/artwork/zapdos.jpg'],["Moltres",'https://img.pokemondb.net/artwork/moltres.jpg'],["Mewtwo",'https://img.pokemondb.net/artwork/mewtwo.jpg'],["Mew",'https://img.pokemondb.net/artwork/mew.jpg'],["Raikou",'https://img.pokemondb.net/artwork/raikou.jpg'],["Entei",'https://img.pokemondb.net/artwork/entei.jpg'],["Suicune",'https://img.pokemondb.net/artwork/suicune.jpg'],["Lugia",'https://img.pokemondb.net/artwork/lugia.jpg'],["Ho-oh",'https://img.pokemondb.net/artwork/ho-oh.jpg'],["Celebi",'https://img.pokemondb.net/artwork/celebi.jpg']]
}

ballTrans = {
    'pk:pb': 'Pokeball',
    'pk:gb': 'Greatball',
    'pk:ub': 'Ultraball',
    'pk:mb': 'Masterball'
}

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

rarityTrans = {
    'c': '🥉',
    'u': '🥈',
    'r': '🥇',
    's': '🎗',
    'l': '🎖'
}

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
            'bud': {},
            'dailytime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'spawn': False,
        }

buyskb = [{'Pokeball':'pkbuy:pb','Greatball':'pkbuy:gb'},{'Ultraball':'pkbuy:ub','Masterball':'pkbuy:mb'}]
buykb = util.getkb(buyskb)

buynumspbkb = [{'1':'pkbuynum:1:pb','2':'pkbuynum:2:pb','3':'pkbuynum:3:pb','4':'pkbuynum:4:pb'},{'5':'pkbuynum:5:pb','6':'pkbuynum:6:pb','7':'pkbuynum:7:pb','8':'pkbuynum:8:pb'},{'9':'pkbuynum:9:pb','10':'pkbuynum:10:pb','11':'pkbuynum:11:pb','12':'pkbuynum:12:pb'},{'13':'pkbuynum:13:pb','14':'pkbuynum:14:pb','15':'pkbuynum:15:pb','16':'pkbuynum:16:pb'},{'17':'pkbuynum:17:pb','18':'pkbuynum:18:pb','19':'pkbuynum:19:pb','20':'pkbuynum:20:pb'}]
buynumpbkb = util.getkb(buynumspbkb)

buynumsgbkb = [{'1':'pkbuynum:1:gb','2':'pkbuynum:2:gb','3':'pkbuynum:3:gb','4':'pkbuynum:4:gb'},{'5':'pkbuynum:5:gb','6':'pkbuynum:6:gb','7':'pkbuynum:7:gb','8':'pkbuynum:8:gb'},{'9':'pkbuynum:9:gb','10':'pkbuynum:10:gb','11':'pkbuynum:11:gb','12':'pkbuynum:12:gb'}]
buynumgbkb = util.getkb(buynumsgbkb)

buynumsubkb = [{'1':'pkbuynum:1:ub','2':'pkbuynum:2:ub','3':'pkbuynum:3:ub','4':'pkbuynum:4:ub'},{'5':'pkbuynum:5:ub','6':'pkbuynum:6:ub'}]
buynumubkb = util.getkb(buynumsubkb)

buynumsmbkb = [{'1':'pkbuynum:1:mb','2':'pkbuynum:2:mb','3':'pkbuynum:3:mb'}]
buynummbkb = util.getkb(buynumsmbkb)

def save():
    config.CONFIG["pk"] = game
    config.save_config()

def get_box(user):
    uid = str(user.id)
    msg = ''
    count = 0
    totalcount = 0
    numcount = 0
    for rarity in pokelist.rarity:
        for id in pokelist.rarity[rarity]:
            for pkdict in game[uid]['box']:
                if pkdict['name'] == pokelist.pokemon[id]['name']:
                    count += 1
                    totalcount += 1
            if count > 0:
                msg += f'{rarityTrans[rarity]}: {pokelist.pokemon[id]["name"]} #{id}: x{count}\n'
                numcount += 1
            count = 0
    msgsplit = msg.split('\n')
    msgcount = -1
    splitmsgs = []
    for msgs in msgsplit:
        msgcount += 1
        if msgcount % 10 == 0:
            splitmsgs.append(f'{user.first_name}\'s box: Page {int(msgcount/10)+1}\n~~~~~~~~~~~~~~~~~~~~\n🥉: Common\n🥈: Uncommon\n🥇: Rare\n🎗: Super rare\n🎖: Legendary\n~~~~~~~~~~~~~~~~~~~~')
        splitmsgs[int(msgcount/10)] += f'\n{msgs}'
    return splitmsgs,numcount,totalcount

def get_dex(user):
    uid = str(user.id)
    msg = ''
    count = 0
    totalsize = len(pokelist.pokemon)
    for id in pokelist.pokemon:
        for pkdict in game[uid]['box']:
            if pkdict['name'] == pokelist.pokemon[id]['name']:
                count += 1
        if count > 0:
            msg += f'✅ {pokelist.pokemon[id]["name"]} #{id}: x{count}\n'
        else:
            msg += f'❌ {pokelist.pokemon[id]["name"]} #{id}\n'
        count = 0
    msgsplit = msg.split('\n')
    msgcount = -1
    splitmsgs = []
    for msgs in msgsplit:
        msgcount += 1
        if msgcount % 15 == 0:
            splitmsgs.append(f'This pokedex lists every single one of the {totalsize} pokemon discovered so far.\n{user.first_name}, gotta catch\'em all©!\nPage {int(msgcount/15)+1}\n~~~~~~~~~~~~~~~~~~~~')
        splitmsgs[int(msgcount/15)] += f'\n{msgs}'
    return splitmsgs

def box(update,context):
    user = update.effective_user
    uid = str(user.id)
    chatid = update.effective_chat.id
    check_time(uid)
    splitmsgs,numcount,totalcount = get_box(user)
    pagenow = 1
    size = 10
    if pagenow * size > numcount:
        update.message.reply_text(splitmsgs[0])
    else:
        kb = util.getkb([{'➡️':f'pkbox:next:{pagenow+1}:{user.id}'}])
        update.message.reply_text(splitmsgs[0],reply_markup=kb)
    context.bot.send_message(chatid, text=f'You have {totalcount} pokemon in your box.')

def boxCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,direction,pagenow,curruid = query.data.split(':')
    if str(user.id) != curruid:
        query.answer("Yo dude this is someone else's box stop clicking these buttons!",show_alert=True)
        return
    size = 10
    splitmsgs,numcount,_ = get_box(user)
    if direction == 'next':
        if (int(pagenow)) * size > numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow-1)])
            else:
                kb = util.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = util.getkb([{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = util.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kb = util.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = util.getkb([{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = util.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)

def pokedex(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    msgs = get_dex(user)
    pagenow = 1
    kb = util.getkb([{'➡️':f'pkdex:next:{pagenow+1}:{user.id}'}])
    update.message.reply_text(msgs[0],reply_markup=kb)

def dexCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,direction,pagenow,curruid = query.data.split(':')
    if str(user.id) != curruid:
        query.answer("Yo dude this is someone else's pokedex stop clicking these buttons!",show_alert=True)
        return
    size = 15
    totalcount = len(pokelist.pokemon)
    splitmsgs = get_dex(user)
    if direction == 'next':
        if (int(pagenow)) * size > totalcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow-1)])
            else:
                kb = util.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = util.getkb([{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = util.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > totalcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kb = util.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = util.getkb([{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = util.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)

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

def add_bud(uid,p):  
    pdict = {'id':p.id,'name':p.name,'hp':p.hp,'atk':p.atk,'lvl':p.lvl,'xp':p.xp,'pktype':p.pktype,'upgrade':p.upgrade,'speed':p.speed}
    game[uid]['bud'] = pdict

def set_bud(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if game[uid]['bud'] == {}:
        kb = util.getkb([{'Bulbasaur':'pkbudstart:bulb'},{'Charmander':'pkbudstart:char'},{'Squirtle':'pkbudstart:squi'}])
        update.message.reply_photo('https://img.pokemondb.net/images/red-blue/kanto-starters.jpg',caption="Hi! My name is pokemon trainer BOTGOD. Someone told me that you wanted to become a master pokemon trainer. Well, I'm the person to seek. You can choose between 3 Kanto starter pokemon and return for more advice. Now, which pokemon would you like to have?",reply_markup=kb)
        return
    kblist = []
    for pkdict in game[uid]['box']:
        kblist.append({f"{pkdict['name']}, XP: {pkdict['xp']}":f"pkbudset:{game[uid]['box'].index(pkdict)}"})
    kb = util.getkb(kblist)
    update.message.reply_text("Which pokemon would you like to have as your buddy?",reply_markup=kb)

def budNewCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,index = query.data.split(':')
    game[uid]['bud'] = game[uid]['box'][int(index)]
    query.edit_message_text(f"{game[uid]['box'][int(index)]['name']}? He/she will be your best buddy! Use /view_bud@SichengsGodBot to have the details!")
    save()

def bud(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if game[uid]['bud'] == {}:
        update.message.reply_text('You do not have a buddy! Use /set_bud@SichengsGodBot to get one!')
    id = game[uid]['bud']['id']
    pk = pokelist.Pokemon(id,random.randint(pokelist.pokemon[id]['lvl'][0],pokelist.pokemon[id]['lvl'][1]))
    if game[uid]['bud']['upgrade'] == '':
        evo = 'This pokemon does not evolve.'
    else:
        evo = f"Evolves at level {pokelist.pokemon[game[uid]['bud']['id']]['lvl'][1]+1} into {pokelist.Pokemon(game[uid]['bud']['upgrade'],random.randint(pokelist.pokemon[game[uid]['bud']['upgrade']]['lvl'][0],pokelist.pokemon[game[uid]['bud']['upgrade']]['lvl'][1])).name}"
    types = ''
    for type in game[uid]['bud']['pktype']:
        types += f'{typeTrans[type]}'
    update.message.reply_photo(open(pk.getPhoto(),'rb'),caption=f"""Your {game[uid]['bud']['name']} {types}:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
XP: {game[uid]['bud']['xp']}
Level: {game[uid]['bud']['lvl']}
XP to next level: {game[uid]['bud']['lvl']*1000-game[uid]['bud']['xp']}
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
        budpk = pokelist.Pokemon(id='001',lvl=1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/bulbasaur.jpg'))
        query.edit_message_caption('Bulbasaur? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    elif pk == 'char':
        budpk = pokelist.Pokemon(id='004',lvl=1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/charmander.jpg'))
        query.edit_message_caption('Charmander? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    elif pk == 'squi':
        budpk = pokelist.Pokemon(id='007',lvl=1)
        pokemon_new.add_pokemon(uid,budpk)
        add_bud(uid,budpk)
        query.edit_message_media(InputMediaPhoto('https://img.pokemondb.net/artwork/squirtle.jpg'))
        query.edit_message_caption('Squirtle? Nice choice! He will be with you for the rest of your journey in Kanto. Good luck!')
    save()

def surprise(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'dailytime' in game[uid]:
        game[uid]['dailytime'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    dailytime = datetime.strptime(game[uid]['dailytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() >= dailytime:
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
            update.message.reply_text(f"Here are your daily pokecoins, {user.first_name}\n{c} pokecoins were pokelistd in your wallet.\nYou also got:\n{pb} Pokeballs\n{gb} Greatballs\n{ub} Ultraballs\n...and 1 Masterball\n这是您的每天打卡的 pokecoins，{user.first_name}\n{c} pokecoins已被放置在您的钱包中。")
        else:
            update.message.reply_text(f"Here are your daily pokecoins, {user.first_name}\n{c} pokecoins were pokelistd in your wallet.\nYou also got:\n{pb} Pokeballs\n{gb} Greatballs\n...and {ub} Ultraballs\n这是您的每天打卡的 pokecoins，{user.first_name}\n{c} pokecoins已被放置在您的钱包中。")
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
        BotCommand('box','Check the pokemon in your box! // 检查盒子里的宠物小精灵！'),
        BotCommand('pokeshop','Buy useful stuff for your adventure! // 为您的冒险购买有用的东西！'),
        BotCommand('view_bud','[BETA] Check on your buddy! // [测试] 检查您的好友！'),
        BotCommand('set_bud','[BETA] Get a new buddy! // [测试] 结识新好友！'),
        BotCommand('surprise','Get your daily injection of pokecoins! // 每天注射 Pokecoins！'),
        BotCommand('pokebal','Check the amount of pokecoins you have. // 检查您有多少 pokecoins。'),
        BotCommand('pokedex','Check the pokemon you have. // 检查您有的 pokemon。')
    ]

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('box', box))
    dispatcher.add_handler(CommandHandler('pokeshop',shop))
    dispatcher.add_handler(CommandHandler('view_bud',bud))
    dispatcher.add_handler(CommandHandler('set_bud',set_bud))
    dispatcher.add_handler(CommandHandler('surprise',surprise))
    dispatcher.add_handler(CommandHandler('pokebal',bal))
    dispatcher.add_handler(CommandHandler('reset',reset))
    dispatcher.add_handler(CommandHandler('pokedex',pokedex))
    dispatcher.add_handler(CallbackQueryHandler(shopCallback,pattern="^pkbuy:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(shopnumCallback,pattern="^pkbuynum:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(boxCallback,pattern="^pkbox:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(dexCallback,pattern="^pkdex:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(budStartCallback,pattern="^pkbudstart:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(budNewCallback,pattern="^pkbudset:[A-Za-z0-9_]*"))