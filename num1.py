import numpy as np

'''
print("hello Numpy")

myary = np.array([[3,6,9,12],[2,4,6,8]], np.int32) # two dimantention array
print(myary)
#print(myary.shape)                               # array dimentation 
#print(myary.dtype)                               # array element data type
print("prev 11 no line myary[0,1] = ",myary[0,1])
myary[0,1]=99                                      # change element specific position in array   
print("later 11 no line myary[0,1] = ",myary[0,1])
'''
# Array creation : Conversion from other python structure

listn = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(listn)
#print(listn.dtype,listn.shape,listn.size)
listb=np.array({34,65,86})
#print(listb)

zero = np.zeros((2,5)) # array with 0 
#print(zero)
rng = np.arange(11) # array with 0-10
#rng = np.arange(11,62) # array with 11-61
#print(rng)
lspa = np.linspace(1,3,4)
#print(lspa)
emp = np.empty((2,2)) # array with random element
#print(emp)
empl = np.empty_like(lspa)
#print(empl)
ide = np.identity(45) # 45x45 array
#print(ide,ide.shape)
arr1 = np.arange(99)
#print(arr1)
arr1=arr1.reshape(3,33) # change column and row in array
#print(arr1)
arr1 = arr1.ravel()
#print(arr1)
x =[[1,2,3],[4,5,6],[7,8,9]]
for item in x:
    #print(item)
    pass
arr5 = np.array(x)
#print(arr5)
sum0 = arr5.sum(axis=0) # sum of column element
#print(sum0)
sum1 = arr5.sum(axis=1) # sum of row element
#print(sum1)
b = arr5.T # it compliment of an array
#print(b)
km = arr5.flat
#for item in km:
    #print(item)
#print("dimention of array:",arr5.ndim,"number of element in array : ",arr5.size,"toltel byte in array: ",arr5.nbytes)
one = np.array([1,2,34,567,8])
#print("max element in array:",one.argmax(),"min element in array:",one.argmin()) # it find max and min element index in given array
#print(one.argsort()) # it give a index of array with sorting element(index)
#print(arr5)
#print("max and min element index in 2d array:",arr5.argmax() ,arr5.argmin())
#print("sorting 2d array:",arr5.argsort())
arr5 = np.array([[1,2,3],[4,5,6],[7,1,0]])
#print("new array: ",arr5)
#print("max with axis 0: ",arr5.argmax(axis=0),"max with axis 1: ",arr5.argmax(axis=1))
arr4 = arr5.ravel()
#print(arr4)
arr4 = arr4.reshape((9,1))
#print(arr4)
arr6 = np.array([[9,5,3],[4,9,6],[7,6,8]])
print("sum",arr5+arr6,"\nmul",arr5*arr6)
print(np.sqrt(arr6)) # squr root of array element
print("sum all elent in array: ",arr6.sum())
print(np.where(arr6>7)) # it return touple of array
print(np.count_nonzero(arr6))
import sys

py_ar = [0,4,55,2]
np_ar = np.array(py_ar)
print(sys.getsizeof(1) *len(py_ar)) # size of py_ar(python)
print(np_ar.itemsize * np_ar.size) # size of np_ar(numpy)


