def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

# Task 1
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2, 3)
print_params()
print()

# Task 2
values_list = ['Строка', False, 55]
values_dict = {'a': 3.14, 'b':False, 'c':10}
print_params(*values_list)
print_params(**values_dict)
print()

# Task 3
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


