#  ******* PYTHON NUMPY TUTORIAL IN HINDI PART-8 ******** Date :- 29/12/2020
import numpy as np
import matplotlib.pyplot as plt

print(np.sin(180))
print(np.sin(90))
print(np.cos(180))
print(np.tan(90))
x_sin=np.arange(0,3*np.pi,0.1)
print(x_sin)
y_sin=np.sin(x_sin)
print(y_sin)
plt.plot(x_sin,y_sin)
plt.show()
y_cos=np.cos(x_sin)
plt.plot(x_sin,y_cos)
plt.show()
y_tan=np.tan(x_sin)
plt.plot(x_sin,y_tan)
plt.show()