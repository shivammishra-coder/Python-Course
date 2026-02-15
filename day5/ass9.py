import pandas as pd
import numpy as np
# 1. Double values
df18 = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)),
                    columns=['A', 'B', 'C'])

df18 = df18.apply(lambda x: x * 2)
print(df18)

# 2. Lambda sum column
df19 = pd.DataFrame(np.random.randint(1, 10, size=(6, 3)),
                    columns=['A', 'B', 'C'])

df19['Sum'] = df19.apply(lambda row: row.sum(), axis=1)
print(df19)
