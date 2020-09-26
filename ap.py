from telegram.ext import CommandHandler, dispatcher
import random

def potions(update, context):
    potions = ["You searched the Gryffindor common room and found a COMMON potion! +3AP!\n您搜索了格兰芬多公共休息室，发现了一瓶普通药水！+3AP！", "You searched the Gryffindor common room and found two COMMON potions! +6AP!\n您搜索了格兰芬多公共休息室，发现了两瓶普通药水！+6AP！", "You searched the Gryffindor common room, and found... nothing.\n您搜索了格兰芬多公共休息室，却发现……一无所获。", "You searched the Great Hall, and found a COMMON potion! +3AP!\n您搜索了大厅，发现了一瓶普通药水！+3AP！", "You searched the Great Hall, and Errol crashed into your face! You spent the rest of the day cleaning your hair.\n您搜索了大厅，但是埃罗尔撞到了您的脸上！您在一天的剩余时间里都在清理头发。", "You searched the Potions classroom, and found a COMMON potion! +3AP!\n您搜索了魔药教室，发现了一瓶普通药水！+3AP！", "You searched the Potions classroom, and found three COMMON potions! +9AP!\n您搜索了魔药教室，发现三瓶普通药水！+9AP！", "You searched the Potions classroom, and found one RARE potion! 20AP!\n您搜索了魔药教室，发现了一瓶稀有药水！+20AP！", "You searched the Potions classroom, and found Severus Snape! You lost 20HP!\n您搜索了魔药教室，发现了西弗勒斯·斯内普！您损失了20HP"]
    result = random.choice(potions)
    update.message.reply_text("%s\nCreator/作者: Sichengthebest"%result)

def addHandler(dispatcher):
    guessHandler = CommandHandler('gainap', potions)
    dispatcher.add_handler(guessHandler)