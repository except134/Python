# Task 1
print("Задача 1")
print("========")
separator = input("Введите строку-разделитель: ")
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str3 = input("Введите третью строку: ")

print(str1, str2, str3, sep = separator)
print()

# Task 2
print("Задача 2")
print("========")
print("Вычесляем формулу f(a, b) = 3(a+b)^3+275b^2−127a−41\n")
a = int(input("Введите параметр a: "))
b = int(input("Введите параметр b: "))

result = 3 * (a + b)**3 + (275*b)**2 - 127 * a - 41
print(result)

print()

# Task 3
print("Задача 3")
print("========")

num = int(input("Введите целое число: "))

print(f"Следующее за числом {num} число: {num + 1}")
print(f"Для числа {num} предыдущее число: {num - 1}")

print()

# Task 4
print("Задача 4")
print("========")

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))

print("Сумма:", a + b)
print("Разность:", abs(a - b))
print("Произведение:", a * b)

print()

# Task 5
print("Задача 5")
print("========")

a1 = int(input("Введите a1: "))
d = int(input("Введите d: "))
n = int(input("Введите n: "))

print("Результат:", a1 + d * (n - 1))

print()

# Task 6
print("Задача 6")
print("========")

num = input("Введите трехзначное число (при вводе отрицательного, будет переведено в положительное): ")
if len(num) != 3:
    print("Ошибка: В веденном числе должно быть три цифры!")
else:
    num = abs(int(num))
    n3 = num % 10
    n2 = num %100 // 10
    n1 = num // 100
    print("Сумма цифр:", n1 + n2 + n3)
    print("Произведение цифр:", n1 * n2 * n3)

print()

# Task 7
print("Задача 7")
print("========")

num = input("Введите трехзначное число (при вводе отрицательного, будет переведено в положительное): ")

if len(num) != 3:
    print("Ошибка: В веденном числе должно быть три цифры!")
else:
    num = abs(int(num))
    c = num % 10
    b = num %100 // 10
    a = num // 100

    if a == b or a == c or b == c:
        print("Ошибка: В веденном числе все цифры должны быть различны!")
    else:
        print(a, b, c)
        print(a, c, b)
        print(b, a, c)
        print(b, c, a)
        print(c, a, b)
        print(c, b, a)

print()

# Task 8
print("Задача 8")
print("========")

num = input("Введите четырехзначное число (при вводе отрицательного, будет переведено в положительное): ")

if len(num) != 4:
    print("Ошибка: В веденном числе должно быть четыре цифры!")
else:
    num = abs(int(num))
    n4 = num % 10
    n3 = num % 100 // 10
    n2 = num // 100 % 10
    n1 = num // 1000
    
    print("Цифра в позиции тысяч равна:", n1)
    print("Цифра в позиции сотен равна:", n2)
    print("Цифра в позиции десятков равна:", n3)
    print("Цифра в позиции единиц равна:", n4)


