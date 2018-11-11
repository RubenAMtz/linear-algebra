from vector import Vector
from matrix import Matrix

def tryouts():
    a = Vector([1, 0, 0])
    b = Vector([2, 1, 3])
    d = Vector([6, -9.9999])
    # print(Vector.angle(a,b))
    # print(a)
    # print(Vector.polar_2d(b))
    # print(Vector.polar_2d(d))
    # print(a.calc_versors()[0])
    # print(a.calc_versors()[1])
    # unit_a = a.calc_unit_vector()
    print(a.magnitude)
    #print(unit_a)
    #print(unit_a.magnitude)
    print(Vector.collinear(b, a))
    print(Vector.cross_product(a,b))
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shape = (3, 3)
    a = Matrix(elements, shape)
    elements = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    b = Matrix(elements,(3,3))
    elements = [1, -2, -3, -4, -5, -6, -7, -8]
    shape = (2,4)
    c = Matrix(elements, shape)
    #print(a + c)
    #print(a - c)
    print(Matrix.direct_sum(b, a))
    Matrix.matmul(a, b)

if __name__ == "__main__":
    tryouts()