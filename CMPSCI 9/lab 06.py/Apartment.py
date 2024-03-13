class Apartment:


    def __init__(self, rent, meters_from_UCSB, condition):
        self.rent = rent
        self.meters_from_UCSB = meters_from_UCSB
        self.condition = condition

    def get_rent(self):
        return self.rent

    def get_meters_from_UCSB(self):
        return self.meters_from_UCSB

    def get_condition(self):
        return self.condition

    def get_apartment_details(self):
        return ('(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}').format(self.rent, self.meters_from_UCSB, self.condition)

    def __lt__(self, rhs):
        apartment_condition = ['excellent', 'average', 'bad']
        if self.rent < rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.meters_from_UCSB < rhs.meters_from_UCSB:
                return True
            elif self.meters_from_UCSB == rhs.meters_from_UCSB:
                if  apartment_condition.index(self.condition) < apartment_condition.index(rhs.condition):
                    return True
        return False


    def __gt__(self, rhs):
        apartment_condition = ['excellent', 'average', 'bad']
        if self.rent > rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.meters_from_UCSB > rhs.meters_from_UCSB:
                return True
            elif self.meters_from_UCSB == rhs.meters_from_UCSB:
                if apartment_condition.index(self.condition) > apartment_condition.index(rhs.condition):
                    return True
        return False


    def __eq__(self, rhs):
        apartment_condition = ['excellent', 'average', 'bad']
        if self.rent == rhs.rent and self.meters_from_UCSB == rhs.meters_from_UCSB and apartment_condition.index(self.condition) == apartment_condition.index(rhs.condition):
            return True
        else:
            return False