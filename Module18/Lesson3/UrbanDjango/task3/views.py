from django.shortcuts import render
from django.views.generic import TemplateView

class platformtpl(TemplateView):
    template_name = 'platform.html'

    title = "Магазин игр"
    header = "Главная страница"

    context = {
        "title": title,
        "header": header
    }

class gamestpl(TemplateView):
    template_name = 'games.html'

    title = "Магазин игр"
    header = "Игры"

    gameslist = ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]

    context = {
        "title": title,
        "header": header,
        "gameslist": gameslist
    }

class carttpl(TemplateView):
    template_name = 'cart.html'

    title = "Магазин игр"
    header = "Корзина"

    context = {
        "title": title,
        "header": header
    }
