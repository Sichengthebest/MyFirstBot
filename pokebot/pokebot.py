import os
import getopt
import sys
import mysystemd
import pokeconfig
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def start(update, context):
    msg = "Do you have a buddy? Use the /set_bud command to get started!\nCreator: Sichengthebest"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Here's all my commands. Have fun!
-------------------------------------------------
/pokemon - Go catch pokemon!
/pokebal - Check the amount of pokecoins you have.
/pokeshop - Buy useful stuff for your adventure!
/box - Check the pokemon in your box!
/view_bud - [BETA] Check on your buddy!
/set_bud - [BETA] Get a new buddy!
/surprise - Get your daily injection of pokecoins!
/pokedex - [BETA] Check the pokemon you have.
/bag - Check the items you have.
/evolve - [BETA] Evolve your buddy!
/view_bud - Check on your buddy!
/set_bud - Get a new buddy!
/add_party_member - Add pokemon into your party!
/view_party - Check your party.
/profile - View your profile.
/add_moves - Add moves to your pokemon!
/view_moves - Check your buddy\'s moves!
/battle - [BETA] Start battling other trainers\'s pokemon!
-------------------------------------------------
You can go find the new added commands at https://t.me/pokebotupdates , the official bot updates channel.
Creator/作者: Sichengthebest""")

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

def get_command():
    return [
        BotCommand('help','Know your commands!')]

def cmd_help():
    return "这是所有参数的说明"

if __name__ == '__main__':
    PATH = "/Users/sichengthebest/Work/MyFirstBot"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hc:",["config="])
    except getopt.GetoptError:
        print(cmd_help())
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(cmd_help())
            sys.exit()
        elif opt in ("-c","--config"):
            PATH = arg
    
    # TOKEN=read_file_as_str(f"{PATH}/TOKEN")
    pokeconfig.config_file = f"{PATH}/pokebot/poke.json"
    pokeconfig.load_config()
    TOKEN=pokeconfig.CONFIG["token2"]

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    me = updater.bot.get_me()
    print(f"Starting... ID: {me.id}, Username: {me.username}")

    import pokemons
    import pokemon_new
    import bud
    import party
    import battle

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    pokemons.addHandler(dispatcher)
    pokemon_new.add_handler(dispatcher)
    bud.addHandler(dispatcher)
    party.addHandler(dispatcher)
    battle.addHandler(dispatcher)
    commands = get_command() + pokemons.getCommand() 
    updater.bot.set_my_commands(commands)
    updater.start_polling()
    print('Started')
    mysystemd.ready()

    updater.idle()
    print('Stopping...')
    print('Stopped.')