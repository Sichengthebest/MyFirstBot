from telegram.ext import CommandHandler, dispatcher
from datetime import datetime,timedelta
import random

gametime = datetime.now()
gametime2 = datetime.now()

def fish(update, context):
    global gametime,gametime2
    gametime = datetime.now() + timedelta(seconds=30)
    fishes = ["You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught two herrings! +16XP!\n你钓到了二条鲱鱼！+16XP！", "You caught three herrings! +24XP!\n你钓到了三条鲱鱼！+24XP！", "You caught four herrings! +32XP!\n你钓到了四条鲱鱼！+32XP！", "You caught a lake trout! +50XP!\n你钓到了一条湖鳟！+50XP！", "You caught two lake trouts! Yeah! +100XP!\n你钓到了两条湖鳟！+100XP！耶～", "You forgot your fishing pole!\n你忘了钓鱼竿！", "You forgot your lure!\n你忘了诱饵！", "YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250XP!\n您钓到了一条大白鲨！你是怎么做到的？+ 250XP！", "You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。", "You caught a lake trout, but it was too large and the police fined you 40GP!\n您抓到一条鳟鱼，但是它太大了，警察罚款了您40GP！", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "LMAO you caught nothing. Keep working on it...\n嘻嘻嘻 你什么都没钓到。在修炼一万年吧～", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～", "LMFAO you caught nothing. Keep working on it...\n哈哈哈哈哈哈哈哈哈哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～", "LMAO you caught nothing. Keep working on it...\n哈哈哈哈哈 你什么都没钓到。在修炼一万年吧～"]
    result = random.choice(fishes)
    t = datetime.now() 
    if t >= gametime2:
        update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)
        gametime2 = datetime.now() + timedelta(seconds=30)
    else:
        update.message.reply_text("Slow it down, cmon!!! The fish seem weary of fishermen right now, wait a few more seconds!\nCreator/作者: Sichengthebest")

def addHandler(dispatcher):
    fsHandler = CommandHandler('fish', fish)
    dispatcher.add_handler(fsHandler)