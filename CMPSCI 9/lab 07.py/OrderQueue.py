from Salad import Salad
from CustomSalad import CustomSalad
from SpecialtySalad import SpecialtySalad
from SaladOrder import SaladOrder

class OrderQueue:

    def __init__(self):
        self.MinHeap = [0]
        self.currentsize = 0
    
    def minChild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.MinHeap[i * 2].get_time() < self.MinHeap[i * 2 + 1].get_time():
                return i * 2
            else:
                return i * 2 + 1


    def perc_up(self, i):
        while i // 2 > 0:
            if self.MinHeap[i].get_time() < self.MinHeap[i // 2].get_time():
                tmp = self.MinHeap[i // 2]
                self.MinHeap[i // 2] = self.MinHeap[i]
                self.MinHeap[i] = tmp
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.currentsize:
            min_child = self.minChild(i)
            if self.MinHeap[i].get_time() > self.MinHeap[min_child].get_time():
                t = self.MinHeap[i]
                self.MinHeap[i] = self.MinHeap[min_child]
                self.MinHeap[min_child] = t
            i = min_child

    def add_order(self, saladOrder):
        self.MinHeap.append(saladOrder)
        self.currentsize += 1
        self.perc_up(self.currentsize)

    def process_next_order(self):
        if self.currentsize == 0:
            return ''
        result = self.MinHeap[1]
        self.MinHeap[1] = self.MinHeap[self.currentsize]
        self.currentsize = self.currentsize-1
        self.MinHeap.pop()
        self.perc_down(1)
        return result.info()



    

