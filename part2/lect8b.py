import numpy as np
arr2 = np.array([[15,20,0],[19,21,-10]])
arr3 = arr2.reshape(-1) #flattening 2D->1D (vector)
arr3 = arr2.reshape(-1,1) #flattening (column)
print(arr3)

