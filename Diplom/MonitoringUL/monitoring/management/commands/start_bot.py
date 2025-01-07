from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater
from django.conf import settings

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        updater = Updater(token=settings.TG_KEY, use_context=True)
        dispatcher = updater.dispatcher

        def start(update: Update, context: CallbackContext):
            update.message.reply_text('Hello! I am your bot.')

        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        updater.start_polling()
        updater.idle()
        
