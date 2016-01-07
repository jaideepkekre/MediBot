#DATES : 4 jan 2016
#USE : Poll telegram API for incoming messages and forward them to core
# after wrapping in a nice JSON format.
#Owner : @v0dro

from telegram import Updater
from core import core
import dispatcher
import threading
import os

def message_dispatcher(bot, update):
  d = {
    'chat_id' : update.message.chat_id,
    'text' : update.message.text
  }
  creator = dispatcher.dispatcher(d)
  while not creator.is_message_ready():
    pass

  m = creator.response()
  bot.sendMessage(chat_id=m['chat_id'], text=m['text'])

def process_messages(bot, update):
  t = threading.Thread(target=message_dispatcher, args=(bot, update))
  t.daemon = True
  t.start()

updater = Updater(token=os.environ.get('TELEGRAM_API_KEY'))
message_sender = updater.dispatcher
message_sender.addTelegramMessageHandler(process_messages)
updater.start_polling()
 