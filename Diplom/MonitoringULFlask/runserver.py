"""
This script runs the MonitoringULFlask application using a development server.
"""

from os import environ
from MonitoringULFlask import app
from MonitoringULFlask.tgbot import *
from threading import Thread, Lock

def start_tg_bot():
    bot.polling(none_stop=True)

def start_web_app(host: str | None = None, port: int | None = None):
    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

#    th1 = Thread(target=start_tg_bot)
    th2 = Thread(target=start_web_app, args=(HOST, PORT))

#    th1.start()
    th2.start()

#    th1.join()
#    th2.join()

    bot.polling(none_stop=True, interval=0)
