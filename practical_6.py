#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-7 ******** Date :- 29/12/2020
import numpy as np

arr1=np.arange(1,17).reshape(4,4)
arr2=np.arange(17,33).reshape(4,4)
print(arr1,arr2)
list1=[2,3,4,5]
list2=[6,7,8,9]
print(list1+list2)
print(arr1+arr2)
print(np.concatenate((arr1,arr2)))
print(np.concatenate((arr1,arr2),axis=1))
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))
print(np.hstack((arr1,arr2,arr1)))
print(np.split(arr1,2))
print(type(np.split(arr1,2)))
list1=np.split(arr1,2)
print(list1[0])
print(type(list1))
print(np.split(arr1,2,axis=1))
arr1d=np.array([2,5,7,9,3,6])
print(np.split(arr1d,[1,3]))