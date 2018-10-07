import math

class Vector:
  # Constructor
  def __init__(self, components, set_unit_vectors = True):
    self._components = components
    self._magnitude = self.calc_magnitude(components)
    self._dim = self.calc_dim()
    if set_unit_vectors:
      self._unit_vectors = self.calc_unit_vectors()
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
    return Vector(result)

  def __sub__(self, vector): # = -(a,b)
    """
    Substracting vectors, creates a vector with a new magnitud and direction
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
    """
    return len(self.components)

  def calc_magnitude(components):
    """
    Calculates the distance or magnitude of the vector(number of elements)
    """
    magnitude = sum([x**2 for x in components])
    magnitude = math.sqrt(magnitude)
    return magnitude

  def valid_dims(self, vector):
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
    if type(other) == int or type(other) == float:
      return Vector([x * other for x in self.components])

v = Vector([1,2])
w = Vector([3,4])
v.dot(w)
Vector.dot(v,w)

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

