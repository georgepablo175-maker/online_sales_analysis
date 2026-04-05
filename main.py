from product import Product
from product_manager import ProductManager
from cart import Cart

# creez managerul
manager = ProductManager()

# adaug produse
p1 = Product("Telefon Samsung", 2500, 2)
p2 = Product("Laptop Gaming", 5000, 1)
p3 = Product("Mouse", 150, 4)

manager.add_products(p1)
manager.add_products(p2) 
manager.add_products(p3)

# afisez produse
print("\nLista produse:")
manager.display_all_products()

# afisam valoare totala
manager.total_value()

# creez cosul
cart = Cart(manager)

# adaug 3 produse din lista managerului
cart.add_to_cart("Telefon Samsung")
cart.add_to_cart("Laptop Gaming")
cart.add_to_cart("Mouse")

# afisez cosul
cart.display_cart()

# total de plata
cart.total_price()

manager.remove_product("Laptop Gaming")
