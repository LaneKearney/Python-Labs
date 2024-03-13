from Car import Car
from CarInventory import CarInventory
from CarInventoryNode import CarInventoryNode

bst = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)

bst.add_car(car1)
bst.add_car(car2)
bst.add_car(car3)
bst.add_car(car4)
bst.add_car(car5)

assert bst.get_best_car("Nissan", "Leaf") == car1
assert bst.get_best_car("Mercedes", "Sprinter") == car3
assert bst.get_best_car("Honda", "Accord") == None

assert bst.get_worst_car("Nissan", "Leaf") == car1
assert bst.get_worst_car("Mercedes", "Sprinter") == car4
assert bst.get_best_car("Honda", "Accord") == None

assert bst.get_total_inventory_price() == 158000
assert bst.inorder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
assert bst.preorder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
assert bst.postorder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""