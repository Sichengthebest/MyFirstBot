import os
import logging
import getopt
import sys
import mysystemd
import config
from telegram.ext import CommandHandler, Updater
from telegram import BotCommand

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
    TOKEN=config.CONFIG["token3"]

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    me = updater.bot.get_me()
    print(f"Starting... ID: {me.id} , Username: {me.username}")

    import story

    commands = story.get_command()
    story.add_handler(dispatcher)
    updater.bot.set_my_commands(commands)

    updater.start_polling()
    updater.idle()