import numpy as np

#VSTACK
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))
print(result)

#HSTACK
a = np.array([[1],
              [2],
              [3]])

b = np.array([[4],
              [5],
              [6]])

result = np.hstack((a, b))
print(result)


#STACK
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.stack((a, b))
print(result)


#DSTACK 
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

result = np.dstack((a, b))
print(result)
print(result.shape)


