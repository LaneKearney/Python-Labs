class Car:
    def __init__(self, make: str, model: str, year: int, price: int):
        self.price = price
        self.year = year
        self.model = model.upper()
        self.make = make.upper()

    def __lt__(self, rhs):
        if self.make.upper() < rhs.make.upper():
            return True
        elif self.make.upper() == rhs.make.upper():
            if self.model.upper() < rhs.model.upper():
                return True
            elif self.model.upper() == rhs.model.upper():
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
        return False

    def __gt__(self, rhs):
        if self.make.upper() > rhs.make.upper():
            return True
        elif self.make.upper() == rhs.make.upper():
            if self.model.upper() > rhs.model.upper():
                return True
            elif self.model.upper() == rhs.model.upper():
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
        return False

    def __eq__(self, rhs):
        if self.make.upper() == rhs.make.upper():
            if self.model.upper() == rhs.model.upper():
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
        return False

    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'
    
#c = Car("Honda", "CRV", 2007, 8000)
#print(c)