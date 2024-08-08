import io

def custom_write(file_name, strings):
    ret = {}
    file = open(file_name, "w", encoding='utf-8')
    line_no = 1

    for i in strings:
        ret[(line_no, file.tell())] = i
        file.write(i + "\n")
        line_no += 1
    
    file.close()
    return ret

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)