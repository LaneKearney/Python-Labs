from Drink import Drink

class Tea(Drink):
    def __init__(self, size:str, price:float, style:str):
        super().__init__(size,price)
        self.style = style
    def info(self):
         return f"{self.style} Tea, {super().info()}"
    
    
