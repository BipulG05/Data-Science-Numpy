#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-6 ******** Date :- 29/12/2020
import numpy as np

ex=np.arange(1,101).reshape(10,10)
print(ex)
print("first element of a array",ex[0,0])
print('first row: ',ex[0])
print(ex[:,0])
print(ex[:,0:1].ndim)
print(ex[1:4,1:4])
print(ex[:,1:3])
print(ex[:])
print(ex[::])
print(ex[:,:])
print(ex.itemsize)
print(ex.dtype)
