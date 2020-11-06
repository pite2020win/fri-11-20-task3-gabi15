#Matrix. 


#Write a class that can represent any 2𝑥2 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

class Matrix:
  def __init__(self,val11 =0, val12=0, val21=0, val22=0):
    self.tab = [[val11,val12],[val21,val22]]
    self.size =2
  
  def __add__(self,other):
    new_matrix = Matrix()
    for i in range(self.size):
      for j in range(self.size):
        new_matrix.tab[i][j] = self.tab[i][j]+other.tab[i][j]
    return new_matrix


if __name__ == "__main__":
  m1 = Matrix(1,2,1,2)
  m2 = Matrix(1,1,1,1)
  print((m1+m2).tab)

