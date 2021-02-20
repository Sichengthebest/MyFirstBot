from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, MessageHandler, CallbackQueryHandler, filters
from utils import util

uservote = {}

def reaction(update,context):
    message = update.channel_post
    message.edit_reply_markup(reply_markup=util.getkb([{'👍 This is what I wanted! (0)':'react:👍:0'},{'👎 What kind of trash update is this? (0)':'react:👎:0'}]))

def add_user_vote(msgid,uid,choice,buttons):
    c = {"👍":0,"👎":1}
    ctrans = {'👍':'👍 This is what I wanted! ','👎':'👎 What kind of trash update is this? '}
    count = int(buttons[c[choice]][0].callback_data.split(":")[2])
    if not msgid in uservote :
        uservote[msgid] = {}
    if not uid in uservote[msgid]:
        uservote[msgid][uid] = choice
        count += 1
        buttons[c[choice]][0].text = f"{ctrans[choice]}({count})"
        buttons[c[choice]][0].callback_data = f"react:{choice}:{count}"
    else:
        if uservote[msgid][uid] == choice:
            # if 👍 原来 👍 [0] -1
            # if 👍 原来 👎 [0] -1 [1] + 1
            count -= 1
            buttons[c[choice]][0].text = f"{ctrans[choice]}({count})"
            buttons[c[choice]][0].callback_data = f"react:{choice}:{count}"
            uservote[msgid].pop(uid)
        else:
            count += 1
            buttons[c[choice]][0].text = f"{ctrans[choice]}({count})"
            buttons[c[choice]][0].callback_data = f"react:{choice}:{count}"
            oldchoice = uservote[msgid][uid]
            oldcount = int(buttons[c[oldchoice]][0].callback_data.split(":")[2])
            oldcount -= 1
            buttons[c[oldchoice]][0].text = f"{ctrans[oldchoice]}({oldcount})"
            buttons[c[oldchoice]][0].callback_data = f"react:{oldchoice}:{oldcount}"
            uservote[msgid][uid] = choice
    return buttons

def react_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":") # ['react','👍',100]
    buttons = query.message.reply_markup.inline_keyboard
    msgid = query.message.message_id
    uid = update.effective_user.id
    kb = add_user_vote(msgid,uid,cmd[1],buttons)
    query.answer("投票成功")
    query.edit_message_reply_markup(InlineKeyboardMarkup(kb))

def add_handler(dp):
    dp.add_handler(MessageHandler(filters.Filters.chat_type.channel,callback=reaction))
    dp.add_handler(CallbackQueryHandler(react_callback,pattern="^react:[A-Za-z0-9_:]*"))