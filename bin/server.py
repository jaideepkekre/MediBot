#DATES : 4 jan 2016
#USE : Poll telegram API for incoming messages and forward them to core
# after wrapping in a nice JSON format.
#Owner : @v0dro

from telegram import Updater
from telegram_interface import create_keyboard
import dispatcher
from multiprocessing import Process, Queue
import os
from time import sleep
import threading

CREATOR                = dispatcher.dispatcher()
MESSAGE_QUEUE          = Queue()
FINISHED_MESSAGE_QUEUE = Queue()

def return_messages(return_queue):
  def actually_return_messages(resp):
    m   = resp[0]
    bot = resp[1]

    for text in m['response_list']:
      bot.sendMessage(
        chat_id=m['chat_id'], text=text, reply_markup=m['keyboard'])    

  user_thread_dict = {}
  while True:
    if not return_queue.empty():
      response = return_queue.get()
      chat_id = response[0]['chat_id']

      if user_thread_dict.has_key(chat_id):
        user_thread_dict[chat_id].join()
        user_thread_dict.pop(chat_id)

      user_thread_dict[chat_id] = threading.Thread(target=actually_return_messages, args=(response,))
      user_thread_dict[chat_id].start()


def dispatch_messages(queue_local):
  while True:
    sleep(0.1)
    if not queue_local.empty():
      user_info = queue_local.get()
      m = CREATOR.run_dispatcher(user_info)

      FINISHED_MESSAGE_QUEUE.put((m, user_info['bot']))

def accept_message(bot, update):
  d = {
    'chat_id' : update.message.chat_id,
    'text'    : update.message.text,
    'bot'     : bot
  }

  MESSAGE_QUEUE.put(d)
TOKEN    = os.environ.get('TELEGRAM_API_KEY')

updater = Updater(token=TOKEN)
message_sender  = updater.dispatcher
message_sender.addTelegramMessageHandler(accept_message)

message_processor = Process(target=dispatch_messages, args=(MESSAGE_QUEUE,))
message_returner  = Process(target=return_messages, args=(FINISHED_MESSAGE_QUEUE,))

message_processor.start()
message_returner .start()
updater.start_polling(poll_interval=0.1)
updater.idle()