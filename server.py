#DATES : 4 jan 2016
#USE : Poll telegram API for incoming messages and forward them to core
# after wrapping in a nice JSON format.
#Owner : @v0dro

from telegram import Updater
import dispatcher
from multiprocessing import Process, Queue
import os

CREATOR = dispatcher.dispatcher()
MESSAGE_QUEUE = Queue()

def dispatch_messages(queue_local):
  while True:
    if not queue_local.empty():
      user_info = queue_local.get()
      m = CREATOR.run_dispatcher(user_info)

      for text in m['response_list']:
        user_info['bot'].sendMessage(chat_id=m['chat_id'], text=text)

def accept_message(bot, update):
  d = {
    'chat_id' : update.message.chat_id,
    'text'    : update.message.text,
    'bot'     : bot
  }

  MESSAGE_QUEUE.put(d)

telegram_poller = Updater(token=os.environ.get('TELEGRAM_API_KEY'))
message_sender  = telegram_poller.dispatcher
message_sender.addTelegramMessageHandler(accept_message)
message_processor = Process(target=dispatch_messages, args=(MESSAGE_QUEUE,))
message_processor.start()
telegram_poller.start_polling()
