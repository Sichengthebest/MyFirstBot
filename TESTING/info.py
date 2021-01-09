from telegram.ext import Dispatcher,CommandHandler
from json import dumps


def info(update,context):
    if update.message.reply_to_message:
        if update.message.reply_to_message.animation:
            u = str(update.message.reply_to_message.animation)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is an animation.
==============================
{u}""")
        elif update.message.reply_to_message.photo:
            u = str(update.message.reply_to_message.photo[len(update.message.reply_to_message.photo)-1])
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a photo.
==============================
{u}""")
        elif update.message.reply_to_message.audio:
            u = str(update.message.reply_to_message.audio)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is an audio.
==============================
{u}""")
        elif update.message.reply_to_message.game:
            u = str(update.message.reply_to_message.game)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a game.
==============================
{u}""")
        elif update.message.reply_to_message.sticker:
            u = str(update.message.reply_to_message.sticker)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a sticker.
==============================
{u}""")
        elif update.message.reply_to_message.video:
            u = str(update.message.reply_to_message.video)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a video.
==============================
{u}""")
        elif update.message.reply_to_message.voice:
            u = str(update.message.reply_to_message.voice)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a voice message.
==============================
{u}""")
        elif update.message.reply_to_message.document:
            u = str(update.message.reply_to_message.voice)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a document.
==============================
{u}""")
        elif update.message.reply_to_message.video_note:
            u = str(update.message.reply_to_message.video_note)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""This is a video message.
==============================
{u}""")
        else:
            u = str(update.message.reply_to_message)
            u = dumps(eval(u),indent=5)
            update.message.reply_text(f"""Such a normie message...""")
    else:
        u = str(update.message)
        u = dumps(eval(u),indent=5)
        update.message.reply_text(f"""No my friend you need to reply this to something""")

def add_handler(dp):
    dp.add_handler(CommandHandler("ainfo", ainfo))
    dp.add_handler(CommandHandler("getinfo", info))