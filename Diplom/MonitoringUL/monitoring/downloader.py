import os
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from .excelutils import *
from .config import *
from django.conf import settings

def download_file_api(s_file_url, to_path_name, params=None, **kwargs):
    # s_file_url - URL загружаемого файла
    # to_path_name - путь для сохранения файла
    try:
        if params == None:
            response = requests.get(s_file_url)
        else:
            response = requests.get(s_file_url, params)
        response.raise_for_status()  # вызвать ошибку при плохом ответе
        with open(to_path_name, 'xb') as file:
            file.write(response.content)
        return True  
    except Exception as e:
        print(f"Failed to download file: {e}")
        return False  

def call_download(s_file_url: str, s_file_name: str, params=None, **kwargs) -> bool:
    # s_file_url  - URL для скачивания файла
    # s_file_name - имя файла с расширением, которое будет присутствовать при скачивании
    s_file_path = settings.MEDIA_ROOT

    resfile = os.path.join(s_file_path, s_file_name)

    if os.path.exists(resfile):
        os.remove(resfile)

    h = download_file_api(s_file_url, resfile, params)
    
    return h

def download_file(s_file_url: str, s_file_name: str, with_excel = True, params=None, **kwargs):
    OUTPUT_DIR = settings.MEDIA_ROOT
    file_path = os.path.join(OUTPUT_DIR, f"{s_file_name}.txt")

    if os.path.exists(file_path):
        os.remove(file_path)

    if with_excel:
        ext = "xlsx"
    else:
        ext = "txt"

    ret = call_download(s_file_url, f"{s_file_name}.{ext}", params)

    if with_excel and ret:
        str_file_path = os.path.join(os.getcwd(), OUTPUT_DIR, f"{s_file_name}.xlsx")
        str_dir_file = os.path.join(os.getcwd(), OUTPUT_DIR, f"{s_file_name}.txt")
        export_all_sheets_to_txt(str_dir_file, str_file_path)

