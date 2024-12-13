from django.shortcuts import render
from django.views.generic import TemplateView

class maintpl(TemplateView):
    template_name = 'monitoring/index.html'

    title = "Мониторинг юридических лиц"
    header = "Главная страница"

    context = {
        "title": title,
        "header": header
    }
