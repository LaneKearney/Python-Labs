
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:

    def __init__(self):
        self.head = None


    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def get_number_of_books(self):
        count = 0
        starter = self.head
        while starter != None:
            starter = starter.get_next()
            count +=1
        return count

    def insert_book(self,book):
        newBook = BookCollectionNode(book)
        current = self.head
        previous = None

        while current and book > current.get_data():
            previous = current
            current = current.get_next()
        if previous == None:
            newBook.set_next(self.head)
            self.head = newBook
        else:
            new_next = previous.get_next()
            newBook.set_next(new_next)
            previous.set_next(newBook)


    def get_books_by_author(self,author):
        book_string = ''
        current = self.head

        while current is not None:
            current_book = current.get_data()
            current_author = current_book.get_author()
            if author.upper() == current_author.upper():
                book_string += current_book.get_book_details() + '\n'
            current = current.get_next()
        return book_string

    def get_all_books_in_collection(self):
        book_string = ''
        current = self.head

        while current is not None:
            book_string += current.get_data().get_book_details() + '\n'
            current = current.get_next()
        return book_string

    def remove_author(self, author):
        if self.head == None:
            return
        while self.head is not None and self.head.get_data().get_author().upper() == author.upper():
            self.head = self.head.get_next()
        if self.head is not None:
            current = self.head
            while current.get_next() is not None:
                if current.get_next().get_data().get_author().upper() == author.upper():
                    current.next = current.get_next().get_next()
                else:
                    current = current.next


    def recursive_search_title(self,title,bookNode):
        if bookNode == None:
            return False
        if bookNode.get_data().title.upper() == title.upper():
            return True
        return self.recursive_search_title(title, bookNode.get_next())


