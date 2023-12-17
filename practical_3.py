# from Indian AI Production it's done in juipyter notebook
import numpy as np
# arange()
#formate : np.arange(start,End,steps)
arng=np.arange(1,13)
print(arng)
arng2=np.arange(1,13,2)
print(arng2)
# linespace() 
lins=np.linspace(1,5,4)
print(lins)
# reshape()
#formate : array.reshape(row,column) 2D array (row*column=total elements/size)
print(arng.reshape(3,4))
# formate : array.reshape(3D,2D,1D) 3D array (3D*2D*1D=total elements/size)
print("3D",arng.reshape(2,3,2))
nps=np.arange(14,26).reshape(2,6)
print(nps)
# ravel() Multi-dymention array convert into 1D array
arry_2d=np.array([[1,1,1,1],[1,1,1,1]])
print("ravel 2D -> 1D",arry_2d.ravel())
ary3d=arng.reshape(2,3,2)
print("ravel 3D -> 1D",ary3d.ravel())
# flatten()
# formate : array.reshape(order=C/F/A/K)
print("flatten",ary3d.flatten())
# transpose() row to column and column to row
ar2D=arng.reshape(2,6)        # create 1D -> 2D array
print(ar2D)
print(ar2D.transpose())
print(ar2D.T)

#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-4 ******** Date :- 26/12/2020