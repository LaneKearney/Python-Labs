from Drink import Drink
class Juice(Drink):
    def __init__(self, size:str, price:float, ingredients:str):
        super().__init__(size, price)
        self.ingredients = ingredients
    def info(self):
        return f"{'/'.join(self.ingredients)} Juice, {super().info()}"

    