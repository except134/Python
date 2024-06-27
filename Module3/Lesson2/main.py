def check_for_email(s):
    chars = (".com", ".ru", ".net")
    s.lower()
    if s.count('@') == 1 and s[0] != '@' and s.endswith(chars):
        return True
    return False

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if not check_for_email(recipient) or not check_for_email(sender):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
    elif recipient.lower() == sender.lower():
        print("Нельзя отправить письмо самому себе!")
    elif sender.lower() == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>")
    
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

