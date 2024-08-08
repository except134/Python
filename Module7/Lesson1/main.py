from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {str(self.weight)}, {self.category}" 

class Shop:
    __file_name = "products.txt"
    
    def __init__(self):
        self.products = []

    def get_products(self):
        try:
            file = open(Shop.__file_name, mode='r')
            ret = file.read()
            file.close()
            return str(ret)
        except:
            return ""

    def add(self, *products):
        file = open(Shop.__file_name, mode='a')
        store_products = self.get_products()
        for product in products:
            if product.name not in store_products:
                file.write(str(product) + '\n')
                store_products += product.name + '\n'
            else:
                print(f"Продукт {product.name} уже есть в магазине")
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
