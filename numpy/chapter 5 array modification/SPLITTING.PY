import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

result = np.split(arr, 3)
print(result)


arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

result = np.hsplit(arr_2d, 2)
result2 = np.vsplit(arr_2d, 2)

print(result)
print(result2)


