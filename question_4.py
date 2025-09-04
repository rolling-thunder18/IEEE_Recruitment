import numpy as np

# 5x5 matrix with random integers from 1 to 10
matrix = np.random.randint(1, 11, (5, 5))
print("Original 5x5 matrix:\n", matrix)
middle= matrix[1:4, 1:4]
print("Middle 3x3 sub-matrix:\n", middle)
first_row= matrix[0, :]
last_column=matrix[:, -1]
print("First row:\n", first_row)
print("Last column:\n", last_column)

dot_product=np.dot(first_row, last_column)
print("Dot product of first row and last column:", dot_product)