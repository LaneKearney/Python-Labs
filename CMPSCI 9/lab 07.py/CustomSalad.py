from Salad import Salad

class CustomSalad(Salad):
    def __init__(self, size):
        self.topping = []
        super().__init__(size)
        if size == 'S':
            self.price=8.75
        if size == 'M':
            self.price=10.75
        if size == 'L':
            self.price=12.75
    def add_topping(self, topping:str):
        self.topping.append(topping)
        if self.size =='S':
            self.price += 1.75
        if self.size =='M':
            self.price +=2.50
        if self.size =='L':
            self.price +=3.00
    def get_salad_details(self):

        topping_str = ''
        for i in self.topping:
            topping_str += '\t+ ' + i + '\n'
        return f'CUSTOM SALAD\nSize: {self.size}\nToppings:\n{topping_str}Price: ${self.price:.2f}\n'

