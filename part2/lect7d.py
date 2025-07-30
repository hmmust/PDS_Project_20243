import numpy as np
arr1 = np.array([[15,20,13],
                 [19,21,25],
                 [18,14,12]])
print(arr1[0,0])
print(arr1[0])
print(arr1[-1,-1]) #last col in last row
print(arr1[-1]) #last row
#arr1[0] = [13,14,15]
arr1[0] = np.arange(1,4)
arr1[0][0] = 100
arr1[0,0] = 100
print(arr1)