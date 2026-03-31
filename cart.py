class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"{product.name} a fost adaugat in cos")

    def total_price(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        print(f"Total de plata: {total} RON")

    def display_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
            return
        
        print("Produse in cos:")
        for product in self.cart_items:
            print(f"{product.name} - {product.price} RON x {product.quantity}")