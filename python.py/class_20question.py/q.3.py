class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total_price = 0
        for item_name, item_info in self.items.items():
            total_price += item_info['price'] * item_info['quantity']
        return total_price

# Example usage:
cart = ShoppingCart()

cart.add_item("Apple", 0.5, 3)
cart.add_item("Banana", 0.3, 2)
cart.add_item("Orange", 0.6)

print("Current items in the cart:")
for item_name, item_info in cart.items.items():
    print(f"{item_name}: {item_info['quantity']} x ${item_info['price']} each")

total_price = cart.calculate_total()
print(f"\nTotal Price: ${total_price}")
