from Apartment import Apartment

def merge_sort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left_half = apartmentList[:mid]
        right_half = apartmentList[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                apartmentList[k] = left_half[i]
                i += 1
            else:
                apartmentList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            apartmentList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            apartmentList[k] = right_half[j]
            j += 1
            k += 1

def ensure_sorted_ascending(apartmentList):
    for index in range(len(apartmentList)):
        if apartmentList[index] > apartmentList[index + 1]:
            return False
        else:
            return True


def get_best_apartment(apartmentList):
    merge_sort(apartmentList)
    return apartmentList[0].get_apartment_details()


def get_worst_apartment(apartmentList):
    merge_sort(apartmentList)
    return apartmentList[-1].get_apartment_details()


def get_affordable_apartments(apartmentList, budget):
    merge_sort(apartmentList)
    apartment_string = ''
    for apartment in apartmentList:
        if apartment.get_rent() <= budget:
            apartment_string += apartment.get_apartment_details() + '\n'
    return apartment_string[:-1]