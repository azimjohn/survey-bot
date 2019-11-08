import time

from django.core.management import BaseCommand

from bot.bot import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Started Development Bot Client")
        try:
            bot.polling()
        except Exception as e:
            print(e)
            time.sleep(5)
            self.handle(*args, **options)
