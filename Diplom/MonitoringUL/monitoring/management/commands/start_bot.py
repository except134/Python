from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        updater = Updater(token='7552183318:AAE6L2Mz48Y_nKkN7VuBbcHY8ozoq0icfY4', use_context=True)
        dispatcher = updater.dispatcher

        def start(update: Update, context: CallbackContext):
            update.message.reply_text('Hello! I am your bot.')

        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        updater.start_polling()
        updater.idle()
        
