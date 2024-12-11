from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from .models import *
from .forms import *

def add_initial_data():
    Game.objects.all().delete()
    Buyer.objects.all().delete()

    b1 = Buyer.objects.create(name='Ilya', balance=1500, age=24, password='11111111')
    b2 = Buyer.objects.create(name='Nagibator', balance=42.15, age=52, password='11111111')
    b3 = Buyer.objects.create(name='Ubivator', balance=0.5, age=16, password='11111111')

    g1 = Game.objects.create(title='Cyberpunk 2077', cost=31, size=46.2, description='Game of year', age_limited=True)
    g2 = Game.objects.create(title='Mario', cost=5, size=0.5, description='Old game')
    g3 = Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=True)

    g1.buyer.set((b1, b2))
    g2.buyer.set((b2, b3))
    g3.buyer.set((b1, b2))

def create_test_db(request):
    assert isinstance(request, HttpRequest)

    add_initial_data()

    return render(
        request,
        'task1/createdb.html',
        {
            'title':'Home Page',
        }
    )

def check_errors(username, password, repeat_password, age, balance, info):
    ret = False

    try:
        user = Buyer.objects.get(name=username)
    except:
        user = None

    if password != repeat_password:
        info['error'] = 'Пароли не совпадают'
    elif age < 18:
        info['error'] = 'Вы должны быть старше 18'
    elif user and username == user.name:
        info['error'] = 'Пользователь уже существует'
    elif balance < 0:
        info['error'] = 'Баланс не может быть отрицательным'
    else:
        info['success'] = f'Приветствуем, {username}!'
        ret = True

    return ret

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        age = int(request.POST.get('age', 0))
        balance = int(request.POST.get('balance', 0))

        ret = check_errors(username, password, repeat_password, age, balance, info)

        if ret == True:
            Buyer.objects.create(name=username, balance=balance, age=age, password=password)

    return render(request, 'task1/registration_page.html', info)

def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']
        balance = form.cleaned_data['balance']

        ret = check_errors(username, password, repeat_password, age, balance, info)

        if ret == True:
            Buyer.objects.create(name=username, balance=balance, age=age, password=password)

    info['form'] = form
    return render(request, 'task1/registration_page.html', info)

class platformtpl(TemplateView):
    template_name = 'task1/platform.html'

    title = "Магазин игр"
    header = "Главная страница"

    context = {
        "title": title,
        "header": header
    }

class gamestpl(TemplateView):
    template_name = 'task1/games.html'

    title = "Магазин игр"
    header = "Игры"

    gameslist = {}
    games = Game.objects.all()
    for game in games:
        gameslist[game.title] = {'desc': game.description, 'cost': game.cost}

    context = {
        "title": title,
        "header": header,
        "gameslist": gameslist
    }

class carttpl(TemplateView):
    template_name = 'task1/cart.html'

    title = "Магазин игр"
    header = "Корзина"

    context = {
        "title": title,
        "header": header
    }

def add_game(request):
    info = {}
    form = AddGame(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data['title']
        cost = form.cleaned_data['cost']
        size = form.cleaned_data['size']
        description = form.cleaned_data['description']
        age_limited = form.cleaned_data['age_limited']

        Game.objects.create(title=title, cost=cost, size=size, description=description, age_limited=age_limited)

    info['form'] = form
    return render(request, 'task1/admin.html', info)

