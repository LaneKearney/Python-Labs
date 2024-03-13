class Movie:
    title:str
    genre:str
    year:int

    def __init__(self = None, title = None, genre = None, year = None):
        self.title = title.title() if title else None
        self.genre = genre.upper() if genre else None
        self.year = year


    def setTitle(self, title):
        self.title = title.title()
    
    def setGenre(self, genre):
        self.genre = genre.upper()

    def setYear(self, year):
        self.year = year
    
    def toString(self):
        return f'"{self.title}" ({self.genre}) - {self.year}'

