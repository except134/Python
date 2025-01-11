from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
from .getfiles import *
from .parser import *

def search_results(search):
    results = {}
    file_names = {
        "aaa.txt": "Для теста", 
        "Lombard.txt": "Государственный реестр ломбардов", 
        "RZHNK.txt": "Жилищные накопительные кооперативы", 
        "SKPK.txt": "Государственный реестр сельскохозяйственных кредитных потребительских кооперативов", 
        "MFO.txt": "Государственный реестр микрофинансовых организаций", 
        "KPKGOV.txt": "Государственный реестр кредитных потребительских кооперативов", 
        "MFOP.txt": "Перечень микрофинансовых организаций", 
        "SPB.txt": "ПАО «СПБ Биржа»", 
        "Zakup.txt": "Единая информационная система в сфере закупок"}

    inn = search

    if inn:
        get_all_files()
        OUTPUT_DIR = settings.MEDIA_ROOT
        for f, n in file_names.items():
            file_path = os.path.join(OUTPUT_DIR, f)
            ret = import_from_txt(file_path, inn)
            if settings.PRINT_DEBUG:
                print(f"{n}: {inn} - {ret}")
            results[n] = "Найден" if ret else "Не найден"

        ret = get_egrul(inn)    
        if settings.PRINT_DEBUG:
            print(f"ЕГРЮЛ: {inn} - {ret}")
        results['ЕГРЮЛ'] = "Найден" if ret else "Не найден"

#        ret = get_inn_ofd(inn, ret)
#        if settings.PRINT_DEBUG:
#            print(f"Единый реестр субъектов малого и среднего предпринимательства: {inn} - {ret}")
#        results['Единый реестр субъектов малого и среднего предпринимательства'] = "Найден" if ret else "Не найден"

    if settings.PRINT_DEBUG:
        print(results)

    if not results:
        flash('По данному ИНН ничего не найдено!')

    return results

def home(request):
    assert isinstance(request, HttpRequest)
    results = {}

    if request.method == 'POST':
        inn = request.POST.get('inn', '')
        results = search_results(inn)

    return render(
        request,
        'app/index.html',
        {
            'title':'Мониторинг ЮЛ',
            'year':datetime.now().year,
            'results': results,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Мониторинг ЮЛ',
            'message':'Мои контакты',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Мониторинг ЮЛ',
            'message':'Мониторинг ЮЛ',
            'year':datetime.now().year,
        }
    )
