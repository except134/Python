first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")

if first == second and first == third:
    print("3")
elif first == second or first == third or second == third:
    print("2")
else:
    print("0")
    