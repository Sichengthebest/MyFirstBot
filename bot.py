import os
import logging
import getopt
import sys
import mysystemd
import config
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

def start(update, context):
    msg = "I'M THE GOD OF BOTS...\n/help for commands.\nVersion: 5.14.18\n------------------------------\n我是机器人的上帝...\n/help 来看命令。\n版本：5.14.18\n------------------------------\nCreator/作者: Sichengthebest"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Here's all my commands. Have fun!
这是我的所有命令。玩得开心点！
-------------------------------------------------
Start commmand // 启动命令:
/start - Random command that makes the bot say \"I'm THE GOD OF BOTS...\" // 使机器人说 “我是机器人的上帝” 的随机命令。
-------------------------------------------------
Currency commands // 货币命令:
/hunt - Gain beastcoins by catching animals. // 以捕捉动物的方式获得兽币。
/huntbal - Check the amount of beastcoins you have. // 检查您有多少兽币。
/huntshop - Buy nice useful stuff for catching more animals! // 购买帮忙捕捉动物的东西！
/fish - Gain fishcoins by fishing. // 以钓鱼的方式获得鱼币。
/fishbal - Check the amount of fishcoins you have. // 检查您有多少鱼币。
/fishshop - Buy nice useful stuff for catching more fish! // 购买帮忙捕捉鱼的东西！
/search - Go fetch the GP falling from the sky!!! // 去获取从天上掉下来的GP吧！！！
/daily - Get daily GP! // 每日打卡！
/hourly - Get hourly GP! // 每时打卡！
/weekly - Get weekly GP! // 每星期打卡！
/yearly - Get yearly GP! // 每年打卡！
/beg - Go beg, peasant! // 去讨钱吧，穷人！
/convert - Convert one currency into another! // 将一种货币转换为另一种货币！
/bal - Check the amount of money you have. // 检查您有多少GP。
-------------------------------------------------
Inventory commands // 库存命令:
/buy - Buy nice useful stuff! // 购买有用的东西！
/sell - Sell useless stuff. // 出售无用的东西。
/inv - Check the items you have in your inventory. // 检查库存中的物品。
-------------------------------------------------
Bank commands // 银行命令:
/dep - Deposit money from your wallet to your bank! // 从钱包里存钱到银行！
/withdraw - Withdraw money from your bank to your wallet! // 从银行提款！
/banknote - Increase the amount of GP you can stuff into your bank! // 增加您可以存入银行的GP数量！
-------------------------------------------------
Fun commands // 有趣的命令:
/capitals - How good are you at capitals? // 你了解所有首都吗？
/gif - The bot will send you a funny gif. // 机器人会向您发送有趣的GIF。
/gamble - Roll your dice against the bot, if you get higher than the bot you'll win! // 与机器人投骰子，如果得到的数比机器人高，您将获胜！
/pokemon - Go catch pokemon! // 去捉宠物小精灵！
/box - [BETA] Check the pokemon in your box! // [测试] 检查盒子里的宠物小精灵！
/pokeshop - Buy useful stuff for your adventure! // 为您的冒险购买有用的东西！
/bud - [BETA] Check on your buddy! // [测试] 检查您的好友！
/pokebal - Check the amount of pokecoins you have. // 检查您有多少 pokecoins。
-------------------------------------------------
You can go find the new added commands at https://t.me/botgodupdates , the official bot updates channel.
您可以在官方bot更新频道 https://t.me/botgodupdates 上找到新添加的命令。
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
    config.config_file = f"{PATH}/my.json"
    config.load_config()
    TOKEN=config.CONFIG["token"]

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    me = updater.bot.get_me()
    print(f"Starting... ID: {me.id} , Username: {me.username}")

    import hunt
    import fish
    import search
    import capitals
    import coins
    import beg
    import gif
    import gamble
    import shop
    import pokemon
    import adventure_main
    import info
    import postmeme
    from adventure_cmds import antarctica,discord,home,mars,northpole,space

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    hunt.addHandler(dispatcher)
    fish.addHandler(dispatcher)
    search.addHandler(dispatcher)
    capitals.add_handler(dispatcher)
    coins.add_handler(dispatcher)
    beg.add_handler(dispatcher)
    gif.add_handler(dispatcher)
    gamble.add_handler(dispatcher)
    shop.add_handler(dispatcher)
    pokemon.addHandler(dispatcher)
    adventure_main.add_handler(dispatcher)
    antarctica.add_handler(dispatcher)
    info.add_handler(dispatcher)
    postmeme.add_handler(dispatcher)
    commands = coins.get_command() + capitals.get_command() + search.get_command() + fish.get_command() + hunt.get_command() + get_command() + beg.get_command() + gif.get_command() + gamble.get_command() + shop.get_command() + pokemon.getCommand()
    updater.bot.set_my_commands(commands)

    updater.start_polling()
    print('Started')
    mysystemd.ready()

    updater.idle()
    print('Stopping...')
    print('Stopped.')