import pandas as pd
import numpy as np

# 1. DataFrame with 4 columns and 6 rows
df1 = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)),
                   columns=['A', 'B', 'C', 'D'])

df1.set_index('A', inplace=True)
print(df1)

# 2. DataFrame with specific index and columns
df2 = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)),
                   index=['X', 'Y', 'Z'],
                   columns=['A', 'B', 'C'])

print(df2)
print("Element at Y, B:", df2.loc['Y', 'B'])
