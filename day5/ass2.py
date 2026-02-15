import pandas as pd
import numpy as np
# 1. Add product column
df3 = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)),
                   columns=['A', 'B', 'C'])

df3['Product'] = df3['A'] * df3['B']
print(df3)

# 2. Row-wise and column-wise sum
df4 = pd.DataFrame(np.random.randint(1, 10, size=(4, 3)),
                   columns=['A', 'B', 'C'])

print("Column-wise sum:\n", df4.sum())
print("Row-wise sum:\n", df4.sum(axis=1))
