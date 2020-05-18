import os
import ptbot
from pytimeparse import parse

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def reply(text):
  time = parse(text)
  message_id = bot.send_message(CHAT_ID, 'Стартую...')
  bot.create_countdown(time, notify_progress, id=message_id, time=time)

def notify_progress(secs_left, id, time):
  message = 'Осталось {} секунд'.format(secs_left) + '\n' + render_progressbar(time, secs_left)
  if secs_left != 0:
    bot.update_message(CHAT_ID, id, message)
  else:
    bot.update_message(CHAT_ID, id, message)
    bot.send_message(CHAT_ID, 'Время вышло')
    bot.send_message(CHAT_ID, 'А теперь на сколько запустим таймер?')

bot = ptbot.Bot(TOKEN)

bot.send_message(CHAT_ID, 'Привет! На сколько запустить таймер?')
bot.reply_on_message(reply)

bot.run_bot()