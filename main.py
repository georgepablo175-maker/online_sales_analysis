from product import Product
from product_manager import ProductManager
from cart import Cart

# creez managerul
manager = ProductManager

# adaug produse
p1 = Product("Telefon Samsung", 2500, 2)
p2 = Product("Laptop Gaming", 5000, 1)
p3 = Product("Mouse", 150, 4)

manager.add_product(p1)
manager.add_product(p2) 
manager.add_product(p3)

# afisez produse
print("\nLista produse:")
manager.display_all_products()

# afisam valoare totala
manager.total_value()

# creez cosul
cart = Cart()

# adaug 3 produse din lista managerului
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

# afisez cosul
cart.display_cart()

# total de plata
cart.total_price()
