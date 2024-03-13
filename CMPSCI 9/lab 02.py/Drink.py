class Drink:
    
    def __init__(self, size:str, price:float):
        self.size = size
        self.price = price
    def updateSize(self, newSize):
        self.size = newSize
    def updatePrice(self, newPrice):
        self.price = newPrice
    def getSize(self):
        return self.size
    def getPrice(self):
        return self.price
    def info(self):
        return f"{self.size}: ${self.price:.2f}"



