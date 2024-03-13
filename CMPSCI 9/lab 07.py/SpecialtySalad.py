from Salad import Salad

class SpecialtySalad(Salad):
    def __init__(self, size, name):
        self.name = name
        super().__init__(size)
        if size == 'S':
            self.price = 12.50
        if size == 'M':
            self.price = 14.50
        if size == 'L':
            self.price = 16.50
    def get_salad_details(self):
        return f'SPECIALTY SALAD\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n'


