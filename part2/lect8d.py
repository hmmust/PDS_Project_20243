import numpy as np
arr1 = np.array([[15,20,0],[10,15,16]])
arr2 = np.array([[19,21,-10],[17,13,12]])
#arr3 = np.concatenate((arr1,arr2),axis=1) #axis=0
#arr3 = np.stack((arr1,arr2),axis=1) #axis=0
#arr3 = np.vstack((arr1,arr2)) # axis = 0
arr3 = np.hstack((arr1,arr2)) # axis = 1 

print(arr3)

