import math
import logging
import vector

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Matrix:
    
    def __init__(self, elements, shape):
        self._dimensions = shape
        self._elements = self.create(elements, shape)
        self._rows = shape[0]
        self._columns = shape[1]

    @property
    def elements(self):
        return self._elements
    
    @property
    def dim(self):
        return self._dimensions

    def create(self, elements, shape):
        m, n = shape
        matrix = []
        _ = 0
        for row in range(m):
            matrix.append(elements[_:(_+n)])
            _ += n
        return matrix
    
    def row(self, row):
        """
        Returns a copy of the row specified
        """
        return list(self._elements[row])
        
    def col(self, col):
        """
        Return the elements of the column
        """
        column = []
        for row in range(self._rows):
            column.append(self._elements[row][col])
        return column

    def transpose(self):
        """
        Returns the transpose of the matrix
        """
        elements = []
        for index in range(self._columns):
            elements += self.col(index)

        shape = (self.dim[1], self.dim[0])
        return Matrix(elements, shape)
        
    def __str__(self):
        matrix_form = "["
        for row in range(self._rows):
            matrix_form += str(self.row(row)) + "\n"
        matrix_form += "]"
        return matrix_form
