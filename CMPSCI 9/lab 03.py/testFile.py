import pytest
from lab03 import int_division, get_even_ints, count_vowels, reverse_str, remove_seq

def test_int():
    assert int_division(0,1) == 0
    assert int_division(12,4) == 3
    assert int_division(5, 5) == 1
    assert int_division (200, 19) == 10
    assert int_division(27, 4) == 6

def test_get():
    assert get_even_ints([1, 1, 2, 3, 4]) == [2, 4]
    assert get_even_ints([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert get_even_ints([1, 3, 5, 7, 9, 10]) == [10]
    assert get_even_ints([20, 40, 50, 60, 80]) == [20, 40, 50, 60, 80]
    assert get_even_ints([11,33,55,77,99]) == []

def test_count():
    assert count_vowels("this is a string") == 4
    assert count_vowels("iH mY nAME iS lANE") == 6
    assert count_vowels("77777777i7777777") == 1
    assert count_vowels("") == 0
    assert count_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 5

def test_reverse():
    assert reverse_str("i love python") == "nohtyp evol i"
    assert reverse_str("123456789") == "987654321"
    assert reverse_str("") == ""
    assert reverse_str("GooDnighT") == "ThginDooG"
    assert reverse_str("123Hello321") == "123olleH321"

def test_remove():
    assert remove_seq("Lolololol", "lol") == "Loo"
    assert remove_seq("hi", "hihi") == "hi"
    assert remove_seq("123456789", "9") == "12345678"
    assert remove_seq("cmpscicmpscicmpsci", "cmpsci") == ""
    assert remove_seq("CmpscicmpsciCmpsci", "Cmpsci") == "cmpsci"