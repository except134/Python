class Vehicle:
    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = power
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        
    def set_color(self, newcolor):
        if newcolor.lower() in self.__COLOR_VARIANTS:
            self.__color = newcolor
        else:
            print(f"Нельзя сменить цвет на {newcolor}")

    def get_color(self):
        return self.__color

    def get_owner(self):
        return self.owner

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power
            

class Sedan(Vehicle):
    def __init__(self, owner, model, color, power):
        self.__PASSENGERS_LIMIT = 5
        super().__init__(owner, model, color, power)

    def print_info(self):
        print(f"Модель: ", self.get_model())
        print(f"Мощность двигателя: ", self.get_horsepower())
        print(f"Цвет: ", self.get_color())
        print(f"Владелец: ", self.get_owner())

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

