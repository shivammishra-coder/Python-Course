import numpy as np
# 1. 6x6 array 1-36, extract 3rd-5th rows and 2nd-4th columns
arr3 = np.arange(1, 37).reshape(6, 6)
sub_arr = arr3[2:5, 1:4]

# 2. 5x5 random, extract border elements
arr4 = np.random.randint(1, 100, (5, 5))
border = np.concatenate([arr4[0, :], arr4[-1, :], arr4[1:-1, 0], arr4[1:-1, -1]])