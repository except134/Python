from django.shortcuts import render
from django.views.generic import TemplateView

def functpl(request):
    return render(request, 'func_template.html')

class classtpl(TemplateView):
    template_name = 'class_template.html'
