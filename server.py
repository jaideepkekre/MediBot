#DATES : 4 jan 2016
#USE : Poll telegram API for incoming messages and forward them to core
# after wrapping in a nice JSON format.
#Owner : @v0dro

from telegram import Updater
import dispatcher
import threading
import os

CREATOR = dispatcher.dispatcher()

def process_messages(bot, update):
  d = {
    'chat_id' : update.message.chat_id,
    'text' : update.message.text
  }

  m = CREATOR.run_dispatcher(d)

  for text in m['response_list']:
    bot.sendMessage(chat_id=m['chat_id'], text=text)

updater = Updater(token=os.environ.get('TELEGRAM_API_KEY'))
message_sender = updater.dispatcher
message_sender.addTelegramMessageHandler(process_messages)
updater.start_polling()
 