class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floor = number_of_floors

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floor}"
    
    def __bool__(self):
        return bool(self.number_of_floor)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floor == other
        elif isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        else:
            print("== не известный тип")

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floor < other
        elif isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        else:
            print("< не известный тип")

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floor <= other
        elif isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        else:
            print("<= не известный тип")

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floor > other
        elif isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        else:
            print("> не известный тип")

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floor >= other
        elif isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        else:
            print(">= не известный тип")

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floor != other
        elif isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        else:
            print("!= не известный тип")

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floor + other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floor + other.number_of_floor)
        else:
            return self

    def __radd__(self, other):
        return self + other 

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floor - other)
        elif isinstance(other, House):
            return House(self.name, self.number_of_floor - other.number_of_floor)
        else:
            return self

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self = self - other
        return self
 
    def go_to(self, new_floor):
        #print(f'Передвигаемся по {self.name}, всего этажей {self.number_of_floor}, двигаемся на {new_floor} этаж')
        if new_floor > self.number_of_floor:
            print('Такого этажа не существует')
        else:
            i = 1
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
