# Task 1
print("Task 1")
print("======")
my_dict = {"Игорь": 1970, "Иван": 1980, "Сергей": 1990}
print(my_dict)

print(my_dict["Иван"])
print(my_dict.get("Дмитрий"))

my_dict["Дитрий"] = 1975
my_dict["Андрей"] = 1985
print(my_dict)

del my_dict["Иван"]
print(my_dict)
print()

# Task 2
print("Task 2")
print("======")
my_set = {2, 3, 4, 5, True, False, 4.5, "String", 3, 2, False, "String"}
print(my_set)

my_set.update([6, 7, 8])
print(my_set)

my_set.discard(7)
print(my_set)

