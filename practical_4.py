#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-5 ******** Date :- 29/12/2020

import numpy as np

arr1 = np.arange(1,10).reshape(3,3) 
arr2 = np.arange(1,10).reshape(3,3)
print(arr1,arr2)
print(arr1+arr2)
print(np.add(arr1,arr2))
print(arr1-arr2)
print(np.subtract(arr1,arr2))
print(arr1*arr2)
print(np.multiply(arr1,arr2))
print(arr1@arr2)
print(np.dot(arr1,arr2))
print(arr1,"max :",arr1.max(),"index max value:",arr1.argmax())
print("max in x axis/column :",arr1.max(axis=0),"max in y axis/row :",arr1.max(axis=1))
print(arr1,"min :",arr1.min(),"index min value:",arr1.argmin())
print("min in x axis/column :",arr1.min(axis=0),"min in y axis/row :",arr1.min(axis=1))
print(np.sum(arr1)) # matrix all element sum
print("column element: ",np.sum(arr1,axis=0),"row element: ",np.sum(arr1,axis=1))
print("sum of matrix all element/total element :-",np.mean(arr1))# arr1 : 45/9
print(np.sqrt(arr1))
print(np.std(arr1)) # standard deviation 
print(np.exp(arr1)) # exponent of array element
print(np.log(arr1)) # log of array element
print(np.log10(arr1)) # log base 10 of array element


