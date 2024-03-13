import pytest
from Tea import Tea
from Juice import Juice
from DrinkOrder import DrinkOrder
from Drink import Drink

class TestDrink:
    def test_init(self):
        drink = Drink('medium', 15.5)
        assert drink.size == 'medium'
        assert drink.price == 20.5
    def test_getSize(self):
        drink = Drink('large', 12.95)
        assert drink.getSize() == 'large'
    def test_getPrice(self):
        drink = Drink('small', 19.75)
        assert drink.getPrice() == 19.75
    def test_updateSize(self):
        drink = Drink('large', 20.5)
        drink.updateSize('medium')
        assert drink.getSize() == 'medium'
    def test_updatePrice(self):
        drink = Drink('large', 8.5)
        drink.updatePrice(5.5)
        assert drink.getPrice() == 5.5
    def test_info(self):
        drink = Drink('small', 9.5)
        assert drink.info()== 'small: $9.50'
    
    def test_drinkorder_init(self):
        order = DrinkOrder()
        assert order.drinks ==[]
    def test_add(self):
        order = DrinkOrder()
        tea = Tea('large', 4.0, 'Chai')
        juice = Juice('small', 5.2, ['Orange', 'Lemon'])
        order.add(tea)
        order.add(juice)
        assert order.drinks == [tea, juice]
    def test_total(self):
        tea = Tea('large', 4.0, 'Chai')
        juice = Juice('large', 5.0, ['Apple', 'Cucumber'])
        order = DrinkOrder()
        order.add(tea)
        order.add(juice)
        assert order.total()=="Order Items:\n* Chai Tea, large: $4.00\n* Apple/Cucumber Juice, large: $5.00\nTotal Price: $9.00"    
    
    
