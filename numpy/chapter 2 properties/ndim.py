import numpy as np 

arr1d = np.array([1,2,3,4,5])

arr2d = np.array([[1,2,3],
                 [1,24,45]])

arr3d = np.array([[[1,2], [2,3], [3,4], [4,5]]])


print(arr1d.ndim)
print(arr2d.ndim)
print(arr3d.ndim)