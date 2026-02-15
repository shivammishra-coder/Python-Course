import pandas as pd
import numpy as np
# 1. Fill NaN with mean
df5 = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)),
                   columns=['A', 'B', 'C'])

df5.iloc[1, 1] = np.nan
df5.iloc[3, 2] = np.nan

df5 = df5.fillna(df5.mean())
print(df5)

# 2. Drop rows with NaN
df6 = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)),
                   columns=['A', 'B', 'C', 'D'])

df6.iloc[2, 1] = np.nan
df6.iloc[4, 3] = np.nan

df6 = df6.dropna()
print(df6)
