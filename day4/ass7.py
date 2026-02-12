import numpy as np
# 1. Reshape 1-9: (3,3) -> (1,9) -> (9,1)
arr10 = np.arange(1, 10).reshape(3, 3)
res_1_9 = arr10.reshape(1, 9)
res_9_1 = res_1_9.reshape(9, 1)

# 2. Flatten and reshape back
arr11 = np.random.randint(1, 100, (5, 5))
flat = arr11.flatten()
back = flat.reshape(5, 5)