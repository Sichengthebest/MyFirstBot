import random
import pokeconfig
import pokelist,movelist,trainerlist
import pokeutils
import pokemons
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

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
    trainertrans = {'Sunny':1000,'Maggie':1001,'Wally':1002,'Elenia':1003,'Parker':1004,'Elsa':1005,'Gordon':1006,'Velenu':1007,'Grady':1008,'Celine':1009,'Rick':1010,'Gherma':1011,'Steven':1012,'Draco':1013}
    trainer = random.choice(trainers)
    choicekbs = {
        'train': [{f'Battle the current Gym Trainer ({trainer})!':f'pkbattlestart:train:{trainertrans[trainer]}'},{'Never mind...':f'pkbattlerestart:{uid}'}],
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

def get_move_buttons(moves,index,opponent_index,choice,copk):
    buttons = []
    for move in moves:
        buttons.append({move:f'pkbattlemove:{move}:{index}:{opponent_index}:{choice}:{copk.hp}:{copk.currhp}:{copk.status}:{copk.atk}:{copk.defence}:{copk.speed}'})
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

def battle_start(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _, type, choice = query.data.split(':')
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
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
Which move would you like to use?""",reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))

def battle_move(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _, move, currentpk_index_str, current_opponent_pk_index_str,choice,current_opponent_pk_hp,current_opponent_pk_currhp,current_opponent_pk_status,current_opponent_pk_atk,current_opponent_pk_def,current_opponent_pk_speed = query.data.split(':')
    currentpk_index = int(currentpk_index_str)
    current_opponent_pk_index = int(current_opponent_pk_index_str)
    opponent_party = trainerlist.trainers[choice]['party']
    party = game[uid]['party']
    lvl = int(opponent_party[current_opponent_pk_index]['xp']/1000)+1
    current_opponent_pk = pokelist.Pokemon.init(
        opponent_party[current_opponent_pk_index]['id'],
        pokelist.pokemon[opponent_party[current_opponent_pk_index]['id']]['name'],
        lvl,
        int(current_opponent_pk_hp),
        int(current_opponent_pk_currhp),
        int(float(current_opponent_pk_atk)),
        pokelist.pokemon[opponent_party[current_opponent_pk_index]['id']]['pktype'],
        random.choice(pokelist.pokemon[opponent_party[current_opponent_pk_index]['id']]['upgrade']),
        int(float(current_opponent_pk_def)),
        int(float(current_opponent_pk_speed)),
        opponent_party[current_opponent_pk_index]['xp'],
        pokelist.pokemon[opponent_party[current_opponent_pk_index]['id']]['evolvewith'],
        100,
        current_opponent_pk_status,
        opponent_party[current_opponent_pk_index]['moves']
    )
    opponent_move = random.choice(trainerlist.trainers[choice]['party'][current_opponent_pk_index]['moves'])
    # priority
    priority = movelist.moves[move]['priority']
    opponent_move_priority = movelist.moves[opponent_move]['priority']
    if priority == opponent_move_priority:
        if party[currentpk_index]['speed'] == current_opponent_pk.speed:
            first = random.randint(1,2)
        elif party[currentpk_index]['speed'] > current_opponent_pk.speed:
            first = 1
        else:
            first = 2
    elif priority > opponent_move_priority:
        first = 1
    else:
        first = 2
    # damage
    p,raisenum,eraisenum = calculate_power(pokelist.Pokemon.init_from_dict(party[currentpk_index]),current_opponent_pk,move)
    opponent_p,opponent_raisenum,opponent_eraisenum = calculate_power(current_opponent_pk,pokelist.Pokemon.init_from_dict(party[currentpk_index]),opponent_move)
    msg = ''
    if first == 1:
        # if you go first
        current_opponent_pk.currhp -= p
        party[currentpk_index]['atk'] += raisenum[0]
        party[currentpk_index]['defence'] += raisenum[1]
        party[currentpk_index]['speed'] += raisenum[0]
        current_opponent_pk.atk -= eraisenum[0]
        current_opponent_pk.defence -= eraisenum[1]
        current_opponent_pk.speed -= eraisenum[0]
        if current_opponent_pk.currhp < 1:
            # if opponent faints
            dead_name = current_opponent_pk.name
            current_opponent_pk_index += 1
            if current_opponent_pk_index >= len(opponent_party):
                # if it's opponent's last pokemon
                msg += f"""{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {dead_name} fainted!"""
                query.edit_message_text(msg)
                coinsnum = random.randint(1000,5000)
                xpnum = 0
                for pkmon in opponent_party:
                    xpnum += pkmon['xp']/1000*57
                for pkm in party:
                    pkm['xp'] += xpnum
                game[uid]['pokecoins'] += coinsnum
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name}, you won against {trainerlist.trainers[choice]['name']}! You earned {coinsnum} pokecoins and {xpnum} XP (for each of your pokemon)!")
                index = 0
                for pkmo in game[uid]['party']:
                    boxindex = game[uid]['box'].index(pkmo)
                    game[uid]['box'][boxindex] = party[index]
                    if pkmo == game[uid]['bud']:
                        game[uid]['bud'] = party[index]
                    index += 1
                for pkmon in party:
                    if pkmon['currhp'] < 1:
                        party[party.index(pkmon)] = {}
                print(party)
                game[uid]['party'] = party
                save()
                return
            # if not opponent's last pokemon
            current_opponent_pk = pokelist.Pokemon(opponent_party[current_opponent_pk_index]['id'],opponent_party[current_opponent_pk_index]['xp'],-1,opponent_party[current_opponent_pk_index]['moves'])
            msg += f"""{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {dead_name} fainted!
{trainerlist.trainers[choice]['name']} sent out {current_opponent_pk.name}!
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
Which move would you like to use?"""
            query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
        else:
            # if opponent doesn't faint
            party[currentpk_index]['currhp'] -= opponent_p
            party[currentpk_index]['atk'] -= opponent_eraisenum[0]
            party[currentpk_index]['defence'] -= opponent_eraisenum[1]
            party[currentpk_index]['speed'] -= opponent_eraisenum[2]
            current_opponent_pk.atk += opponent_raisenum[0]
            current_opponent_pk.defence += opponent_raisenum[0]
            current_opponent_pk.speed += opponent_raisenum[0]
            if party[currentpk_index]['currhp'] < 1:
                # if you faint
                my_dead_name = party[currentpk_index]['name']
                currentpk_index += 1
                if currentpk_index >= len(party):
                    # if it's your last pokemon
                    msg += f"""{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {my_dead_name} fainted!"""
                    query.edit_message_text(msg)
                    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name}, you lost against {trainerlist.trainers[choice]['name']}!")
                    game[uid]['party'] = party
                    save()
                    return
                # if it's not your last pokemon
                msg += f"""{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {my_dead_name} fainted!
{user.first_name} sent out {party[currentpk_index]['name']}!
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
Which move would you like to use?"""
                query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
            else:
                # if you don't faint
                msg += f"""{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
Which move would you like to use?"""
                query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
    else:
        # if opponent goes first
        party[currentpk_index]['currhp'] -= opponent_p
        party[currentpk_index]['atk'] -= opponent_eraisenum[0]
        party[currentpk_index]['defence'] -= opponent_eraisenum[1]
        party[currentpk_index]['speed'] -= opponent_eraisenum[2]
        current_opponent_pk.atk += opponent_raisenum[0]
        current_opponent_pk.defence += opponent_raisenum[0]
        current_opponent_pk.speed += opponent_raisenum[0]
        if party[currentpk_index]['currhp'] < 1:
            # if you faint
            my_dead_name = party[currentpk_index]['name']
            currentpk_index += 1
            if currentpk_index >= len(party):
                # if it's your last pokemon
                msg += f"""{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {my_dead_name} fainted!
===================="""
                query.edit_message_text(msg)
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name}, you lost against {trainerlist.trainers[choice]['name']}!")
                game[uid]['party'] = party
                save()
                return
            # if it's not your last pokemon
            msg += f"""{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {my_dead_name} fainted!
{user.first_name} sent out {party[currentpk_index]['name']}!
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
Which move would you like to use?"""
            query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
        else:
            # if you don't faint
            current_opponent_pk.currhp -= p
            party[currentpk_index]['atk'] += raisenum[0]
            party[currentpk_index]['defence'] += raisenum[1]
            party[currentpk_index]['speed'] += raisenum[0]
            current_opponent_pk.atk -= eraisenum[0]
            current_opponent_pk.defence -= eraisenum[1]
            current_opponent_pk.speed -= eraisenum[0]
            if current_opponent_pk.currhp < 1:
                # if opponent faints
                dead_name = current_opponent_pk.name
                current_opponent_pk_index += 1
                if current_opponent_pk_index >= len(opponent_party):
                    # if it's opponent's last pokemon
                    msg += f"""{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {dead_name} fainted!
===================="""
                    query.edit_message_text(msg)
                    coinsnum = random.randint(1000,5000)
                    xpnum = 0
                    for pkmon in opponent_party:
                        xpnum += int(pkmon['xp']/1000*57)
                    for pkm in party:
                        pkm['xp'] += xpnum
                    game[uid]['pokecoins'] += coinsnum
                    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name}, you won against {trainerlist.trainers[choice]['name']}! You earned {coinsnum} pokecoins and {xpnum} XP (for each of your pokemon)!")
                    index = 0
                    for pkmo in game[uid]['party']:
                        boxindex = game[uid]['box'].index(pkmo)
                        game[uid]['box'][boxindex] = party[index]
                        if pkmo == game[uid]['bud']:
                            game[uid]['bud'] = party[index]
                        index += 1
                    for pkmon in party:
                        if pkmon['currhp'] < 1:
                            party[party.index(pkmon)] = {}
                    game[uid]['party'] = party
                    save()
                    return
                # otherwise
                msg += f"""{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {dead_name} fainted!
{trainerlist.trainers[choice]['name']} sent out {current_opponent_pk.name}!
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
Which move would you like to use?"""
                query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
            else:
                # if opponent doesn't faint
                msg += f"""{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name} used {opponent_move}!
{opponent_move} dealt {opponent_p} damage!
====================
{user.first_name}'s {party[currentpk_index]['name']}:
LEVEL: {party[currentpk_index]['lvl']}
HP: {party[currentpk_index]['currhp']}/{party[currentpk_index]['hp']}
====================
{user.first_name}'s {party[currentpk_index]['name']} used {move}!
{move} dealt {p} damage!
====================
{trainerlist.trainers[choice]['name']}'s {current_opponent_pk.name}:
LEVEL: {current_opponent_pk.lvl}
HP: {current_opponent_pk.currhp}/{current_opponent_pk.hp}
====================
Which move would you like to use?"""
                query.edit_message_text(msg,reply_markup=pokeutils.getkb(get_move_buttons(party[currentpk_index]['moves'], currentpk_index, current_opponent_pk_index, choice, current_opponent_pk)))
    game[uid]['party'] = party
    save()

def calculate_power(pk,opponent_pk,move):
    # raise
    raisers = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    raisenum = [0,0,0]
    if raisers[0] <= movelist.moves[move]['raiser'][1]:
       raisenum[0] += opponent_pk.atk*((movelist.moves[move]['raise'][1]*10)/100)
    if raisers[1] <= movelist.moves[move]['raiser'][2]:
        raisenum[1] += opponent_pk.defence*((movelist.moves[move]['raise'][2]*10)/100)
    if raisers[2] <= movelist.moves[move]['raiser'][3]:
        raisenum[2] += opponent_pk.speed*((movelist.moves[move]['raise'][3]*10)/100)
    # un-raise
    eraisers = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    eraisenum = [0,0,0]
    if eraisers[0] <= movelist.moves[move]['eraiser'][1]:
        eraisenum[0] += opponent_pk.atk*((movelist.moves[move]['eraise'][1]*10)/100)
    if eraisers[1] <= movelist.moves[move]['eraiser'][2]:
        eraisenum[1] += opponent_pk.defence*((movelist.moves[move]['eraise'][2]*10)/100)
    if eraisers[2] <= movelist.moves[move]['eraiser'][3]:
        eraisenum[2] += opponent_pk.speed*((movelist.moves[move]['eraise'][3]*10)/100)
    # damage
    damage = int(2*pk.lvl/5+2*pk.atk*movelist.moves[move]['power']/opponent_pk.defence/50)+2
    # critical hit
    c = movelist.moves[move]['crithit']
    if c == 0:
        cint = random.randint(1,24)
    else:
        cint = random.randint(1,8)
    if cint == 1:
        damage *= 1.5
    # others
    if movelist.moves[move]['pktype'] in pk.pktype:
        damage *= 1.5
    damage *= random.randint(movelist.moves[move]['timesperturn'][0],movelist.moves[move]['timesperturn'][1])
    # accuracy check
    acc = random.randint(0,100)
    if acc > movelist.moves[move]['acc']:
        damage = 0
    return [int(damage),raisenum,eraisenum]

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
    dispatcher.add_handler(CallbackQueryHandler(battle_start,pattern="^pkbattlestart:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(battle_move,pattern="^pkbattlemove:[A-Za-z0-9_]*"))