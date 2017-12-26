from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import re
import os

TOKEN = "502882933:AAGtNf5KxO1QKFc7AE2UDLEUSmip5NNDAik"
PORT = int(os.environ.get('PORT', '5000'))

stringHowItWorks = '''
This is a news bot:
Receive instant updates from news sites.
'''

def start(bot, update):
	update.message.reply_text("Hi!")
	update.message.reply_text(stringHowItWorks)

def help(bot, update):
	update.message.reply_text(stringHowItWorks)




def main():
	updater = Updater(TOKEN)
	
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	updater.start_polling()

	updater.idle()






if __name__ == '__main__':
	main()