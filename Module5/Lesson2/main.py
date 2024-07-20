class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floor = number_of_floors

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floor}"

    def go_to(self, new_floor):
        #print(f'Передвигаемся по {self.name}, всего этажей {self.number_of_floor}, двигаемся на {new_floor} этаж')
        if new_floor > self.number_of_floor:
            print('Такого этажа не существует')
        else:
            i = 1
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

#h1.go_to(5)
#h2.go_to(10)
