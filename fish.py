from telegram.ext import CommandHandler, dispatcher
import random

def fish(update, context):
    fishes = ["You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught a herring! +8XP!\n你钓到了一条鲱鱼！+8XP！","You caught two herrings! +15XP!\n你钓到了二条鲱鱼！+15XP！", "You caught three herrings! +25XP!\n你钓到了三条鲱鱼！+25XP！", "You caught four herrings! +32XP!\n你钓到了四条鲱鱼！+32XP！", "You caught a lake trout! +50XP!\n你钓到了一条湖鳟！+50XP！", "You caught two lake trout! Yeah! +100XP!\n你钓到了两条湖鳟！+100XP！耶～", "You forgot your fishing pole!\n你忘了钓鱼竿！", "You forgot your lure!\n你忘了诱饵！", "YOU HAVE CAUGHT A GREAT WHITE SHARK! How did you do that? +250XP!\n您钓到了一条大白鲨！你是怎么做到的？+ 250XP！", "You have caught a Great White Shark, but it pulled you into the ocean and ate you! You died.\n您捕获了一条大白鲨，但是它把您拖入海中并吞噬了您！您挂了。", "You caught a lake trout, but it was too large and the police fined you 40GP!\n您抓到一条鳟鱼，但是它太大了，警察罚款了您40GP！", "You caught nothing. Keep working on it...\n你什么都没钓到。在修炼一万年吧～"]
    result = random.choice(fishes)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)

def addHandler(dispatcher):
    fsHandler = CommandHandler('fish', fish)
    dispatcher.add_handler(fsHandler)