from bottle import route, view, post, request
from datetime import datetime
from settings import *
from getfiles import *
from parser import *
from tgbot import *

@route('/', method='GET')
@route('/home', method='GET')
@view('index')
def home():
    results = {}
    INN = request.GET.get('inn', '').strip()

    if INN:
        results = search_results(INN)

    return dict(
        title='Мониторинг ЮЛ',
        year=datetime.now().year,
        results=results
    )

@route('/contact')
@view('contact')
def contact():
    return dict(
        title='Мониторинг ЮЛ',
        message='Мои контакты',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    return dict(
        title='Мониторинг ЮЛ',
        message='Мониторинг ЮЛ',
        year=datetime.now().year
    )
