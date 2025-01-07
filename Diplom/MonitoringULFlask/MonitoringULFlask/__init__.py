"""
The flask application package.
"""

from flask import Flask
import os
from .settings import *

class MyApp(Flask):
    def __init__(self, import_name: str):
        super().__init__(import_name=import_name)

    def run(
        self,
        host: str | None = None,
        port: int | None = None
    ):
        super().run(host=host, port=port)

app = MyApp(__name__)
app.config['SECRET_KEY'] = WEB_SECRET_KEY
app.config['TG_KEY'] = TG_KEY
app.config['PRINT_DEBUG'] = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config['MEDIA_ROOT'] = os.path.join(BASE_DIR, 'PS_INFO')

import MonitoringULFlask.views
