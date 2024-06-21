my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

num = -1

while True:
    if num == len(my_list) or my_list[num] < 0:
        break

    num += 1
    if my_list[num] > 0:
        print(my_list[num])

