import math
import logging
import vector

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Matrix:
    
    def __init__(self, elements, shape):
        self._dimensions = shape
        self._elements = self.create(elements, shape)
    
    def create(self, elements, shape):
        m, n = shape
        matrix = []
        _ = 0
        for row in range(m):
            matrix.append(elements[_:(_+n)])
            _ += n
        return matrix

    
    
def tryouts():
    elements = [1, 2, 3, 4, 5, 6, 7, 8]
    shape = [1, 8]
    a = Matrix(elements,shape)
    print(a._elements)

tryouts()