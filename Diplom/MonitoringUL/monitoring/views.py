from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from .parser import *
from .config import *

file_names = ["aaa.txt", "Lombard.txt", "RZHNK.txt", "SKPK.txt", "MFO.txt", "KPKGOV.txt", "MFOP.txt", "SPB.txt", "Zakup.txt"]

def get_inn_from_html(request):
    info = {}
    temp_result = {}

    info['title'] = "Мониторинг юридических лиц"
    info['header'] = "Главная страница"

    if request.method == 'POST':
        inn = request.POST.get('inn', '')
        if inn:
            OUTPUT_DIR = settings.MEDIA_ROOT
            for f in file_names:
                file_path = os.path.join(OUTPUT_DIR, f)
                ret = import_from_txt(file_path, inn)
                if PRINT_DEBUG:
                    print(f"{f}: {inn} - {ret}")
                temp_result[f] = ret

            ret = get_egrul(inn)    
            if PRINT_DEBUG:
                print(f"ЕГРЮЛ: {inn} - {ret}")
            temp_result['egrul'] = ret
            ret = get_inn_ofd(inn)
            if PRINT_DEBUG:
                print(f"ОФД: {inn} - {ret}")
            temp_result['ofd'] = ret

    if PRINT_DEBUG:
        print(temp_result)

    info['temp_results'] = temp_result

    return render(request, 'monitoring/index.html', info)

