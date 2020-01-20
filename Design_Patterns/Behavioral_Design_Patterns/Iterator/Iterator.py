import sys
import os.path
from abc import ABC, abstractmethod
sys.path.append(os.path.join(os.path.dirname(__file__), '../Visitor/'))
from Elements import Element, ProductTypeEnum
import Aggregate

class Iterator(ABC):
    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def first(self):
        pass
    
    @abstractmethod    
    def next(self):
        pass

    @abstractmethod
    def isFinal(self):
        pass

    @abstractmethod
    def add(self, elm):
        pass



class ConcreteIterator(Iterator):

    def __init__(self, aggregate, prodType):
        self.aggregate = aggregate
        self.prodType = prodType
        self.pointer = 0
        self.collection = []

    def current(self):
        if (self.pointer >= len(self.collection)):
                raise Exception("IndexOutOfRangeException:pointer")
        else:
            elm = self.collection[self.pointer]
            while (not elm.productType==self.prodType):
                self.pointer = self.pointer + 1
                if (self.pointer >= len(self.collection)):
                    return None
                else:
                    elm = self.collection[self.pointer]

            return self.collection[self.pointer]

    def first(self):
        self.pointer = 0
        return self.current()
    
    def next(self):
        self.pointer = self.pointer + 1
        return self.current()
        
    def isFinal(self):
        if (self.pointer >= (len(self.collection) - 1)):
            return True
        else:
            return False

    def add(self, elm):
        self.collection.append(elm)
