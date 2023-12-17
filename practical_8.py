#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-9 ******** Date :- 06/01/2021
import numpy as np
import random

ar1=np.random.random(1) # random data generate
print(ar1)
ar2=np.random.random((3,3)) # random 2D array generate
print(ar2)
ar1D=np.random.randint(1,4) # random 1D int no array generate
print(ar1D)
ar2D=np.random.randint(1,4,(4,4)) # random 2D int no array generate
print(ar2D)
ar3D=np.random.randint(1,4,(2,4,4)) # random 3D int no array generate
print("print",ar3D)
np.random.seed(10)
ar23D=np.random.randint(1,4,(2,4,4)) # random 3D int no array generate
print("print2",ar23D)

#  ******* PYTHON PANDS TUTORIAL IN HINDI PART-2 ******** Date :- 06/01/2021