import pandas as pd
import numpy as np
# 1. Group by Category
df7 = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], 10),
    'Value': np.random.randint(1, 100, 10)
})

grouped = df7.groupby('Category')['Value'].agg(['sum', 'mean'])
print(grouped)

# 2. Product sales
df8 = pd.DataFrame({
    'Product': np.random.choice(['P1', 'P2', 'P3'], 10),
    'Category': np.random.choice(['A', 'B', 'C'], 10),
    'Sales': np.random.randint(100, 1000, 10)
})

print(df8.groupby('Category')['Sales'].sum())
