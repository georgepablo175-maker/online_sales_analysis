from product import Product
from product_manager import ProductManager

# creez managerul
manager = ProductManager

# adaug produse
p1 = Product("Telefon Samsung", 2500, 2)
p2 = Product("Laptop Gaming", 5000, 1)
p3 = Product("Mouse", 150, 4)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)