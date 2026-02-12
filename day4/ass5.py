import numpy as np
# 1. Add 1D array (3,) to each row of (3,3)
arr8 = np.random.randint(1, 10, (3, 3))
row_vec = np.array([1, 2, 3])
res1 = arr8 + row_vec

# 2. Subtract 1D array (4,) from each column of (4,4)
arr9 = np.random.randint(1, 10, (4, 4))
col_vec = np.array([1, 2, 3, 4]).reshape(4, 1)
res2 = arr9 - col_vec