import numpy as np

arr = np.array([10, 20, 30, 40])

new_arr = np.delete(arr, 1)   # delete index 1
print(new_arr)


arr_2d = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

# delete row at index 1
new_arr = np.delete(arr_2d, 1, axis=0)
print(new_arr)
