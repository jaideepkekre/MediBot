from telegram import Updater
import os

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

updater = Updater(token=os.environ.get('TELEGRAM_API_KEY'))
dispatcher = updater.dispatcher
dispatcher.addTelegramCommandHandler('start', start)
updater.start_polling()
