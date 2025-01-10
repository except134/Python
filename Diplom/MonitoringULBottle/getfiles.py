import asyncio
import re
import requests
import json
import webbrowser
import openpyxl
from datetime import datetime 
import time 
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import typing
from downloader import *
from settings import *
from parser import *

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
        OUTPUT_DIR = MEDIA_ROOT
        for f, n in file_names.items():
            file_path = os.path.join(OUTPUT_DIR, f)
            ret = import_from_txt(file_path, inn)
            if PRINT_DEBUG:
                print(f"{n}: {inn} - {ret}")
            results[n] = "Найден" if ret else "Не найден"

        ret = get_egrul(inn)    
        if PRINT_DEBUG:
            print(f"ЕГРЮЛ: {inn} - {ret}")
        results['ЕГРЮЛ'] = "Найден" if ret else "Не найден"

        #ret = get_inn_ofd(inn, ret)
        #if PRINT_DEBUG:
        #    print(f"Единый реестр субъектов малого и среднего предпринимательства: {inn} - {ret}")
        #results['Единый реестр субъектов малого и среднего предпринимательства'] = "Найден" if ret else "Не найден"

    if PRINT_DEBUG:
        print(results)

    if not results:
        return 'По данному ИНН ничего не найдено!'

    return results

def get_tags(text, tag, attribute, pattern, value_attribute):
    regex = f'<{tag}[^>]*{attribute}="[^"]*{pattern}[^"]*"[^>]*{value_attribute}="([^"]*)"'
    match = re.search(regex, text)
    if match:
        return match.group(1)
    return ""

def prepare_reg_file():
    url = "https://cbr.ru/microfinance/registry/"
    
    response = requests.get(url)
    txt = response.text
    
    description = get_tags(txt, "a", "data-zoom-referer", r".*/microfinance/#a_148281.*", "href")
    description = "https://cbr.ru" + description

    return description

def get_all_files():
    OUTPUT_DIR = MEDIA_ROOT

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    download_file("https://cbr.ru/vfs/finmarkets/files/supervision/list_PS.xlsx", "Lombard")
    download_file("https://cbr.ru/vfs/finmarkets/files/supervision/list_ZHNK.xlsx", "RZHNK")
    download_file("https://cbr.ru/vfs/finmarkets/files/supervision/list_skpk.xlsx", "SKPK")
    download_file("https://cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx", "MFO")
    download_file("https://cbr.ru/vfs/finmarkets/files/supervision/list_KPK_gov.xlsx", "KPKGOV")
    download_file(prepare_reg_file(), "MFOP")
    #download_file("https://web.moex.com/moex-web-icdb-api/api/v2/export/ru_securities-list", "MB", False, {"Format.Type": "csv", "Data.Direction": "asc", "Data.Language": "ru", "Format.Delimiter": "comma"})
    download_file("https://spbexchange.ru/api/listing/v1/list/export?fileName=ListingSecurityList", "SPB", False)
    #download_file("https://spvb.ru/rynki/fondovyy-rynok/uchastniki-torgov-v-fondovoy-sektsii-ao-spvb/", "SPVB", False)
    download_file("https://zakupki.gov.ru/epz/dishonestsupplier/search/rss", "Zakup", False)

