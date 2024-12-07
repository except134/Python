from django.shortcuts import render
from .forms import UserRegister

users = []

def check_errors(username, password, repeat_password, age, info):
    ret = False

    if password != repeat_password:
        info['error'] = 'Пароли не совпадают'
    elif age < 18:
        info['error'] = 'Вы должны быть старше 18'
    elif username in users:
        info['error'] = 'Пользователь уже существует'
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

        ret = check_errors(username, password, repeat_password, age, info)

        if ret == True:
            users.append(username)

    return render(request, 'registration_page.html', info)

def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']

        ret = check_errors(username, password, repeat_password, age, info)

        if ret == True:
            users.append(username)

    info['form'] = form
    return render(request, 'registration_page.html', info)
