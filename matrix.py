import math
import logging
import vector

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class Matrix:
    
    def __init__(self, elements, shape):
        if type(shape) is not tuple:
            raise TypeError("Shape must be a tuple")
        if type(elements) is not list:
            raise TypeError("Elements must be a list")
        
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

    def __add__(self, other):
        if (self._dimensions != other._dimensions):
            raise ValueError("Dimension of matrices don't match")
        added_matrix = []
        for i, row in enumerate(self._elements):
            for j, column in enumerate(row):
                added_matrix.append(self._elements[i][j] + other._elements[i][j])
        return Matrix(added_matrix, self._dimensions)

    @staticmethod
    def direct_sum(self, other):
        """
        The direct sum of matrices is a special type of block matrix, 
        in particular the direct sum of square matrices is a block diagonal matrix.
        """
        elements = []
        zeros_other_h = [0] * other.dim[1]
        zeros_self_h = [0] * self.dim[1]                    
        
        for row in range(self._rows):
            elements += self.row(row) + zeros_other_h
            
        for row in range(other._rows):
            elements += zeros_self_h + other.row(row)
        
        shape = (self.dim[0] + other.dim[0], self.dim[1] + other.dim[1])
        return Matrix(elements, shape=shape)             
                                            
    def __sub__(self, other):
        if (self._dimensions != other._dimensions):
            raise ValueError("Dimension of matrices don't match")
        added_matrix = []
        for i, row in enumerate(self._elements):
            for j, column in enumerate(row):
                added_matrix.append(self._elements[i][j] - other._elements[i][j])
        return Matrix(added_matrix, self._dimensions)

    def gaussian_elimination(self):
        """
        This function applies gaussian elimination and pivoting to return a Upper triangular-shapped matrix
        """
        rows = self._rows
        columns = self._columns

        #rank(self) = A in row echelon form, it is the number of non-zero rows from the A in ref
        """
        rows = size(A,1);
        columns = size(A,2);

        if rank(A) < min(rows,columns)
            flag = -1;
            U = [];
            y = [];
            return
        end
        flag = 1;

        if rows ~= columns
            return
        end

        for j=1:(columns-1)
            for i=(j+1):rows
                P= zeros(rows);
                if A(j,j) < tol
                    greatest = max(A(:,j));
                    index = max(find(A(:,j)==greatest));
                    P(j,index) = 1; %elemnt to be switched down
                    P(index,j) = 1; %element to be swtiched up
                    for z=1:rows
                        if 0 == max(P(z,:))
                            P(z,z) = 1; 
                        end
                    end
                    A = P*A;
                end
                L= eye(rows);
                L(i,j) = -A(i,j)/A(j,j);
                A = L*A;
                b = L*b;
            end
        end
        U = A;
        y = b;
        """
    @staticmethod
    def matmul(a, b):
        """
        Returns matrix multiplication
        """
        # keep testing for this condition:
        if a._columns is not b._rows:
            #(m x n) (p x q)
            raise ValueError("Matrix dimensions must match")
        elements = []
        for i in range(a._rows):
            row_a = vector.Vector(a.row(i))
            for j in range(b._columns):
                col_b = vector.Vector(b.col(j))
                elements.append(vector.Vector.dot(row_a, col_b))

        shape = (a._rows, b._columns)
        return Matrix(elements, shape=shape)
        
    def row_echelon_form(self):
        """
        This method applies the Gauss-Jordan algorithm to get a matrix in its row echelon form
        """
        rows = self._rows
        columns = self._columns
        for i in range(rows):
            for j in range(columns):
                pass


    @staticmethod
    def permutation_matrix(matrix, indices):
        result = []
        for element in indices:
            zeros = [0] * matrix._columns
            zeros[element] = 1
            result += zeros
        return Matrix(result, shape=matrix.dim)

    @staticmethod
    def permutation_matrix_2(matrix, from_=0, to_=1):
        result = []
        for row in range(matrix._rows):
            zeros = [0] * matrix._columns
            if row == from_:
                zeros[to_] = 1
            elif row == to_:
                zeros[from_] = 1
            else:
                zeros[row] = 1                                    
            result += zeros
        return Matrix(result, shape=matrix.dim)

    def __str__(self):
        matrix_form = ""
        for row in range(self._rows):
            matrix_form += str(self.row(row)) + "\n"
        matrix_form += ""
        return matrix_form
