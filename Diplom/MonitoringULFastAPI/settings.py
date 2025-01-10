import os

WEB_SECRET_KEY = '8cf59782-dafd-428d-ba8f-19a04f1899f5'
TG_KEY = '7552183318:AAE6L2Mz48Y_nKkN7VuBbcHY8ozoq0icfY4'
PRINT_DEBUG = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'PS_INFO')

if PRINT_DEBUG:
    print(BASE_DIR)
    print(MEDIA_ROOT)
