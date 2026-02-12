import numpy as np
# 1. Determinant, Inverse, Eigenvalues
matrix = np.random.randint(1, 10, (3, 3))
det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
eig_vals, eig_vecs = np.linalg.eig(matrix)

# 2. Matrix Multiplication
m1 = np.random.randint(1, 10, (2, 3))
m2 = np.random.randint(1, 10, (3, 2))
prod = np.dot(m1, m2)