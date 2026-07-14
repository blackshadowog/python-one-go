import numpy as np 

arr = np.array([1,2,3,np.nan , 5 , np.nan , 6])

print(np.isnan(arr))

print(np.nan == np.nan)