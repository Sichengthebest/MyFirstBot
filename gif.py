from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton
import random

# msgid: {uid:👍,uid:👍,uid:👍}
uservote = {}

def vote(update,context):
    gifs = [
        'https://cdn.lowgif.com/full/f276bc439595465c-motorcycle-fails-gif-by-world-s-funniest-find-share-on.gif',
        'https://media.tenor.com/images/1b3aa48cfa63240adfef3a61a179bec0/tenor.gif',
        'https://i.pinimg.com/originals/30/7e/44/307e44c8022a1cc37d7d1ddb102770f0.gif',
        'https://media2.giphy.com/media/l41m5h1yLXqAi5Uf6/giphy.gif',
        'https://vl-media.fr/wp-content/uploads/2018/03/fail-gif-shopping-cart.gif',
        'https://thumbs.gfycat.com/SelfreliantGoodDinosaur-max-1mb.gif',
        'https://i.pinimg.com/originals/9e/db/3f/9edb3f6a282f13de6579fc4df77172ae.gif',
        'https://media1.giphy.com/media/WjldrOwZZ3EpW/giphy.gif',
        'https://i.pinimg.com/originals/e0/55/85/e05585b6800b93f1991219a100a28cee.gif',
        'https://media4.giphy.com/media/DbbHysLg3LCF2/giphy.gif',
        'https://media3.giphy.com/media/eerGTVL76LuS1Nkzuv/giphy.gif',
        'https://media1.giphy.com/media/l0O9zrbtv8ALhvqi4/giphy.gif',
        'https://media1.giphy.com/media/3xz2BL0e68kldZ45LW/giphy.gif',
        'https://media4.giphy.com/media/QssykBpF9GVmtgadgW/giphy.gif',
        'https://thumbpress.com/wp-content/uploads/2013/05/Funniest-Fail-GIFs-7.gif',
        'https://i.pinimg.com/originals/39/ba/3b/39ba3b40ca7fd947a1b63924bcb1202d.gif',
        'https://media1.tenor.com/images/1d72c5b67e5eca205bde53ad223e26b4/tenor.gif?itemid=4128851',
        'https://i.chzbgr.com/full/5560084736/hEF066B39/double-skate-fail',
        'https://i.chzbgr.com/full/4102161664/hBC1CB70A/soccer-fail',
        'https://media4.giphy.com/media/9c4ls9LuNjkbe/giphy.gif',
        'https://media.tenor.com/images/d33af9e2bced4bc1ad116a9c3a22d0c7/tenor.gif',
        'https://www.pbh2.com/wordpress/wp-content/uploads/2013/02/sports-fails-gifs-basketball-trick.gif',
        'https://media4.giphy.com/media/WbhKnXKLZAkVi/source.gif',
        'https://i.pinimg.com/originals/2f/be/a3/2fbea3d75a9a437e6541beb32d34684c.gif',
        'https://thumbs.gfycat.com/AbleIlliterateKitten-max-1mb.gif',
        'https://media2.giphy.com/media/l41lFYeLmNE4DZP6U/source.gif',
        'https://i.pinimg.com/originals/ef/c6/0b/efc60b0c103c21f746fd0f105ec68dad.gif',
        'https://www.humoar.com/wp-content/uploads/gallery/gymfails/01.gif',
        'https://www.15heures.com/wp-content/uploads/2014/08/1409063446-ada59e1f14f09f2805016b3b6c230e58.gif'
    ]
    #  [[👍,👎,😍]]
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("👍(0)",callback_data="vote:👍:0"),
        InlineKeyboardButton("👎(0)",callback_data="vote:👎:0")
        ]])
    jif = random.choice(gifs)
    update.message.reply_animation(jif,reply_markup=kb)

def add_user_vote(msgid,uid,choice,buttons):
    c = {"👍":0,"👎":1}
    count = int(buttons[0][c[choice]].callback_data.split(":")[2])
    if not msgid in uservote :
        uservote[msgid] = {}
    if not uid in uservote[msgid]:
        uservote[msgid][uid] = choice
        count += 1
        buttons[0][c[choice]].text = f"{choice}({count})"
        buttons[0][c[choice]].callback_data = f"vote:{choice}:{count}"
    else:
        if uservote[msgid][uid] == choice:
            # if 👍 原来 👍 [0] -1
            # if 👍 原来 👎 [0] -1 [1] + 1
            count -= 1
            buttons[0][c[choice]].text = f"{choice}({count})"
            buttons[0][c[choice]].callback_data = f"vote:{choice}:{count}"
            print(uid)
            uservote[msgid].pop(uid)
        else:
            count += 1
            buttons[0][c[choice]].text = f"{choice}({count})"
            buttons[0][c[choice]].callback_data = f"vote:{choice}:{count}"
            oldchoice = uservote[msgid][uid]
            oldcount = int(buttons[0][c[oldchoice]].callback_data.split(":")[2])
            oldcount -= 1
            buttons[0][c[oldchoice]].text = f"{oldchoice}({oldcount})"
            buttons[0][c[oldchoice]].callback_data = f"vote:{oldchoice}:{oldcount}"
            uservote[msgid][uid] = choice
    return buttons

def vote_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":") # ['vote','👍',100]
    buttons = query.message.reply_markup.inline_keyboard
    msgid = query.message.message_id
    uid = update.effective_user.id

    kb = add_user_vote(msgid,uid,cmd[1],buttons)
    query.answer("投票成功")
    query.edit_message_reply_markup(InlineKeyboardMarkup(kb))
    # count = int(cmd[2])
    # query.answer("投票成功")
    # if cmd[1] == '👍':
    #     buttons[0][0] = InlineKeyboardButton(f"👍({count})",callback_data=f"vote:👍:{count}")
    #     query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    # elif cmd[1] == "👎":
    #     buttons[0][1] = InlineKeyboardButton(f"👎({count})",callback_data=f"vote:👎:{count}")
    #     query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    # elif cmd[1] == "😍":
    #     buttons[0][2] = InlineKeyboardButton(f"😍({count})",callback_data=f"vote:😍:{count}")
    #     query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    # query.answer("大傻子你已经投了，表再投了，烦不烦",show_alert=True)


def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('gif', vote))
    dp.add_handler(CallbackQueryHandler(vote_callback,pattern="^vote:[A-Za-z0-9_:]*"))

def get_command():
    return [BotCommand('gif','投票哪个是你最喜欢的')]