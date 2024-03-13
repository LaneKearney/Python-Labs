from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add_car(self,car):
        if self.root is None:
            self.root = CarInventoryNode(car)

        else:
            self.add_car_helper(car, self.root)
    
    def add_car_helper(self, car, node):
        if CarInventoryNode(car) == node:
            return node.cars.append(car)
        elif CarInventoryNode(car) > node:
            if node.get_right():
                self.add_car_helper(car, node.get_right())
            else:
                node.set_right(CarInventoryNode(car))
                node.right.set_parent(node)
        else:
            if node.get_left():
                self.add_car_helper(car, node.get_left())
            else:
                node.set_left(CarInventoryNode(car))
                node.left.set_parent(node)
    
    
    def does_car_exist(self, car):
        if self.root is not None:
            result = self._does_car_exist(car, self.root)
            if result is not None:
                if car not in result.cars:
                    return False
                else:
                    return True
            else:
                return False
    
    def _does_car_exist(self, car, node):
        if not node:
            return None
        elif node == CarInventoryNode(car):
            return node
        elif node < CarInventoryNode(car):
            return self._does_car_exist(car, node.get_right())
        else:
            return self._does_car_exist(car, node.get_left())

    def inorder(self):
        return self.in_order(self.root)

    def in_order(self, car):
        c = ''
        if car is not None:
            c = c + self.in_order(car.get_left()) + str(car) + self.in_order(car.get_right())
        return c

    def postorder(self):
        return self.post_order(self.root)
    
    def post_order(self, car):
        b = ''
        if car is not None:
            b = b + self.post_order(car.get_left()) + self.post_order(car.get_right()) + str(car)
        return b
    
    def preorder(self):
        return self.pre_order(self.root)

    def pre_order(self, car):
        a = ''
        if car is not None:
            a = a + str(car) + self.pre_order(car.get_left()) + self.pre_order(car.get_right())
        return a
    
    def get_best_car(self, make, model):
        if self.root:
            result = self.get_(CarInventoryNode(Car(make, model, 1, 1)), self.root)
            if result:
                best_car = result.cars[0]
                for index in result.cars:
                    if index > best_car:
                        best_car = index
                return best_car
            else:
                return None
        else:
            return None
    def get_(self, CarInventoryNode, node):
        if not node:
            return None
        elif CarInventoryNode == node:
            return node
        elif CarInventoryNode < node:
            return self.get_(CarInventoryNode, node.left)
        else:
            return self.get_(CarInventoryNode, node.right)

    def get_worst_car(self, make, model):
        if self.root:
            result = self.get_(CarInventoryNode(Car(make, model, 1, 1)), self.root)
            if result:
                worst_car = result.cars[0]
                for index in result.cars:
                    if index < worst_car:
                        worst_car = index
                return worst_car
            else:
                return None
        else:
            return None
        
    def _get_total_inventory_price(self, node):
        i = 0
        if node is not None:
            for _car in node.cars:
                i = i + _car.price
            i = i + self._get_total_inventory_price(node.get_right()) + self._get_total_inventory_price(node.get_left())
        return i

    def get_total_inventory_price(self):
        return self._get_total_inventory_price(self.root)
    
#bst = CarInventory()

#car1 = Car("Nissan", "Leaf", 2018, 18000)
#car2 = Car("Tesla", "Model3", 2018, 50000)
#car3 = Car("Mercedes", "Sprinter", 2022, 40000)
#car4 = Car("Mercedes", "Sprinter", 2014, 25000)
#car5 = Car("Ford", "Ranger", 2021, 25000)

#bst.add_car(car1)
#bst.add_car(car2)
#bst.add_car(car3)
#bst.add_car(car4)
#bst.add_car(car5)

#assert bst.get_best_car("Nissan", "Leaf") == car1
#assert bst.get_best_car("Mercedes", "Sprinter") == car3
#assert bst.get_best_car("Honda", "Accord") == None
#assert bst.get_worst_car("Nissan", "Leaf") == car1
#assert bst.get_worst_car("Mercedes", "Sprinter") == car4
#assert bst.get_best_car("Honda", "Accord") == None
#assert bst.get_total_inventory_price() == 158000