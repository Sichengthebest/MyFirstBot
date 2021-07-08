import random
import pokeconfig
import pokemon_new
import pokelist
import pokeutils
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

rarityTrans = {
    'c': '🥉',
    'u': '🥈',
    'r': '🥇',
    's': '🎗',
    'l': '🎖',
    'ss': '💫',
    'ee': '🏆'
}

game = pokeconfig.CONFIG["pk"]

def check_time(uid):
    if not uid in game:
        game[uid] = {
            'gametime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            "tier": "0",
            'pb': 10,
            'gb': 5,
            'ub': 3,
            'mb': 1,
            'pokecoins': 0,
            'box': [],
            'bud': {},
            'dailytime': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'spawn': False,
            "inv": [],
            "party": [
                {},
                {},
                {},
                {},
                {},
                {}
            ],
            "trainerprogress": 0,
            "leaderprogress": 0,
            "e4progress": 0,
            "champprogress": 0
        }

buyskb = [{'Pokeball':'pkbuy:pb','Greatball':'pkbuy:gb'},{'Ultraball':'pkbuy:ub','Masterball':'pkbuy:mb'}]
buykb = pokeutils.getkb(buyskb)

buynumspbkb = [{'1':'pkbuynum:1:pb','2':'pkbuynum:2:pb','3':'pkbuynum:3:pb','4':'pkbuynum:4:pb'},{'5':'pkbuynum:5:pb','6':'pkbuynum:6:pb','7':'pkbuynum:7:pb','8':'pkbuynum:8:pb'},{'9':'pkbuynum:9:pb','10':'pkbuynum:10:pb','11':'pkbuynum:11:pb','12':'pkbuynum:12:pb'},{'13':'pkbuynum:13:pb','14':'pkbuynum:14:pb','15':'pkbuynum:15:pb','16':'pkbuynum:16:pb'},{'17':'pkbuynum:17:pb','18':'pkbuynum:18:pb','19':'pkbuynum:19:pb','20':'pkbuynum:20:pb'}]
buynumpbkb = pokeutils.getkb(buynumspbkb)

buynumsgbkb = [{'1':'pkbuynum:1:gb','2':'pkbuynum:2:gb','3':'pkbuynum:3:gb','4':'pkbuynum:4:gb'},{'5':'pkbuynum:5:gb','6':'pkbuynum:6:gb','7':'pkbuynum:7:gb','8':'pkbuynum:8:gb'},{'9':'pkbuynum:9:gb','10':'pkbuynum:10:gb','11':'pkbuynum:11:gb','12':'pkbuynum:12:gb'}]
buynumgbkb = pokeutils.getkb(buynumsgbkb)

buynumsubkb = [{'1':'pkbuynum:1:ub','2':'pkbuynum:2:ub','3':'pkbuynum:3:ub','4':'pkbuynum:4:ub'},{'5':'pkbuynum:5:ub','6':'pkbuynum:6:ub'}]
buynumubkb = pokeutils.getkb(buynumsubkb)

buynumsmbkb = [{'1':'pkbuynum:1:mb','2':'pkbuynum:2:mb','3':'pkbuynum:3:mb'}]
buynummbkb = pokeutils.getkb(buynumsmbkb)

def save():
    pokeconfig.CONFIG["pk"] = game
    pokeconfig.save_config()

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
            splitmsgs.append(f'{user.first_name}\'s box: Page {int(msgcount/10)+1}\n~~~~~~~~~~~~~~~~~~~~\n🥉: Common\n🥈: Uncommon\n🥇: Rare\n🎗: Super rare\n🎖: Legendary\n💫: Special Spawn\n🏆: Exclusive Evolution\n~~~~~~~~~~~~~~~~~~~~')
        splitmsgs[int(msgcount/10)] += f'\n{msgs}'
    return splitmsgs,numcount,totalcount

