from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)
        print(f"Produsul {product.name} a fost adaugat.")

    def display_all_products(self):
        if not self.products:
            print("Nu exista produse.")
        for product in self.products:
            product.display_info()
            print("-------")

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Valoarea totala a produselor: {total} RON")


    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Produsul {name} a fost eliminat.")
                return
        print(f"Produsul {name} nu a fost gasit.")