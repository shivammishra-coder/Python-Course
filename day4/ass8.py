import numpy as np
# 1. Fancy indexing corners
arr12 = np.random.randint(1, 100, (5, 5))
corners = arr12[[0, 0, 4, 4], [0, 4, 0, 4]]

# 2. Boolean indexing: elements > 10 set to 10
arr13 = np.random.randint(1, 20, (4, 4))
arr13[arr13 > 10] = 10