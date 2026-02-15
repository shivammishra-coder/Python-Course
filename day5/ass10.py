import pandas as pd
# 1. Uppercase
s1 = pd.Series(['apple', 'banana', 'cherry', 'mango', 'grape'])
print(s1.str.upper())

# 2. First three characters
s2 = pd.Series(['python', 'pandas', 'numpy', 'matplotlib', 'seaborn'])
print(s2.str[:3])
