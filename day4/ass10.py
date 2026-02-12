import numpy as np
# 1. Mask > 10, sum unmasked
data2 = np.random.randint(1, 20, (4, 4))
masked_arr1 = np.ma.masked_greater(data2, 10)
sum_unmasked = masked_arr1.sum()

# 2. Mask diagonal, replace with mean of others
data3 = np.random.randint(1, 20, (3, 3)).astype(float)
mask = np.eye(3, dtype=bool)
masked_arr2 = np.ma.array(data3, mask=mask)
mean_val = masked_arr2.mean()
filled_arr = masked_arr2.filled(mean_val)