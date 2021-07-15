import pokeconfig
import pokeutils
import pokemons
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

game = pokeconfig.CONFIG["pk"]

def save():
    pokeconfig.CONFIG["pk"] = game
    pokeconfig.save_config()

def add_party(update,context):
    user = update.effective_user
    uid = str(user.id)
    pokemons.check_time(uid)
    pagenow = 1
    size = 5
    kblist = get_party_members(uid,pagenow)
    splitmsgs,numcount = get_party_text(user)
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
            buttons.append({f"{game[uid]['box'][index]['name']}, XP: {game[uid]['box'][index]['xp']}":f"pkpartyadd:{index}"})
        kb = pokeutils.getkb(buttons)
        update.message.reply_text(f'Which {pk} are you choosing?',reply_markup=kb)
    else:
        if pagenow * size > numcount:
            kb = pokeutils.getkb(kblist)
            update.message.reply_text(splitmsgs[0],reply_markup=kb)
        else:
            kblist.append({'➡️':f'pkpartypages:next:{pagenow+1}:{user.id}'})
            kb = pokeutils.getkb(kblist)
            update.message.reply_text(splitmsgs[0],reply_markup=kb)


def partyPagesCallback(update,context):
    user = update.effective_user
    query = update.callback_query
    _,direction,pagenow,curruid = query.data.split(':')
    if str(user.id) != curruid:
        query.answer("Yo dude this is someone else's party setting stop clicking these buttons!",show_alert=True)
        return
    size = 5
    splitmsgs,numcount = get_party_text(user)
    kblist = get_party_members(str(user.id),int(pagenow))
    if direction == 'next':
        if (int(pagenow)) * size >= numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow-1)])
            else:
                kblist.append({'⬅️':f'pkpartypages:prev:{int(pagenow)-1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kblist.append({'➡️':f'pkpartypages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kblist.append({'⬅️':f'pkpartypages:prev:{int(pagenow)-1}:{user.id}'})
                kblist.append({'➡️':f'pkpartypages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
    else:
        if (int(pagenow)) * size > numcount:
            if int(pagenow) * size <= 0:
                query.edit_message_text(splitmsgs[int(pagenow)-1])
            else:
                kblist.append({'⬅️':f'pkpartypages:prev:{int(pagenow)-1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
        else:
            if (int(pagenow)-1) * size <= 0:
                kblist.append({'➡️':f'pkpartypages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)
            else:
                kblist.append({'⬅️':f'pkpartypages:prev:{int(pagenow)-1}:{user.id}'})
                kblist.append({'➡️':f'pkpartypages:next:{int(pagenow)+1}:{user.id}'})
                kb = pokeutils.getkb(kblist)
                query.edit_message_text(splitmsgs[int(pagenow)-1],reply_markup=kb)

def partyAddCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,index = query.data.split(':')
    if game[uid]['box'][int(index)]['moves'] == []:
        query.answer('This pokemon has no moves!', show_alert=True)
        return
    if game[uid]['box'][int(index)]['currhp'] < 1:
        query.answer('This pokemon has no HP!', show_alert=True)
        return
    kb = pokeutils.getkb([{'1':f'pkpartyposition:{index}:1','2':f'pkpartyposition:{index}:2','3':f'pkpartyposition:{index}:3','4':f'pkpartyposition:{index}:4','5':f'pkpartyposition:{index}:5','6':f'pkpartyposition:{index}:6'}])
    query.edit_message_text(f"{game[uid]['box'][int(index)]['name']}? OK! In which position in your party would you like to put him/her?",reply_markup=kb)

def partyPositionCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    query = update.callback_query
    _,index,positionbig = query.data.split(':')
    position = int(positionbig)-1
    if game[uid]['box'][int(index)] in game[uid]['party']:
        index2 = game[uid]['party'].index(game[uid]['box'][int(index)])
        game[uid]['party'][index2] = {}
    game[uid]['party'][position] = game[uid]['box'][int(index)]
    kb = pokeutils.getkb([{'Add another pokemon?':'pkpartyrestart:'}])
    query.edit_message_text(f"Success! {game[uid]['box'][int(index)]['name']} has been added at position {positionbig} in your party.",reply_markup=kb)
    save()

def partyRestartCallback(update,context):
    user = update.effective_user
    uid = str(user.id)
    pokemons.check_time(uid)
    query = update.callback_query
    pagenow = 1
    size = 5
    kblist = get_party_members(uid,pagenow)
    splitmsgs,numcount = get_party_text(user)
    if pagenow * size > numcount:
        kb = pokeutils.getkb(kblist)
        query.edit_message_text(splitmsgs[0],reply_markup=kb)
    else:
        kblist.append({'➡️':f'pkpartypages:next:{pagenow+1}:{user.id}'})
        kb = pokeutils.getkb(kblist)
        query.edit_message_text(splitmsgs[0],reply_markup=kb)

def show_party(update,context):
    user = update.effective_user
    uid = str(user.id)
    msg = ''
    count = 0
    if not 'party' in game[uid]:
        game[uid]['party'] = [{},{},{},{},{},{}]
    if game[uid]['party'] == [{},{},{},{},{},{}]:
        msg = 'Your party is empty. Use /add_party_member to start adding pokemon to your party!'
    else:
        for pkdict in game[uid]['party']:
            count += 1
            if pkdict == {}:
                msg += f"{count}. Empty\n~~~~~~~~~~~~~~~~~~~~\n"
            else:
                la = ''
                for move in pkdict['moves']:
                    la += f'\n{move}'
                msg += f"{count}. {pkdict['name']}\nLevel: {pkdict['lvl']}      💖 HP: {pkdict['currhp']}/{pkdict['hp']}\nMoves: {la}\n~~~~~~~~~~~~~~~~~~~~~\n"
    update.message.reply_text(msg)

def get_party_text(user):
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
            splitmsgs.append(f'{user.first_name}, which pokemon would you like to have in your party? Page {int(msgcount/5)+1}\n~~~~~~~~~~~~~~~~~~~~')
        splitmsgs[int(msgcount/5)] += f'\n{msgs}'
    return splitmsgs,numcount

def get_party_members(uid,pagenow):
    kblist = []
    kbstart = (pagenow-1)*5
    kbend = kbstart + 5
    for index in range(kbstart,kbend):
        if index > len(game[uid]['box'])-1:
            return kblist
        kblist.append({f"{game[uid]['box'][index]['name']}, XP: {game[uid]['box'][index]['xp']}":f"pkpartyadd:{index}"})
    return kblist

def addHandler(dispatcher):
    dispatcher.add_handler(CommandHandler('add_party_member',add_party))
    dispatcher.add_handler(CommandHandler('view_party',show_party))
    dispatcher.add_handler(CallbackQueryHandler(partyPagesCallback,pattern="^pkpartypages:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(partyAddCallback,pattern="^pkpartyadd:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(partyPositionCallback,pattern="^pkpartyposition:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CallbackQueryHandler(partyRestartCallback,pattern="^pkpartyrestart:[A-Za-z0-9_]*"))