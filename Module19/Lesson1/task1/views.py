from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'task1/index.html',
        {
            'title':'Home Page',
        }
    )
