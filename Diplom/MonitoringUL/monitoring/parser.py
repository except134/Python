import os
import fnmatch
import re
import time 
import requests
import json
import traceback
import datetime 
from django.conf import settings
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

def import_from_txt(file_path: str, like_pattern: str) -> bool:
    import_result = False
    
    if not os.path.isfile(file_path):
        return import_result

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if fnmatch.fnmatch(line.strip(), like_pattern):
                import_result = True
                break

    return import_result

def get_egrul(inn: str):
    OUTPUT_DIR = settings.MEDIA_ROOT
    query = inn
    s = requests.Session()

    r = s.get("https://egrul.nalog.ru/index.html",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            }
        )

    req = requests.Request(
        'POST',
        'https://egrul.nalog.ru/',
        data=b'vyp3CaptchaToken=&page=&query='+query.encode()+b'&region=&PreventChromeAutocomplete=', 
        headers = {
        "Host": "egrul.nalog.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://egrul.nalog.ru/index.html",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest"
        }
        )

    r = s.prepare_request(req)
    r = s.send(r)
    item = json.loads(r.text)

    try:
        if item["ERRORS"] != '' and (item["ERRORS"])["captchaSearch"] != '':
            while True:
                r = s.get('https://egrul.nalog.ru/captcha-dialog.html',
                headers = {
                    "Host": "egrul.nalog.ru",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Referer": "https://egrul.nalog.ru/index.html",
                    "Pragma": "no-cache",
                    "Cache-Control": "no-cache"
                })
                b = bs4.BeautifulSoup(r.content.decode(),features="lxml").find('div',class_='field-data').find('img').get('src')
                webbrowser.open('https://egrul.nalog.ru' + b)
                ct = b.split('?a=')[1].split('&')[0]
                captcha = input('Введите капчу: ')

                r = requests.Request(
                'POST',
                'https://egrul.nalog.ru/captcha-proc.json',
                data=b'captcha='+captcha.encode()+b'&captchaToken='+ct.encode(), 
                headers = {
                    "Host": "egrul.nalog.ru",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://egrul.nalog.ru/index.html"
                    }
                )

                r = s.prepare_request(req)
                r = s.send(r)
                item = json.loads(r.text)

                try:
                    tr = False
                    if item["ERRORS"] != '':
                        tr = True
                except Exception as e:
                    print(e)
                    pass
                if tr == False: break
                

    except Exception as e:
        print(e)
        pass
    t = json.loads(r.text)['t']

    time.sleep(0.5)

    r = s.get("https://egrul.nalog.ru/search-result/"+str(t),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Referer": "https://egrul.nalog.ru/index.html"
            }
        )

    jsn = json.loads(r.text)

    try:
        while True:
            if jsn['status'] != 'wait': break
            time.sleep(0.2)
    except Exception:
        pass

    try:
        item = (jsn["rows"])[0]
        itemParse = ''

        itemParse += item['n'] + '\n'
        try:
            itemParse += item['g'] + '\n'
        except Exception:
            pass
        try:
            itemParse += 'Адрес: ' + item['a']+'\n'
        except Exception:
            pass
        itemParse += 'ИНН: ' + item['i']+'\n'
        itemParse += 'ОГРН: ' + item['o']+'\n'
        try:
            itemParse += 'КПП: ' + item['p']+'\n'
        except Exception:
            pass
        itemParse += 'Дата регистрации: ' + item['r']+'\n'

        try:
            itemParse += 'ДАТА ПРЕКРАЩЕНИЯ ДЕЯТЕЛЬНОСТИ: ' + item['e']+'\n'
        except Exception:
            pass

        if str(item['tot']) != '0':
            if len(item['n']) < 50: name = str(item['n'])
            else: name = str(item['i'])

            name = name.replace('"',"'").replace('\\','⧵').replace('/','⁄').replace('|','¦').replace(':',';').replace('*','✱').replace('?','').replace('<','«').replace('>','»')

            cur_date = datetime.date.today().strftime("%d.%m.%Y")
            output_folder = OUTPUT_DIR + '\\' + cur_date + '\\' + name+'\\'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            f = open(output_folder+name+'.txt','w+',encoding='utf-8')
            f.write('по состоянию на ' + str(datetime.datetime.strftime(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))),'%x %X %Z')).replace('/','.')+'\n'+str(itemParse))
            f.close()

            t = item['t']

            r = s.get("https://egrul.nalog.ru/vyp-request/"+str(t),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Referer": "https://egrul.nalog.ru/index.html"
                    }
                )
            time.sleep(0.5)
            while True:
                r = s.get("https://egrul.nalog.ru/vyp-status/"+str(t),
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Referer": "https://egrul.nalog.ru/index.html"
                        }
                    )
                st = json.loads(r.text)['status']
                if st == 'ready': break
                time.sleep(0.5)

            r = s.get("https://egrul.nalog.ru/vyp-download/"+str(t),
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Referer": "https://egrul.nalog.ru/index.html"
                        }
                    )

            f = open(output_folder+f'ИНН_{inn} {item['n'].replace('"','')}_{cur_date}.pdf','wb+')
            f.write(r.content)
            f.close()
            time.sleep(5)
            return True

    except Exception as e:
        print(e)
        traceback.print_exc()
        return False

def get_inn_ofd(srch_inn):
    try:
        # Initialize the webdriver (you may need to specify the path to your webdriver)
        driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox
        driver.set_window_position(-2000, 0)  # Move the window off-screen

        # Navigate to the website
        driver.get("https://ofd.nalog.ru/#")

        # Wait for the search input to be present and fill it
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "query"))
        )
        search_input.send_keys(srch_inn)

        # Click the search button
        search_button = driver.find_element(By.CSS_SELECTOR, "#pnlSearch > div.quick-search-controls.form-layout-top-labels > div.form-field > div > div.field-value > button")
        search_button.click()

        # Wait for 1 second
        time.sleep(1)

        # Get the text from the specified element
        temp = driver.find_element(By.CSS_SELECTOR, "#tblResultData > tr > td:nth-child(2) > span").text

        # Check if the text is "Микропредприятие" (note: using the actual Russian text here)
        return temp == "Микропредприятие"

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the browser
        driver.quit()
