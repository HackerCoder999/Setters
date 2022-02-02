
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def rintarea(self):
        return 0

class rectangle(shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.lenght = 6
        self.breatce = 4

    def rintarea(self):
        return self.lenght * self.breatce

rect1 = Rectangle ()
print(rect1.printarea())
