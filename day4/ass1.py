import numpy as np

# 1. 5x5 array, random 1-20, 3rd column = 1
arr1 = np.random.randint(1, 21, (5, 5))
arr1[:, 2] = 1

# 2. 4x4 array 1-16, diagonal = 0
arr2 = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(arr2, 0)

# printing arr1 and arr2 
print(arr1,arr2)