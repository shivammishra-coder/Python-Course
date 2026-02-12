import numpy as np
# 1. Mean, median, std, var
arr6 = np.random.randint(1, 100, (5, 5))
stats = {
    "mean": np.mean(arr6),
    "median": np.median(arr6),
    "std": np.std(arr6),
    "var": np.var(arr6)
}

# 2. Normalize array (mean=0, std=1)
arr7 = np.arange(1, 10).reshape(3, 3)
normalized = (arr7 - np.mean(arr7)) / np.std(arr7)