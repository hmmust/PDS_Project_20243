import numpy as np
arr1 = np.array([[15,20,13],
                 [19,21,25],
                 [18,14,12]])
arr2 = np.array([15,20,13,19,21,25])
print(arr2[1])
print(arr2[[1,3]])
print(arr2[[-1,-2,-1]])
#print(arr2[[-1,-2,0:2]]) # error
print(arr1[1,2])  #item in row 1 col 2
print(arr1[[1,2]]) #rows 1 and 2 

