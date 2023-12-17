# from Indian AI Production it's done in juipyter notebook 
import numpy as np
arry_2d=np.array([[1,1,1,1],[1,1,1,1]])
print(arry_2d)
arr1=np.ones(5)
print(arr1)
print(arr1.dtype)
arr2=np.ones((5,4))
print(arr2)
arr3=np.ones((5,4),dtype=int)
print(arr3)
arr0=np.zeros((5,4))
print(arr0)
arr0=np.zeros((5,4),dtype=bool)
print(arr0)
arr0=np.zeros((5,4),dtype=str)
print(arr0)
em_str=""
en_str=" "
print(bool(em_str),bool(en_str))
em_empity=np.empty((3,3)) # random number
print(em_empity)