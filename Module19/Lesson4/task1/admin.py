from django.contrib import admin
from .models import Buyer, Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
     list_display = ('title', 'cost', 'size')
     list_filter = ('cost', 'size')
     list_max_show_all = 20
     search_fields = ['title']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
     list_display = ('name', 'balance', 'age')
     list_filter = ('balance', 'age')
     readonly_fields = ('balance',)
     list_max_show_all = 30
     search_fields = ['name']
