import pandas as pd

# 1. Merge
df9 = pd.DataFrame({'ID': [1, 2, 3], 'A': [10, 20, 30]})
df10 = pd.DataFrame({'ID': [1, 2, 3], 'B': [40, 50, 60]})

merged = pd.merge(df9, df10, on='ID')
print(merged)

# 2. Concatenate
df11 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df12 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

print(pd.concat([df11, df12], axis=0))  # rows
print(pd.concat([df11, df12], axis=1))  # columns
