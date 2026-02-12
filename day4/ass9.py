import numpy as np
# 1. Structured array: name, age, weight. Sort by age.
dtype1 = [('name', 'U20'), ('age', 'i4'), ('weight', 'f4')]
data1 = np.array([('Alice', 25, 55.5), ('Bob', 20, 70.2), ('Charlie', 30, 65.0)], dtype=dtype1)
sorted_data = np.sort(data1, order='age')

# 2. Structured array: x, y. Euclidean distance.
dtype2 = [('x', 'i4'), ('y', 'i4')]
points = np.array([(0, 0), (3, 4), (1, 1)], dtype=dtype2)
coords = np.array([list(p) for p in points])
# Distance matrix
diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))