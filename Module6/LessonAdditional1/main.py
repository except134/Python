from math import pi, sin

class Figure:
   sides_count = 0
   __sides = list()
   __color = list()
   filled = False

   def __init__(self, rgb, *sides):
       self.set_color(*rgb)
       self.__sides = list(sides)

   def get_color(self):
       return self.__color

   def __is_valid_color(self, r, g, b):
       correct_color = False
       if 0 <= r <= 255:
           if 0 <= g <= 255:
               if 0 <= b <= 255:
                   return True
               else:
                   return False
           else:
               return False
       else:
           return False

   def set_color(self, r=None, g=None, b=None):
       if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]
           self.filled = True
   
   def __is_valid_sides(self, *args):
       _flag = False
       if len(args) == len(self.__sides) and len(args) == self.sides_count:
           for arg in args:
               if isinstance(arg, int):
                   if arg > 0:
                       _flag = True
                   else:
                       return False
               else:
                   return False
       return _flag

   def get_sides(self):
       return self.__sides

   def __len__(self):
       return sum(self.__sides)

   def set_sides(self, *new_sides):
       if self.__is_valid_sides(*new_sides):
           self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    __radius = float()

    def __init__(self, rgb, *sides):
        if len(sides) == self.sides_count:
            _side = sides[0]
        else:
            _side = 1
        self.__radius = _side / (2 * pi)
        super().__init__(rgb, _side)

    def get_square(self):
        _square = pi * self.__radius ** 2
        return round(_square, 2)

class Triangle(Figure):
   sides_count = 3
   __height = None

   def __init__(self, rgb, *sides):
       if len(sides) == self.sides_count:
           _side = sides
       else:
           _side = (1, 1, 1)
       super().__init__(rgb, *_side)

   def get_square(self):
       _a = self._Figure__sides[0]
       _b = self._Figure__sides[1]
       _c = self._Figure__sides[2]
       square_triangle = (_a * _b) / 2 * sin(_c)
       return square_triangle

class Cube(Figure):
   sides_count = 12

   def __init__(self, rgb, *sides):
       _sides = []
       if len(sides) == 1:
           for i in range(self.sides_count):
               _sides.append(sides[0])
       else:
           _sides = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
       super().__init__(rgb, *_sides)

   def get_volume(self):
       _one_side = self._Figure__sides[0]
       _volume = _one_side ** 3
       return _volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
