#to perform linear algebra in single program
import numpy as np
a=np.array(input("enter a matrix:"));
b=np.array(input("enetr a matrix:"));
#matrix addtion
print a+b;
#matrix subtraction
print a-b;
f=np.linalg.matrix_rank(a);
#rank of a matrix
print f;
g=np.trace(a);
#trace of a matrix
print g;
h=np.linalg.inv(a);
#inverse of a matrix
print h
k=np.linalg.eigh(a);
#eigen values of a matrix
print k;
o=np.matmul(a,b);
#matrix multiplication
print o;
l=input("enter a vector:");
p=input("enter a vector:");
b=np.vdot(l,p);
#dot product of two vectors
print b;





