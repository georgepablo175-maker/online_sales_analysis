from product import Product
from product_manager import ProductManager

# creez managerul
manager = ProductManager

# adaug produse
p1 = Product("Telefon", 2000, 3)
p2 = Product("Laptop", 3500, 2)
p3 = Product("Casti", 300, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# afisez produse
print("\nLista produse:")
manager.display_all_products()

# afisam valoare totala
manager.total_value()