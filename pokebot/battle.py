import random
import pokeconfig
import pokemon_new
import pokelist,movelist,trainerlist
import pokeutils
import pokemons
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand, InputMediaPhoto
from datetime import datetime,timedelta

game = pokeconfig.CONFIG["pk"]

unlockTrans = {
    '0': '🔓 [UNLOCKED] Gym Trainer\n🔐 [LOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '1': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '2': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '3': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '4': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '5': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '6': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '7': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '8': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔐 [LOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '9': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '10': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔐 [LOCKED] Champion',
    '11': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔓 [UNLOCKED] Champion',
    '12': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔓 [UNLOCKED] Champion',
    '13': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔓 [UNLOCKED] Champion',
    '14': '🔓 [UNLOCKED] Gym Trainer\n🔓 [UNLOCKED] Gym Leader\n🔓 [UNLOCKED] Elite 4\n🔓 [UNLOCKED] Champion'
}

unlockkbs = {
    '0': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'}],
    '1': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '2': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '3': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '4': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '5': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '6': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '7': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '8': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'}],
    '9': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'}],
    '10': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'}],
    '11': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'},{'Challenge a Champion!':'pkbattlechoose:champ'}],
    '12': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'},{'Challenge a Champion!':'pkbattlechoose:champ'}],
    '13': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'},{'Challenge a Champion!':'pkbattlechoose:champ'}],
    '14': [{'Challenge a Gym Trainer!':'pkbattlechoose:train'},{'Challenge a Gym Leader!':'pkbattlechoose:lead'},{'Challenge an Elite Four!':'pkbattlechoose:e4'},{'Challenge a Champion!':'pkbattlechoose:champ'}]
}

statusTrans = {
    'con': '🌀 Confused',
    'bur': '🔥 Burned',
    '': 'NO SPECIAL STATUS',
    'par': '⚡️ Paralysed',
}

def get_choice(choice,user):
    uid = str(user.id)
    trainers = ['Sunny','Maggie','Wally','Elenia','Parker','Elsa','Gordon','Velenu','Grady','Celine','Rick','Gherma','Steven','Draco']
    trainer = random.choice(trainers)
    choicekbs = {
        'train': [{f'Battle the current Gym Trainer ({trainer})!':f'pkbattlestart:train:{trainer}'},{'Never mind...':f'pkbattlerestart:{uid}'}],
        'lead': [{'I':'pkbattlegen:lead:1','II':'pkbattlegen:lead:2','III':'pkbattlegen:lead:3'},{'IV':'pkbattlegen:lead:4','V':'pkbattlegen:lead:5','VI':'pkbattlegen:lead:6'},{'Never mind...':f'pkbattlerestart:{uid}'}],
        'e4': [{'I':'pkbattlegen:e4:1','II':'pkbattlegen:e4:2','III':'pkbattlegen:e4:3'},{'IV':'pkbattlegen:e4:4','V':'pkbattlegen:e4:5','VI':'pkbattlegen:e4:6'},{'Never mind...':f'pkbattlerestart:{uid}'}],
        'champ': [{'I':'pkbattlegen:champ:1','II':'pkbattlegen:champ:2','III':'pkbattlegen:champ:3'},{'IV':'pkbattlegen:champ:4','V':'pkbattlegen:champ:5','VI':'pkbattlegen:champ:6'},{'Never mind...':f'pkbattlerestart:{uid}'}]
    }
    if choice == 'train':
        choicetext = f"The current trainer in the gym is {trainer}. Click on the 'Never mind' button and re-click on the trainer button the get a new Gym Trainer (if you are lucky)."
    elif choice == 'lead':
        choicetext = f"Which generation of Gym Leaders would you like to battle with, {user.first_name}?"
    elif choice == 'e4':
        choicetext = f"Which generation of Elite Fours would you like to battle with, {user.first_name}?"
    elif choice == 'champ':
        choicetext = f"Which generation of Champions would you like to battle with, {user.first_name}?"
    kb = pokeutils.getkb(choicekbs[choice])
    return choicetext,kb

