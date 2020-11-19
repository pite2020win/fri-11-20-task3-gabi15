import math

# A class to create n x n Matrix and to handle math operations
class Matrix:
  def __init__(self,*args):
    if isinstance(args[0],list):
      self.tab = args[0]
      self.size = len(args[0])
    else:
      if(math.sqrt(len(args))%1==0):
        self.size = int (math.sqrt(len(args)))
        self.tab =[]
        for i in range(0,len(args),self.size):
          self.tab.append(list(args[i:i+self.size]))
  
  def __str__(self):
    return str(self.tab)

  
  def __add__(self,other):
    size = self.size
    new_matrix = Matrix([[0 for x in range(size)] for y in range(size)])
    if(isinstance(other,Matrix)):
      for i in range(size):
        for j in range(size):
          new_matrix.tab[i][j] = self.tab[i][j]+other.tab[i][j]
    else:
      for i in range(size):
        for j in range(size):
          new_matrix.tab[i][j] = self.tab[i][j]+other
    return new_matrix

    
  
  def __radd__(self,other):
    return self+other

  def __sub__(self,other):
    if(isinstance(other,Matrix)):
      tt = [[-y for y in x]for x in other.tab]
      return self.__add__(tt)
    else:
      return self.__add__(-other)

  def __rsub__(self,other):
    return self.__sub__(other)*-1
  
  def __mul__(self,other):
    size = self.size
    new_matrix = Matrix([[0 for x in range(size)] for y in range(size)])
    for i in range(size):
      for j in range(size):
        new_matrix.tab[i][j] = self.tab[i][j]*other
    return new_matrix

  def __rmul__(self, other):
    return self.__mul__(other)

  def __truediv__(self,other):
    return self.__mul__(1/other)

  def __matmul__(self,other):
    size = self.size
    new_matrix = Matrix([[0 for x in range(size)] for y in range(size)])
    for i in range(size):
      for j in range(size):
        for k in range(size):
          new_matrix.tab[i][j] += self.tab[i][k] * other.tab[k][j]
    return new_matrix


if __name__ == "__main__":

  # you can create Matrix of any n x n size in two ways
  m1 = Matrix(1,2,1,2)
  m2 = Matrix([[1,1],[1,1]])
  m3 = Matrix(1,2,3,4,5,6,7,8,9)
  m4 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
  print(15*'-'+'Examle operations'+15*'-')
  print('{} + {} = {}\n'.format(m1, m2, m1+m2))
  print('{} + {} = {}\n'.format(m3,6,m3+6))
  print('{} + {} = {}\n'.format(6,m4,6+m4))
  print('{} - {} = {}\n'.format(m1,6,m1-6))
  print('{} - {} = {}\n'.format(6,m1,6-m1))
  print('{} * {} = {}\n'.format(m2,2,m2*2))
  print('{} * {} = {}\n'.format(2,m2,2*m2))
  print('{} / {} = {}\n'.format(m2,2,m2/2))
  print('{} @ {} = {}\n'.format(m1,m2,m2@m2))

  

