# Task 1
print("Task 1")
print("======")
my_dict = {"Игорь": 1970, "Иван": 1980, "Сергей": 1990}
print("Dict:", my_dict)

print("Existing value:", my_dict["Иван"])
print("Not existing value:", my_dict.get("Дмитрий"))

my_dict["Дитрий"] = 1975
my_dict["Андрей"] = 1985
print("New dict:", my_dict)

for_delete = my_dict["Иван"]
del my_dict["Иван"]
print("Deleted value:", for_delete)
print("Modified dict:", my_dict)
print()

# Task 2
print("Task 2")
print("======")
my_set = {2, 3, 4, 5, True, False, 4.5, "String", 3, 2, False, "String"}
print("Set:", my_set)

my_set.update([6, 7, 8])
print("Modified set:", my_set)

my_set.discard(7)
print("Set after delete:", my_set)

