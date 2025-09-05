import numpy as np
arr1=np.random.randint(1,10,(5,1))
arr2=np.random.randint(1,10,(5,1))


intersection=list(set(arr1.flatten()) & set(arr2.flatten()))
print(intersection)