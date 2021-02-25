import os
import logging
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
这是我的所有命令。玩得开心点！
-------------------------------------------------
/pokemon - Go catch pokemon! // 去捉宠物小精灵！
/pokebal - Check the amount of pokecoins you have. // 检查您有多少 pokecoins。
/pokeshop - Buy useful stuff for your adventure! // 为您的冒险购买有用的东西！
/box - Check the pokemon in your box! // 检查盒子里的宠物小精灵！
/view_bud - [BETA] Check on your buddy! // [测试] 检查您的好友！
/set_bud - [BETA] Get a new buddy! // [测试] 结识新好友！
/surprise - Get your daily injection of pokecoins! // 每天注射 Pokecoins！
/pokedex - [BETA] Check the pokemon you have. // [测试] 检查您有的 pokemon。
/bag - Check the items you have. // 检查您有的物件。
/evolve - [BETA] Evolve your buddy! // 升级你的伙伴！
/view_bud - Check on your buddy! // [测试] 检查您的好友！
/set_bud - Get a new buddy! // 结识新好友！
/add_party_member - Add pokemon into your party! // 将宠物小精灵加入您的团队！
/view_party - Check your party. // 检查您的团队。
/profile - View your profile. // 查看你的个人资料。
-------------------------------------------------
You can go find the new added commands at https://t.me/pokebotupdates , the official bot updates channel.
您可以在官方bot更新频道 https://t.me/pokebotupdates 上找到新添加的命令。
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
        BotCommand('start','Random command that makes the bot say "I\'m THE GOD OF BOTS..." // 使机器人说 “我是机器人的上帝” 的随机命令。'),
        BotCommand('help','Know your commands! // 了解你的命令！')]

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
    print(f"Starting... ID: {me.id} , Username: {me.username}")

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