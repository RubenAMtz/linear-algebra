import math
import logging
logging.basicConfig(level=logging.DEBUG)

class Vector:
  # Constructor
  def __init__(self, components, set_unit_vectors = True, log = True):
    """
    Constructs a Vector object by passing the components of a "vector" in a list

    @param components: A list containing the numeric components\n
    @type components: list\n
    @param set_unit_vectors: A flag to calculate a unit vector object of the Vector\n
    @type set_unit_vectors: bool
    return: A vector
    rtype: Vector
    """
    self._components = components
    self._magnitude = self.calc_magnitude(components)
    self._dim = self.calc_dim()
    if set_unit_vectors:
      self._unit_vectors = self.calc_unit_vectors()
    if log:
      logging.info('Created vector - %s', str(self.components))
      
      
  # Getters
  @property
  def unit_vectors(self):
    return self._unit_vectors
  
  @property #decorator
  def components(self):
    return self._components

  @property #decorator
  def dimensions(self):
    return self._dim

  @property #decorator
  def magnitude(self):
    return self._magnitude

  # Setters
  @components.setter #decorator
  def components(self, components):
    self._components = components
    self._dim = self.calc_dim()
    self._magnitude = self.calc_magnitude(components)
    self._unit_vectors = self.calc_unit_vectors()

  # Instance methods
  def __add__(self, vector): # = +(a,b)
    """
    Adding vectors, creates a vector with a new magnitud and direction
    
    @param vector: a vector\n
    @type vector: Vector\n
    @return: vector + vector\n
    @rtype: Vector
    """
    if not self.valid_dims(vector):
      raise ValueError("Vector Dimensions don't Match.")
    a = self.components
    b = vector.components
    result = []
    # For to access each element of the vectors
    for x in range(self.dimensions):
      add = a[x] + b[x]
      result.append(add)
    results = Vector(result, log=False)
    logging.info('Addition of vectors - %s + %s = %s', str(self.components), str(vector.components), str(results.components))
    return results

  def __sub__(self, vector): # = -(a,b)
    """
    Substracting vectors, creates a vector with a new magnitud and direction.
    
    @param vector: a vector\n
    @type vector: Vector\n
    @return: vector + vector\n
    @rtype: Vector
    """
    if not self.valid_dims(vector):
      raise ValueError("Vector Dimensions don't Match.")
    a = self.components
    b = vector.components
    result = []
    # For to access each element of the vectors
    for x in range(self.dimensions):
      sub = a[x] - b[x]
      result.append(sub)
    return Vector(result)

  def calc_dim(self):
    """
    Calculates the number of dimensions of the vector (number of elements)
    
    @return: dimensions of the vector\n
    @rtype: int
    """
    return len(self.components)

  def calc_magnitude(self, components):
    """
    Calculates the distance or magnitude of the vector(number of elements)
    
    @param components: components of a vector\n
    @type components: list\n
    @return: magnitude of vector\n
    @rtype: float
    """
    magnitude = sum([x ** 2 for x in components])
    magnitude = math.sqrt(magnitude)
    return magnitude

  def valid_dims(self, vector):
    """
    Compares the dimensions between Vector objects
    
    @param vector: A Vector object (to be compared with)
    @type: Vector object
    return: TRUE/FALSE
    rtype: Bool        
    """
    return self.dimensions == vector.dimensions

  def __mul__(self, other):
    """
    Multiplies a vector with a scalar
    This multiply a vector with a numeric value and returns a vector with a different magnitud. 
    The direction will be shifted if the scalar brings a negative sign.        
    
    @param other: a scalar\n
    @type other: float or int\n
    @return: Vector * scalar\n
    @rtype: Vector
    """
    if type(other) == int or type(other) == float:
      return Vector([x * other for x in self.components])

  #rmul to prevent for order of factors in parameters
  def __rmul__(self, other):
    """
    Same as method __mul__(self,other)
    """    
    if type(other) == int or type(other) == float:
      return Vector([x * other for x in self.components])

  def calc_unit_vectors(self):
    """
    Calculates the unit vectors of the vector
    
    return: A list of Vector type objects
    rtype: List (of Vector objects)
    """
    result = []
    for i in range(self.dimensions):
      unit_vector = [0] * self.dimensions
      unit_vector[i] = 1
      result.append(Vector(unit_vector, set_unit_vectors=False, log=False))
    return result

  # Static methods
  @staticmethod
  def dot(a, b):
    """ 
    Calculates the dot product between two Vector type objects a & b
    @param a: A Vector object
    @param b: A Vector object
    return: A scalar
    rtype: Float    
    """
    return sum([x * y for x, y in zip(a.components, b.components)])

  @staticmethod
  def collinear(a, b):
    """
    Calculates vectors that are either parallel to each other or are in the same line. It also 
    detects if direction is either opposite or the same (given that they are collinear)
    @param a: Vector A
    type: Vector
    @param b: Vector B
    type: Vector
    return: true if vectors are collinear
    rtype: bool
    """
    result = Vector.dot(a, b) / (a.magnitude * b.magnitude)
    if result == -1:
      print("Collinear with opposite directions")
    return 1.0 == abs(result)

v = Vector([1, 2, 3])
w = Vector([1, 1, 1])
v + w
# Cross product, Gradients, Igualdades
# v = Vector([1,2,3])
# w = Vector([-1,-2,-3])
# print(Vector.collinear(v, w))

#Vector.collinear(v,w) # True/False
#print(Vector.dot(w, v))
# v = Vector([1,2])
# w = Vector([3,4])
# Vector.dot(v,w)

# v = Vector([4,5])
# w = Vector([1,1])
# # Setter
# v.components = [1,2,3] # old way = v.setcomponents(..)
# print(v.components)
# print(v.unit_vectors)
# unit_vectors = v.unit_vectors
# print(unit_vectors[0].components)
# print(unit_vectors[1].dimensions)
# print(unit_vectors[2].magnitude)
# print((unit_vectors[0]-unit_vectors[1]).components)