def get_dex(user):
    uid = str(user.id)
    msg = ''
    count = 0
    eachcount = 0
    totalsize = len(pokelist.pokemon)
    for id in pokelist.pokemon:
        for pkdict in game[uid]['box']:
            if pkdict['name'] == pokelist.pokemon[id]['name']:
                count += 1
        if count > 0:
            msg += f'✅ {pokelist.pokemon[id]["name"]} #{id}: x{count}\n'
            eachcount += 1
        else:
            msg += f'❌ {pokelist.pokemon[id]["name"]} #{id}\n'
        count = 0
    msgsplit = msg.split('\n')
    msgcount = -1
    splitmsgs = []
    for msgs in msgsplit:
        msgcount += 1
        if msgcount % 15 == 0:
            splitmsgs.append(f'This pokedex lists every single one of the {totalsize} pokemon discovered so far (including formes).\nYou have caught {eachcount} of {totalsize} pokemon.\n{user.first_name}, gotta catch\'em all©!\nPage {int(msgcount/15)+1}\n~~~~~~~~~~~~~~~~~~~~')
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
        kb = pokeutils.getkb([{'➡️':f'pkbox:next:{pagenow+1}:{user.id}'}])
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
                kb = pokeutils.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = pokeutils.getkb([{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = pokeutils.getkb([{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkbox:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkbox:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)

def pokedex(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    msgs = get_dex(user)
    pagenow = 1
    kb = pokeutils.getkb([{'➡️':f'pkdex:next:{pagenow+1}:{user.id}'}])
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
                kb = pokeutils.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = pokeutils.getkb([{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > totalcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kb = pokeutils.getkb([{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kb = pokeutils.getkb([{'⬅️':f'pkdex:prev:{int(pagenow)-1}:{user.id}'},{'➡️':f'pkdex:next:{int(pagenow)+1}:{user.id}'}])
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
    update.message.reply_text(f"""Welcome to the PokeMart! Buy some items for your adventure!
{user.first_name}'s pokeCoins: {game[uid]['pokecoins']}
-------------------------
You currently own:
{game[uid]['pb']} Pokeballs
{game[uid]['gb']} Greatballs
{game[uid]['ub']} Ultraballs
{game[uid]['mb']} Masterballs
-------------------------
Pokeball: 200 pokecoins
Greatball: 600 pokecoins
Ultraball: 1200 pokecoins
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

def shopnumCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,num,ball = query.data.split(':')
    if ball == 'pb':
        c = 200
    elif ball == 'gb':
        c = 600
    elif ball == 'ub':
        c = 1200
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
    save()
    username = user.username
    if username == None:
        username = user.first_name
    return f"Success! @{username} , you have bought {num} {ballTrans[f'pk:{ball}']}(s) with {totalcost} pokecoins and you have {game[uid]['pokecoins']} pokecoins remaining.\nYou now have {game[uid]['pb']} Pokeballs, {game[uid]['gb']} Greatballs, {game[uid]['ub']} Ultraballs and {game[uid]['mb']} Masterballs."

def surprise(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    if not 'dailytime' in game[uid]:
        game[uid]['dailytime'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    dailytime = datetime.strptime(game[uid]['dailytime'],"%Y/%m/%d %H:%M:%S")
    if datetime.now() >= dailytime:
        c = random.randint(100,500)
        pb = random.randint(3,12)
        gb = random.randint(0,4)
        ub = random.randint(0,2)
        game[uid]['pokecoins'] += c
        game[uid]['pb'] += pb
        game[uid]['gb'] += gb
        game[uid]['ub'] += ub
        update.message.reply_text(f"Here are your daily pokecoins, {user.first_name}\n{c} pokecoins were placed in your wallet.\nYou also got:\n{pb} Pokeballs\n{gb} Greatballs\n...and {ub} Ultraballs")
        dailytime = datetime.now() + timedelta(days=1)
        game[uid]['dailytime'] = dailytime.strftime("%Y/%m/%d %H:%M:%S")
    else:
        update.message.reply_text("Slow it down, cmon!!! I'm not made of money dude, one day hasn't passed yet!") 
    save()

def reset(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    game[uid]['spawn'] = False
    update.message.reply_text("You have reset your pokemon.")
    save()

def inv(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    msg = 'Your bag:\n---------------'
    if game[uid]['inv'] == []:
        msg += '\nYou have nothing in your bag!'
    for thing in game[uid]['inv']:
        msg += f'\n{pokemon_new.stoneTrans[thing]}'
    update.message.reply_text(msg)

def profile(update,context):
    user = update.effective_user
    uid = str(user.id)
    eachcount = 0
    count = 0
    for id in pokelist.pokemon:
        for pkdict in game[uid]['box']:
            if pkdict['name'] == pokelist.pokemon[id]['name']:
                count += 1
        if count > 0:
            eachcount += 1
        count = 0
    totalsize = len(pokelist.pokemon)
    update.message.reply_text(f"{user.first_name}'s profile:\n~~~~~~~~~~~~~~~\nTier: {game[uid]['tier']}\nYou have caught {eachcount} pokemon on {totalsize} pokemon.")

def get_release_text(user):
    uid = str(user.id)
    msg = ''
    numcount = 0
    for pkdict in game[uid]['box']:
        msg += f'{pkdict["name"]} #{pkdict["id"]}, XP:{pkdict["xp"]}\n'
        numcount += 1
    msgsplit = msg.split('\n')
    msgcount = -1
    splitmsgs = []
    for msgs in msgsplit:
        msgcount += 1
        if msgcount % 5 == 0:
            splitmsgs.append(f'{user.first_name}, which pokemon would you like to release? Page {int(msgcount/5)+1}\n~~~~~~~~~~~~~~~~~~~~')
        splitmsgs[int(msgcount/5)] += f'\n{msgs}'
    return splitmsgs,numcount

def get_release_members(uid,pagenow):
    kblist = []
    kbstart = (pagenow-1)*5
    kbend = kbstart + 5
    for index in range(kbstart,kbend):
        if index > len(game[uid]['box'])-1:
            return kblist
        kblist.append({f"{game[uid]['box'][index]['name']}, XP: {game[uid]['box'][index]['xp']}":f"pkrelease:{index}"})
    return kblist

def release(update,context):
    user = update.effective_user
    uid = str(user.id)
    check_time(uid)
    pagenow = 1
    size = 5
    kblist = get_release_members(uid,pagenow)
    kb = []
    splitmsgs,numcount = get_release_text(user)
    if len(context.args) == 1:
        oldpk = context.args[0].replace('_',' ')
        lala = False
        pk = oldpk.title().replace(' ','-')
        count = 0
        counts = []
        buttons = []
        for pkdict in game[uid]['box']:
            if pk == pkdict['name']:
                lala = True
                counts.append(count)
            count += 1
        if not lala:
            update.message.reply_text('This pokemon is not in your box!')
            return
        for index in counts:
            buttons.append({f"{game[uid]['box'][index]['name']}, XP: {game[uid]['box'][index]['xp']}":f"pkrelease:{index}"})
        kb = pokeutils.getkb(buttons)
        update.message.reply_text(f'Which {pk} are you choosing?',reply_markup=kb)
        return
    if pagenow * size > numcount:
        kb = pokeutils.getkb(kblist)
        update.message.reply_text(splitmsgs[0],reply_markup=kb)
    else:
        kblist.append({'➡️':f'pkreleasepages:next:{pagenow+1}:{user.id}'})
        kb = pokeutils.getkb(kblist)
        update.message.reply_text(splitmsgs[0],reply_markup=kb)

def releasePagesCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,direction,pagenow,curruid = query.data.split(':')
    if str(user.id) != curruid:
        query.answer("Yo dude this is someone else's releasing stop clicking these buttons!",show_alert=True)
        return
    size = 5
    splitmsgs,numcount = get_release_text(user)
    kblist = get_release_members(str(user.id),int(pagenow))
    if direction == 'next':
        if (int(pagenow)) * size >= numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow-1)])
            else:
                kblist.append({'⬅️':f'pkreleasepages:prev:{int(pagenow)-1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kblist.append({'➡️':f'pkreleasepages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kblist.append({'⬅️':f'pkreleasepages:prev:{int(pagenow)-1}:{user.id}'})
                kblist.append({'➡️':f'pkreleasepages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kblist.append({'⬅️':f'pkreleasepages:prev:{int(pagenow)-1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kblist.append({'➡️':f'pkreleasepages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kblist.append({'⬅️':f'pkreleasepages:prev:{int(pagenow)-1}:{user.id}'})
                kblist.append({'➡️':f'pkreleasepages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)

def releaseCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,index = query.data.split(':')
    released = {'c':0,'u':0,'r':0,'s':0,'l':0,'ss':0}
    releasedTrans = {'c':20,'u':35,'r':60,'s':120,'l':1500,'ss':2500}
    amount = 0
    for rarity in pokelist.rarity:
        for id in pokelist.rarity[rarity]:
            if id == game[uid]['box'][int(index)]['id']:
                released[rarity] += 1
    for rare in released:
        amount += releasedTrans[rare]*released[rare]
    game[uid]['pokecoins'] += amount
    query.edit_message_text(f"{game[uid]['box'][int(index)]['name']} has been released. You earned {amount} pokecoins.")
    game[uid]['box'].remove(game[uid]['box'][int(index)])
    save()

#def releaseDuplicates(update,context):
#    user = update.effective_user
#    uid = str(user.id)
#    query = update.callback_query
#    _,curruid = query.data.split(':')
#    if str(uid) != curruid:
#        query.answer("Yo dude this is someone else's releasing stop clicking these buttons!",show_alert=True)
#        return
#    duplicates = []
#    released = {'c':0,'u':0,'r':0,'s':0}
#    for pkdict in game[uid]['box']:
#        if pkdict['id'] in duplicates:
#            game[uid]['box'].remove(pkdict)
#        else:
#            duplicates.append(pkdict['id'])
#    amount = 0
#    game[uid]['pokecoins'] += amount
#    query.edit_message_text(f"You have released:\nx{released['c']} common pokemon;\nx{released['u']} uncommon pokemon;\nx{released['r']} rare pokemon...\n...and x{released['s']} super rare pokemon.\nYou earned {amount} pokecoins.")
#    save()

def getCommand():
    return [
        BotCommand('pokemon','Go catch pokemon!'),
        BotCommand('box','Check the pokemon in your box!'),
        BotCommand('pokemart','Buy useful stuff for your adventure!'),
        BotCommand('view_bud','Check on your buddy!'),
        BotCommand('set_bud','Get a new buddy!'),
        BotCommand('surprise','Get your daily injection of pokecoins!'),
        BotCommand('bal','Check the amount of pokecoins you have.'),
        BotCommand('pokedex','Check the pokemon you have.'),
        BotCommand('bag','Check the items you have.'),
        BotCommand('evolve','Evolve your pokemon!'),
        BotCommand('add_party_member','Add pokemon into your party!'),
        BotCommand('view_party','Check your party.'),
        BotCommand('profile','View your profile.'),
        BotCommand('release','Release useless pokemon.'),
        BotCommand('battle','[BETA] Start battling other trainers\'s pokemon!'),
        BotCommand('add_moves','Add moves to your pokemon!'),
        BotCommand('view_moves','Check your buddy\'s moves!')
    ]

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('box', box))
    dispatcher.add_handler(CommandHandler('bag', inv))
    dispatcher.add_handler(CommandHandler('pokemart',shop))
    dispatcher.add_handler(CommandHandler('surprise',surprise))
    dispatcher.add_handler(CommandHandler('bal',bal))
    dispatcher.add_handler(CommandHandler('reset',reset))
    dispatcher.add_handler(CommandHandler('pokedex',pokedex))
    dispatcher.add_handler(CommandHandler('profile',profile))
    dispatcher.add_handler(CommandHandler('release',release))
    dispatcher.add_handler(CallbackQueryHandler(shopCallback,pattern="^pkbuy:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(shopnumCallback,pattern="^pkbuynum:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(boxCallback,pattern="^pkbox:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(dexCallback,pattern="^pkdex:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(releaseCallback,pattern="^pkrelease:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(releasePagesCallback,pattern="^pkreleasepages:[A-Za-z0-9_]*"))
#    dispatcher.add_handler(CallbackQueryHandler(releaseDuplicates,pattern="^pkreleasedup:[A-Za-z0-9_]*"))