class DrinkOrder:
    def __init__(self):
        self.drinks = []
    def add(self, drink):
        self.drinks.append(drink)
    def total(self):
        if not self.drinks:
            return "Order Items:\nTotal Price: $0.00"
        order_items = "\n".join([f"* {drink.info()}" for drink in self.drinks])
        total_price = sum([drink.getPrice() for drink in self.drinks])

        return f"Order Items:\n{order_items}\nTotal Price: ${total_price:.2f}"
    


