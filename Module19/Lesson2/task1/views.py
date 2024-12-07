from django.shortcuts import render
from django.http import HttpRequest
from .models import *

def add_initial_data():
    Game.objects.all().delete()
    Buyer.objects.all().delete()

    b1 = Buyer.objects.create(name='Ilya', balance=1500, age=24)
    b2 = Buyer.objects.create(name='Nagibator', balance=42.15, age=52)
    b3 = Buyer.objects.create(name='Ubivator', balance=0.5, age=16)

    g1 = Game.objects.create(title='Cyberpunk 2077', cost=31, size=46.2, description='Game of year', age_limited=True)
    g2 = Game.objects.create(title='Mario', cost=5, size=0.5, description='Old game')
    g3 = Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=True)

    g1.buyer.set((b1, b2))
    g2.buyer.set((b2, b3))
    g3.buyer.set((b1, b2))

def home(request):
    assert isinstance(request, HttpRequest)

    add_initial_data()

    return render(
        request,
        'task1/index.html',
        {
            'title':'Home Page',
        }
    )
