import pytz
from icalevents.icalevents import events
from datetime import datetime, timedelta, date, time
from telegram.ext import JobQueue, CommandHandler, Updater
from telegram import bot

def JOB(update,context):
    chat_id = update.effective_chat.id
    context.job_queue.run_daily(get_cal,time(12,0,0,0,pytz.timezone('US/Eastern')),context=chat_id)

def get_cal(context):
    t = date.today()
    tmr = t + timedelta(days=1)
    url = 'webcal://p72-caldav.icloud.com/published/2/NDE3OTkzMjk0NDE3OTkzMpSxb7ERH6yybgSlRn2nfyB4Hv7q5lfiDR7Fdx2tj3PeCWqnHVbkdy36ExtEYZ7PMeviqrlOuICN0CTECfxfDcw'
    es = events(url=url,start=tmr,end=tmr,fix_apple=True)
    msg = "Tomorrow's events:"
    if len(es) == 0:
        msg = 'You have no events tomorrow.'
    for thing in es:
        msg += f'''
----------------------------
{thing.summary}: {thing.description}
    Starts: {datetime.strftime(thing.start,"%Y/%m/%d %H:%M:%S")}
    Ends: {datetime.strftime(thing.end,"%Y/%m/%d %H:%M:%S")}'''
    job = context.job
    context.bot.send_message(job.context,msg)

if __name__ == '__main__':
    t = date.today()
    tmr = t + timedelta(days=1)
    url = 'webcal://p72-caldav.icloud.com/published/2/NDE3OTkzMjk0NDE3OTkzMpSxb7ERH6yybgSlRn2nfyB4Hv7q5lfiDR7Fdx2tj3PeCWqnHVbkdy36ExtEYZ7PMeviqrlOuICN0CTECfxfDcw'
    es = events(url=url,start=tmr,end=tmr,fix_apple=True)
    msg = "Tomorrow's events:"
    if len(es) == 0:
        msg = 'You have no events tomorrow.'
    for thing in es:
        msg += f'''
----------------------------
{thing.summary}: {thing.description}
    Starts: {datetime.strftime(thing.start,"%Y/%m/%d %H:%M:%S")}
    Ends: {datetime.strftime(thing.end,"%Y/%m/%d %H:%M:%S")}'''
    print(msg)

def add_handler(dp):
    dp.add_handler(CommandHandler('get_cal',JOB,pass_job_queue=True))