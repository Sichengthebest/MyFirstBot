from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import random

countries = {
    'easy':{
        "🇫🇷 France // 法国 🇫🇷" : {
            "yes":"Paris // 巴黎",
            "no":["Calais // 加来","Marseilles // 马赛","Versailles // 凡尔赛","Québec // 魁北克"],
            "haha":["thE eIFFel ToWEr obVioUSlY // 当然是诶福尔铁塔啦～","Macron City // 马克龙城","Beaconsfield // 比肯斯菲尔德"]
        },
        "🇨🇦 Canada // 加拿大 🇨🇦" : {
            "yes":"Ottawa // 渥太华",
            "no":["Toronto // 多伦多","Kingston // 金斯敦","Vancouver // 温歌华"],
            "haha":["The North Pole HOHOHO","Beaconsfield // 比肯斯菲尔德"]
        },
        "🇨🇳 China // 中国 🇨🇳" : {
            "yes": "Beijing // 北京",
            "no":["Shanghai // 上海","Beijiing // 北进","Guangzhou // 广州"],
            "haha" : ["Centre City // 中城","Beaconsfield // 比肯斯菲尔德","Xi Jingping City"]
        },
        "🇬🇧 UK // 英国 🇬🇧" : {
            "yes": "Beaconsfield // 比肯斯菲尔德",
            "no":["Beaconsfield // 比肯斯菲尔德","Beaconsfield // 比肯斯菲尔德"],
            "haha":["Beaconsfield // 比肯斯菲尔德","Beaconsfield // 比肯斯菲尔德","Beaconsfield // 比肯斯菲尔德"]
        }
    },
    'normal':{
        "🇸🇪 Sweden // 瑞典 🇸🇪" : {
            "yes": "dfsdfsdf",
            "no":["Beaconsfield // 比肯斯菲尔德","Beaconsfield // 比肯斯菲尔"],
            "haha":["Beaconsfild // 比肯斯菲尔德","Beaconsfield // 比肯斯尔德"]
        }
    },
    'hard':{
        "🇻🇪 Venezuela // 委内瑞拉 🇻🇪" : {
            "yes": "sdfsdf",
            "no":["Beacosfield // 比肯斯菲尔德","Eaconsfield // 比肯斯菲尔德"],
            "haha":["Baconsfield // 比肯斯菲尔德","Beaconsfield // 比肯斯菲德"]
        }
    
    },
    'extreme':{
        "🇵🇬 Papua New Guinea // 巴布亚新几内亚 🇵🇬" : {
            "yes": "sadasada",
            "no":["Beaconsfiel // 比肯斯菲尔德","Beaconsfield // 肯斯菲尔德"],
            "haha":["Beacnsfield // 比肯斯菲尔德","Beaconsfied // 比肯斯菲尔德"]
        }
    }
}

def init_markup(choice):
    mk = []
    yesIndex = random.randint(0,2)
    no1 = random.choice(choice['no'])
    no2 = random.choice(choice['no'])
    while no1 == no2 :
        no2 = random.choice(choice['no'])
    no = [no1,no2]
    haha = random.choice(choice['haha'])
    yes = choice['yes']
    for i in range(3):
        if i == yesIndex:
            mk.append({yes:"cap:yes"})
        else:
            mk.append({no[0]:"cap:no"})
            no.remove(no[0])
    mk.append({haha:"cap:no"})
    buttons = []
    for line in mk:
        button = []
        for key in line.keys():
            button.append(InlineKeyboardButton(key, callback_data=line[key]))
        buttons.append(button)
    return InlineKeyboardMarkup(buttons)


def capitals(update,context):
    country = {}
    command = update.effective_message.text
    if command == "/capitals_easy":
        country = countries['easy']
    elif command == "/capitals_normal":
        country = countries['normal']
    elif command == "/capitals_hard":
        country = countries['hard']
    elif command == "/capitals_extreme":
        country = countries['extreme']
    elif command == "/capitals_random":
        rkey = random.choice([*countries.keys()])
        country = countries[rkey]
    c = random.choice([*country.keys()])
    update.effective_message.reply_text("What is the capital of %s?"%c,reply_markup=init_markup(country[c]))
    

def capitals_old(update,context):
    update.message.reply_text("""A general knowledge game! The bot will randomly generate a country and a number of answer choices, depending on your chosen difficulty level. The choices are as shown:
-------------------------------------------------------------------------
- /capitals_easy : You are supposed to be cultivated enough to know these countries's capitals.
4 answer choices, with one aberrant choice.
Rewards: 10GP per correct answer, lose 50GP per wrong answer.
-------------------------------------------------------------------------
- /capitals_normal : Quite easy questions for those who have at least observed correctly a map.
4 answer choices
Rewards: 25GP per correct answer, lose 20GP per wrong answer.
-------------------------------------------------------------------------
- /capitals_hard : Quite hard countries, but most of which you have heard of, but probably not the capitals...
5 answer choices
Rewards: 50GP per correct answer, lose 10GP per wrong answer.
-------------------------------------------------------------------------
- /capitals_extreme : Countries you have never heard of! Big cash to win, though!
6 answer choices
Rewards: 125GP per correct answer, lose 5GP per wrong answer.
-------------------------------------------------------------------------""")

def capitalsCallback(update,context):
    query = update.callback_query
    if query.data == 'cap:yes':
        query.edit_message_text("yes")
    else:
        query.edit_message_text("no")

def add_handler(dispatcher):
    dispatcher.add_handler(CallbackQueryHandler(capitalsCallback,pattern="^cap:[A-Za-z0-9_]*"))
    dispatcher.add_handler(CommandHandler('capitals_easy', capitals))
    dispatcher.add_handler(CommandHandler('capitals_normal', capitals))
    dispatcher.add_handler(CommandHandler('capitals_hard', capitals))
    dispatcher.add_handler(CommandHandler('capitals_extreme', capitals))
    dispatcher.add_handler(CommandHandler('capitals_random', capitals))
    dispatcher.add_handler(CommandHandler('capitals', capitals_old))