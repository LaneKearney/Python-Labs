import pytest
from lab06 import *

a0 = Apartment(1110, 215, "bad")
a1 = Apartment(999, 215, "average")
a2 = Apartment(950, 215, "excellent")
a3 = Apartment(900, 195, "excellent")
a4 = Apartment(800, 200, "average")
a5 = Apartment(750, 250, "average")
apartmentList = [a0, a1, a2, a3, a4, a5]
merge_sort(apartmentList)
assert apartmentList[0].get_apartment_details() == '(Apartment) Rent: $750, Distance From UCSB: 250m, Condition: average'
assert apartmentList[1].get_apartment_details() == '(Apartment) Rent: $800, Distance From UCSB: 200m, Condition: average'
assert apartmentList[2].get_apartment_details() == '(Apartment) Rent: $900, Distance From UCSB: 195m, Condition: excellent'
assert apartmentList[3].get_apartment_details() == '(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent'
assert apartmentList[4].get_apartment_details() == '(Apartment) Rent: $999, Distance From UCSB: 215m, Condition: average'
assert apartmentList[5].get_apartment_details() == '(Apartment) Rent: $1110, Distance From UCSB: 215m, Condition: bad'

def test_ensure_sorted_ascending():
    a0 = Apartment(1100, 300, "average")
    a1 = Apartment(950, 250, "average")
    a2 = Apartment(950, 220, "excellent")
    a3 = Apartment(900, 195, "bad")
    a4 = Apartment(800, 200, "average")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensure_sorted_ascending(apartmentList) == False
    merge_sort(apartmentList)
    assert ensure_sorted_ascending(apartmentList) == True

def test__best_apartment():
    a0 = Apartment(1100, 300, "average")
    a1 = Apartment(950, 250, "average")
    a2 = Apartment(950, 220, "excellent")
    a3 = Apartment(900, 195, "bad")
    a4 = Apartment(800, 200, "average")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert get_best_apartment(apartmentList) == '(Apartment) Rent: $800, Distance From UCSB: 200m, Condition: average'

def test_worst_apartment():
    a0 = Apartment(1100, 300, "average")
    a1 = Apartment(950, 250, "average")
    a2 = Apartment(950, 220, "excellent")
    a3 = Apartment(900, 195, "bad")
    a4 = Apartment(800, 200, "average")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert get_worst_apartment(apartmentList) == '(Apartment) Rent: $1100, Distance From UCSB: 300m, Condition: average'


def test_affordable_apartment():
    a0 = Apartment(1110, 215, "bad")
    a1 = Apartment(999, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(900, 195, "excellent")
    a4 = Apartment(800, 200, "average")
    a5 = Apartment(750, 250, "average")
    apartmentList = [a0, a1, a2, a3, a4, a5]

assert get_affordable_apartments(apartmentList, 900) == \
        '(Apartment) Rent: $750, Distance From UCSB: 250m, Condition: average\n'\
        '(Apartment) Rent: $800, Distance From UCSB: 200m, Condition: average\n'\
        '(Apartment) Rent: $900, Distance From UCSB: 195m, Condition: excellent'





