from Salad import Salad
from CustomSalad import CustomSalad
from SpecialtySalad import SpecialtySalad
from SaladOrder import SaladOrder
from OrderQueue import OrderQueue

def test_custom_salad():
    cs1 = CustomSalad("L")
    cs1.add_topping("chicken")
    cs1.add_topping("cucumbers")

    assert cs1.get_salad_details() == \
    'CUSTOM SALAD\nSize: L\nToppings:\n\t+ chicken\n\t+ cucumbers\nPrice: $18.75\n'
def test_salad_order():
    cs1 = CustomSalad("S")
    cs1.add_topping("chicken")
    cs1.add_topping("cucumber")
    ss1 = SpecialtySalad("S", "Cobb")
    order = SaladOrder(123000) 
    order.add_salad(cs1)
    order.add_salad(ss1)

    assert order.info() == \
    """\
    ***
    Order Time: 123000
    CUSTOM SALAD
    Size: S
    Toppings:
    \t+ chicken
    \t+ cucumber
    Price: $12.25

    ----
    SPECIALTY SALAD
    Size: S
    Name: Cobb
    Price: $12.50

    ----
    TOTAL ORDER PRICE: $24.75
    ***
    """
def test_specialty_salad():
    ss1 = SpecialtySalad("S", "Cobb")
    assert ss1.get_salad_details() == \
    """\
    SPECIALTY SALAD
    Size: S
    Name: Cobb
    Price: $12.50
    """
def test_OrderQueue():
    o1 = SaladOrder(140000)
    o2 = SaladOrder(154000)
    cs1 = CustomSalad('L')
    cs1.add_topping('tomatoes')
    cs1.add_topping('olives')
    ss1 = SpecialtySalad('L', 'Caesar')
    o1.add_salad(cs1)
    o1.add_salad(ss1)
    queue = OrderQueue()
    queue.add_order(o1)
    queue.add_order(o2)
    assert queue.process_next_order() == \
    """\
    ***
    Order Time: 140000
    CUSTOM SALAD
    Size = L
    Toppings:
    \t+ tomatoes
    \t+ olives
    Price: $18.75

    ----
    SPECIALTY SALAD:
    Size: L
    Name: Caesar
    Price: $16.50

    ----
    TOTAL ORDER PRICE: $37.25
    ***
    """
    assert queue.process_next_order() ==\
    """
    ***
    Order Time: 154000
    TOTAL ORDER PRICE: $0.00
    ***
    """