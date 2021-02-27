from telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters
from telegram import BotCommand,Update
from random import sample
import re

games = {}

def set_games_cards(chatid,cards):
    games[chatid] = {'answers':[],'users':{}}
    games[chatid]['cards'] = cards

def add_player(user,chatid):
    uid = user.id
    if not chatid in games:
        games[chatid] = {'answers':[],'users':{}}
    if not uid in games[chatid]['users']:
        games[chatid]['users'][uid] = {'correct':0,'incorrect':0,'fname':user.first_name}

def add_answer(chatid,answer):
    if not chatid in games:
        games[chatid] = {'answers':[],'users':{}}
    if not 'answers' in games[chatid]:
        games[chatid]['answers'] = []
    games[chatid]['answers'].append(answer)

def remove_games_cards(chatid):
    games[chatid] = {}

def start(update,context):
    chatid = update.effective_chat.id
    cards = [1,2,3,4,5,6,7,8,9,10]
    putcards = sample(cards,4)
    update.message.reply_text(f'{putcards[0]},{putcards[1]},{putcards[2]},{putcards[3]}')
    set_games_cards(chatid,putcards)

def rules(update,context):
    update.message.reply_text('''Welcome to 24! Your goal is to figure out how to make 24 with these numbers ( /q@sicheng24bot ).
Remember, you can only use the basic operations. They are to be typed like this: +, -, *, /. Parentheses are allowed.
Good Luck! Or is it luck?''')

def question(update,context):
    chatid = update.effective_chat.id
    msg = ""
    lead = ""
    if not chatid in games:
        update.effective_message.reply_text("There is no game currently. Use /start24@sicheng24bot to start a game.")
        return
    if games[chatid]['users'] == {}:
        update.effective_message.reply_text(f"Current cards: {games[chatid]['cards']}. There are no answers currently.")
        return
    for uid in games[chatid]['users']:
        print(games[chatid]['users'])
        print(games[chatid]['answers'])
        if games[chatid]['answers'] == []:
            msg = "There are currently no right answers."
        else:
            for answer in games[chatid]['answers']:
                msg += f"✔︎ : {answer}\n"
        lead += f"✨ {games[chatid]['users'][uid]['fname']}: ✅ {games[chatid]['users'][uid]['correct']} times correct ❌ {games[chatid]['users'][uid]['incorrect']} times incorrect\n"
    update.effective_message.reply_text(f"""Current cards: {games[chatid]['cards']}
--------------------
Current (right) answers
{msg}
--------------------
Leaderboard:
{lead}
""")

def end(update,context):
    chatid = update.effective_chat.id
    remove_games_cards(chatid)
    update.message.reply_text('The game is now ended. Use /start24@sicheng24bot to start a new game.')

def answer(update,context):
    chatid = update.effective_chat.id
    user = update.effective_user
    uid = user.id
    add_player(user,chatid)
    if not chatid in games:
        update.message.reply_text('There is no game currently. Use /start24@sicheng24bot to start a game.')
        return
    if not 'cards' in games[chatid]:
        update.message.reply_text('There is no game currently. Use /start24@sicheng24bot to start a game.')
        return
    cards = games[chatid]['cards']
    lala = True
    msg = update.message.text.replace(".","").replace(" ","")
    if msg[0].isdigit() or msg[0]== "(":
        for thing in msg:
            if thing != '*' and thing != '+' and thing != '-' and thing != '/' and thing != '(' and thing != ')':
                if not thing.isnumeric():
                    lala = False
        if lala == False:
            games[chatid]['users'][uid]['incorrect'] += 1
            update.message.reply_text(f"You must use the basic operations (+,-,*,/) and numbers from the list I gave you! (/q@sicheng24bot) For more information, please check the rules of the game here: /rules@sicheng24bot\n {update.effective_user.first_name}, you now have {games[chatid]['users'][uid]['correct']} correct answers and {games[chatid]['users'][uid]['incorrect']} incorrect answers.")
            return
        numbers = list(dict.fromkeys(re.findall(r'\d+', msg)))
        for number in numbers:
            if not int(number) in cards:
                lala = False
        if lala == False:
            games[chatid]['users'][uid]['incorrect'] += 1
            update.message.reply_text(f"You must use the numbers from the list I gave you! (/q@sicheng24bot) For more information, please check the rules of the game here: /rules@sicheng24bot\n{update.effective_user.first_name}, you now have {games[chatid]['users'][uid]['correct']} correct answers and {games[chatid]['users'][uid]['incorrect']} incorrect answers.")
            return
        if len(numbers) != 4:
            games[chatid]['users'][uid]['incorrect'] += 1
            update.message.reply_text(f"You must use the numbers from the list I gave you, and only once! (/q@sicheng24bot) For more information, please check the rules of the game here: /rules@sicheng24bot\n{update.effective_user.first_name}, you now have {games[chatid]['users'][uid]['correct']} correct answers and {games[chatid]['users'][uid]['incorrect']} incorrect answers.")
            return
        if eval(msg) == 24:
            
            if msg in games[chatid]['answers']:
                update.message.reply_text('Someone already said that answer!')
                return
            games[chatid]['users'][uid]['correct'] += 1
            update.message.reply_text(f"🎉 You did it! {update.effective_user.first_name}, you now have {games[chatid]['users'][uid]['correct']} correct answers and {games[chatid]['users'][uid]['incorrect']} incorrect answers.")
            add_answer(chatid,msg)
        else:
            games[chatid]['users'][uid]['incorrect'] += 1
            update.message.reply_text(f"🤦🐛 You are a big bug! {update.effective_user.first_name}, you now have {games[chatid]['users'][uid]['correct']} correct answers and {games[chatid]['users'][uid]['incorrect']} incorrect answers.")

def get_command():
    return [
        BotCommand('start24','开始一个24点游戏'),
        BotCommand('q','查询当前进行中的24点游戏'),
        BotCommand('end24','结束当前进行的游戏'),
        BotCommand('rules','规矩~')
    ]

def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('start24', start))
    dp.add_handler(CommandHandler('q', question))
    dp.add_handler(CommandHandler('end24', end))
    dp.add_handler(CommandHandler('rules', rules))
    dp.add_handler(MessageHandler(Filters.chat_type.supergroup & Filters.text , answer))