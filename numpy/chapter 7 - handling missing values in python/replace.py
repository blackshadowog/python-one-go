import numpy as np 

arr = np.array([1,2,3,np.inf , 5 , -np.inf , 6])

arr2 = np.nan_to_num(arr , posinf=2000 , neginf=3000)

print(arr2)