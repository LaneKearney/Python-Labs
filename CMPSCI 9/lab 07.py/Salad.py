class Salad:
    def __init__(self, size: str):
        self.price = 0.0
        self.size = size
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_size(self):
        return self.size
    def set_size(self, size):
        self.size = size
    