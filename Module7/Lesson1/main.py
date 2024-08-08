from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name +', ' + str(self.weight) + ', ' + self.category 

class Shop:
    __file_name = "products.txt"
    
    def __init__(self):
        self.products = []
        try:
            file = open(Shop.__file_name, mode='r')
        except:
            return
        
        line = True
        while line:
            line = file.readline()
            products = self.get_products()
            splitted = line.split(sep=',');
            if not splitted[0] in products:
                self.products.append(line)
            else:   
                print(f"Продукт {line[0]} уже есть в магазине")
        file.close()

    def get_products(self):
        return self.products

    def add(self, *products):
        for name in products:
            line = str(name)
            products = self.get_products()
            splitted = line.split(sep=',');
            if splitted[0] in products:
                print(f"Продукт {name} уже есть в магазине")
            else:
                file = open(Shop.__file_name, mode='a')
                self.products.append(name)
                file.writelines(str(name))
                file.close()
        

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
