from Car import Car


class CarInventoryNode:
    def __init__(self, car):
        self.car = car
        self.cars = [car]
        self.model = car.model.upper()
        self.make = car.make.upper()
        self.parent = None
        self.left = None
        self.right = None

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def __str__(self):
        car_1 = ''
        for car in self.cars:
            car_1 = car_1 + (str(car) + '\n')
        return str(car_1)

    def __eq__(self, rhs):
        if self.model == rhs.model:
            if self.make == rhs.make:
                return True
        else:
            return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
        else:
            return False

    def __gt__(self,rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
        else:
            return False

#car1 = Car("Dodge", "dart", 2015, 6000)
#car2 = Car("dodge", "DaRt", 2003, 5000)
#carNode = CarInventoryNode(car1)
#carNode.cars.append(car2)
#print(carNode)