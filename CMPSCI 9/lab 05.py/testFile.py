import pytest
from Book import Book
from BookCollection import BookCollection
from BookCollectionNode import BookCollectionNode

b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
bc.insertBook(b2)
bc.insertBook(b3)
print(bc.get_all_books_in_collection())
bc.remove_author('King, Stephen')
print(bc.get_all_books_in_collection())
bc.remove_author('Cline, Ernest')



b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
bc = BookCollection()
bc.insertBook(b0)
bc.insertBook(b1)
assert bc.recursive_search_title("CUJO", bc.head) == True
assert bc.recursive_search_title("Twilight", bc.head) == False

def test_constructor():
    book = Book("Ready Player One", "Cline, Ernest", 2011)
    node = BookCollectionNode(book)
    assert node.get_data() == book
    assert node.get_next() == None
def test_setters():
    book1 = Book("Ready Player One", "Cline, Ernest", 2011)
    book2 = Book("The Shining", "King, Stephen", 1977)
    node = BookCollectionNode(book1)
    node.set_data(book2)
    assert node.get_data() == book2
def test_insert_book():
    b1 = Book("Ready Player One", "Cline, Ernest", 2011)
    b2 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insert_book(b1)
    assert bc.is_empty() == False
    assert bc.get_number_of_books() == 1
    bc.insert_book(b2)
    assert bc.get_number_of_books() == 2
def test_get_books_by_author():
    b1 = Book("Ready Player One", "Cline, Ernest", 2011)
    b2 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insert_book(b1)
    bc.insert_book(b2)
    assert bc.get_books_by_author("CLINE, ERNEST") == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n"
    assert bc.get_books_by_author("KING, Stephen") == "Title: The Shining, Author: King, Stephen, Year: 1977\n"
def test_recursive_search_title():
    b1 = Book("Ready Player One", "Cline, Ernest", 2011)
    b2 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insert_book(b1)
    bc.insert_book(b2)
    assert bc.recursive_search_title("Ready Player One", bc.head) == True
    assert bc.recursive_search_title("The Shining", bc.head) == True
    assert bc.recursive_search_title("CUJO", bc.head) == False
def test_remove_author():
    b1 = Book("Ready Player One", "Cline, Ernest", 2011)
    b2 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insert_book(b1)
    bc.insert_book(b2)
    bc.remove_author("CLINE, ERNEST")
    assert bc.get_number_of_books() == 1
    assert bc.get_all_books_in_collection() == "Title: The Shining, Author: King, Stephen, Year: 1977\n"
