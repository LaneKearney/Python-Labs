from Salad import Salad
from CustomSalad import CustomSalad

class SaladOrder:
    def __init__(self, time:int):
        self.time = time
        self.salads = []
    def get_time(self):
        return self.time
    def add_salad(self, salad):
        self.salads.append(salad)
    def info(self):
        total = sum(salad.get_price() for salad in self.salads)
        order_details = f'***\nOrder Time: {self.time}\n'
        
        for salad in self.salads:
            order_details += salad.get_salad_details() + '\n----\n'
        
        order_details += f'TOTAL ORDER PRICE: ${total:.2f}\n***\n'
        return order_details
    

