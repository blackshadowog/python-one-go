import numpy as np 

arr = np.array([1,2,3,np.nan , 5 , np.nan , 6])

arr2 = np.nan_to_num(arr,nan=67)

print(arr2)