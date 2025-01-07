"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, flash
from MonitoringULFlask import app
from .forms import INNSearchForm
from .getfiles import *
from .parser import *
from threading import Thread, Lock

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    results = {}

    search = INNSearchForm(request.form)
    if request.method == 'POST':
        results = search_results(search.data['search'])

    return render_template(
        'index.html',
        title='Мониторинг ЮЛ',
        year=datetime.now().year,
        form=search,
        results=results
    )

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
        OUTPUT_DIR = app.config['MEDIA_ROOT']
        for f, n in file_names.items():
            file_path = os.path.join(OUTPUT_DIR, f)
            ret = import_from_txt(file_path, inn)
            if app.config['PRINT_DEBUG']:
                print(f"{n}: {inn} - {ret}")
            results[n] = "Найден" if ret else "Не найден"

        ret = get_egrul(inn)    
        if app.config['PRINT_DEBUG']:
            print(f"ЕГРЮЛ: {inn} - {ret}")
        results['ЕГРЮЛ'] = "Найден" if ret else "Не найден"

#        ret = get_inn_ofd(inn, ret)
#        if app.config['PRINT_DEBUG']:
#            print(f"Единая информационная система в сфере закупок: {inn} - {ret}")
#        results['Единая информационная система в сфере закупок'] = "Найден" if ret else "Не найден"

    if app.config['PRINT_DEBUG']:
        print(results)

    if not results:
        flash('По данному ИНН ничего не найдено!')

    return results

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Мониторинг ЮЛ',
        year=datetime.now().year,
        message='Мои контакты'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Мониторинг ЮЛ',
        year=datetime.now().year,
        message='Мониторинг ЮЛ'
    )
