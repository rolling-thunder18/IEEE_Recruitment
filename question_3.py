import numpy as np

matrix=np.random.randint(1,10,size=(5,5))

print("5x5 Matrix:", matrix)

#for maximum
print("maximum: ", matrix.max())
#for minimum
print("minimum: ", matrix.min())
#for mean
print("mean: ", matrix.mean())
#for normalized matrix
normalized_matrix=(matrix-matrix.min())/(matrix.max()-matrix.min())
print("normalized matrix: ", normalized_matrix)
#for flattened and sorted array
flatten=normalized_matrix.flatten()
sorted_array=np.sort(flatten)
print("flattened and sorted array: ", sorted_array)