def get_choice_gen(choice,user,gen):
    uid = str(user.id)
    choicekbs = {
        'lead': [{'Back ⏪':'pkbattlechoose:lead'}],
        'e4': [{'Back ⏪':'pkbattlechoose:e4'}],
        'champ': [{'Start!':f'pkbattlestart:champ:{gen}'},{'Back ⏪':'pkbattlechoose:champ'}]
    }
    if choice == 'lead':
        choicetext = 'Which Gym Leader do you wish to battle?'
        for key in trainerlist.trainers:
            if int(key) < 100:
                if int(key) < int(gen)*10 and int(key) > (int(gen)-1)*10 :
                    if (int(key) - (int(gen)-1)*10)-1 <= game[uid]['leaderprogress']:
                        choicetext += f"\n{key}. {trainerlist.trainers[key]['name']}"
                        choicekbs['lead'].append({f'{key}':f'pkbattlestart:lead:{key}'})
    elif choice == 'e4':
        choicetext = 'Which Elite Four do you wish to battle?'
        for key in trainerlist.trainers:
            if int(key) > 100 and int(key) < 150:
                if int(key) < 100+int(gen)*5 and int(key) > 100+(int(gen)-1)*5:
                    if (int(key) - (int(gen)-1)*10)-101 <= game[uid]['e4progress']:
                        choicetext += f"\n{key}. {trainerlist.trainers[key]['name']}"
                        choicekbs['e4'].append({f'{key}':f'pkbattlestart:e4:{key}'})
    elif choice == 'champ':
        choicetext = f"Ready to go, {user.first_name}?"
    kb = pokeutils.getkb(choicekbs[choice])
    return kb,choicetext

def get_move_buttons(moves):
    buttons = []
    for move in moves:
        buttons.append(InlineKeyboardButton(move,callback_data=f'pkbattlemove:{move}'))
    return buttons

def save():
    pokeconfig.CONFIG["pk"] = game
    pokeconfig.save_config()

def battle_menu(update,context):
    user = update.effective_user
    uid = str(user.id)
    pokemons.check_time(uid)
    kb = pokeutils.getkb(unlockkbs[game[uid]['tier']])
    update.message.reply_text(f"Current user tier: {game[uid]['tier']}\n~~~~~~~~~~~~~~~~~~~~~~\nCurrent unlocks:\n{unlockTrans[game[uid]['tier']]}\n~~~~~~~~~~~~~~~~~~~~~~\nDon't forget, if you are progressing in Alola or Galar, you can still battle here, but to advance in those territories, use the commands /battle_alola or /battle_galar !",reply_markup=kb)

def battle_choose(update,context):
    user = update.effective_user
    query = update.callback_query
    _, choice = query.data.split(':')
    msg,kb = get_choice(choice,user)
    query.edit_message_text(msg,reply_markup=kb)

def battle_choose_gen(update,context):
    user = update.effective_user
    query = update.callback_query
    _, choice, gen = query.data.split(':')
    kb,msg = get_choice_gen(choice,user,gen)
    query.edit_message_text(msg,reply_markup=kb)

def battle(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _, type, choice = query.data.split(':')
    if type == 'train':
        pass
    elif type == 'lead':
        opponent_party = trainerlist.trainers[choice]['party']
        party = game[uid]['party']
        query.edit_message_text("Battle started!")
        currentpk_index = 0
        current_opponent_pk_index = 0
        current_opponent_pk = pokelist.Pokemon(opponent_party[current_opponent_pk_index]['id'],opponent_party[current_opponent_pk_index]['xp'],-1,opponent_party[current_opponent_pk_index]['moves'])
        context.bot.send_media_group(chat_id=update.effective_chat.id,media=[InputMediaPhoto(open(pokelist.Pokemon(party[currentpk_index]['id'],0,-1,[]).getPhoto(),'rb'),caption=f"{user.first_name} VS {trainerlist.trainers[choice]['name']}"),InputMediaPhoto(open(current_opponent_pk.getPhoto(),'rb'))])
        context.bot.send_message(chat_id=update.effective_chat.id,text=f"""{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
Status: {statusTrans[party[currentpk_index]['status']]}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
Status: {statusTrans[current_opponent_pk.status]}
====================
Which move do you want to use?""",reply_markup=InlineKeyboardMarkup([get_move_buttons(party[currentpk_index]['moves'])]))

def restart(update,context):
    user = update.effective_user
    uid = str(user.id)
    _, curruid = update.callback_query.data.split(':')
    query = update.callback_query
    if uid != curruid:
        query.answer("你是谁？你在哪儿？你想做啥？这是别人的，大笨蛋！",show_alert=True)
        return
    kb = pokeutils.getkb(unlockkbs[game[uid]['tier']])
    query.edit_message_text(f"Current user tier: {game[uid]['tier']}\n~~~~~~~~~~~~~~~~~~~~~~\nCurrent unlocks:\n{unlockTrans[game[uid]['tier']]}\n~~~~~~~~~~~~~~~~~~~~~~\nDon't forget, if you are progressing in Alola or Galar, you can still battle here, but to advance in those territories, use the commands /battle_alola or /battle_galar !",reply_markup=kb)

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('battle', battle_menu))
    dispatcher.add_handler(CallbackQueryHandler(battle_choose,pattern="^pkbattlechoose:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(battle_choose_gen,pattern="^pkbattlegen:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(restart,pattern="^pkbattlerestart:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(battle,pattern="^pkbattlestart:[A-Za-z0-9_]*"))