import pandas as pd
import numpy as np
# 1. Monthly mean
dates = pd.date_range('2021-01-01', periods=100)
df13 = pd.DataFrame(np.random.randint(1, 100, size=(100, 1)),
                    index=dates, columns=['Value'])

print(df13.resample('M').mean())

# 2. Rolling mean
dates_full = pd.date_range('2021-01-01', '2021-12-31')
df14 = pd.DataFrame(np.random.randint(1, 100, size=(len(dates_full), 1)),
                    index=dates_full, columns=['Value'])

df14['RollingMean'] = df14['Value'].rolling(window=7).mean()
print(df14.head(10))
