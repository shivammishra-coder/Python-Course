import numpy as np

# 1. Element-wise operations
a = np.random.randint(1, 10, (3, 4))
b = np.random.randint(1, 10, (3, 4))
add = a + b
sub = a - b
mul = a * b
div = a / b

# 2. Row-wise and column-wise sum
arr5 = np.arange(1, 17).reshape(4, 4)
row_sum = arr5.sum(axis=1)
col_sum = arr5.sum(axis=0)