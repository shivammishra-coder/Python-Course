import pandas as pd
import numpy as np
# 1. MultiIndex
arrays = [['A', 'A', 'B', 'B'], ['X', 'Y', 'X', 'Y']]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'SubCategory'))

df15 = pd.DataFrame(np.random.randint(1, 100, size=(4, 2)),
                    index=index, columns=['Value1', 'Value2'])

print(df15)
print(df15.loc['A'])
print(df15.loc[('B', 'X')])

# 2. Sum by MultiIndex
print(df15.groupby(level=['Category', 'SubCategory']).sum())

