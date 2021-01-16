from telegram import InlineKeyboardButton,InlineKeyboardMarkup

def getkb(kb):
    # kb : [{'text':'callback_data',...},{},{}....]
    buttons = []
    for line in kb:
        line_buttons = []
        for button_name in line:
            button = InlineKeyboardButton(button_name,callback_data=line[button_name])
            line_buttons.append(button)
        buttons.append(line_buttons)
    return InlineKeyboardMarkup(buttons)