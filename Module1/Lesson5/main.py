immutable_var = (1, 2, 3, True, "String", 4.5)
print(immutable_var)

# Кортеж нельзя изменить, только для чтения
# immutable_var[0] = 10

mutable_list = [1, 2, 3, True, "String", 4.5]
print(mutable_list)

mutable_list[2] = immutable_var[5]
mutable_list[3] = False
print(mutable_list)


