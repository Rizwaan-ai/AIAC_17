class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name]['quantity'] += 1
        else:
            self.items[name] = {'price': price, 'quantity': 1}

    def remove_item(self, name):
        if name in self.items:
            if self.items[name]['quantity'] > 1:
                self.items[name]['quantity'] -= 1
            else:
                del self.items[name]

    def total_cost(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())
    def show_cart(self):
        for name, info in self.items.items():
            print(f"{name}: ${info['price']} x {info['quantity']}")