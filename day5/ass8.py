import pandas as pd
import numpy as np
# 1. Pivot table
df16 = pd.DataFrame({
    'Date': np.random.choice(pd.date_range('2021-01-01', periods=5), 20),
    'Category': np.random.choice(['A', 'B', 'C'], 20),
    'Value': np.random.randint(1, 100, 20)
})

pivot1 = pd.pivot_table(df16, values='Value',
                        index='Date', columns='Category',
                        aggfunc='sum')
print(pivot1)

# 2. Revenue pivot
df17 = pd.DataFrame({
    'Year': np.random.choice([2020, 2021, 2022], 20),
    'Quarter': np.random.choice(['Q1', 'Q2', 'Q3', 'Q4'], 20),
    'Revenue': np.random.randint(1000, 10000, 20)
})

pivot2 = pd.pivot_table(df17, values='Revenue',
                        index='Year', columns='Quarter',
                        aggfunc='mean')
print(pivot2)
