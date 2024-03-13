class Book:
    def __init__(self,title: str = '', author: str = '', year: int = None):
        self.title = title
        self.author = author
        self.year = year
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_book_details(self):
        return('Title: {}, Author: {}, Year: {}').format(self.title,self.author,self.year)

    def __gt__(self,other):
        if self.author.upper() == other.author.upper():
            if self.year == other.year:
                if self.title.upper() == other.title.upper():
                    return False

                else:
                    return self.title.upper() > other.title.upper()
            else:
                return self.year > other.year
        else:
            return self.author.upper() > other.author.upper()

