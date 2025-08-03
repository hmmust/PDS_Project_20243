import numpy as np
arr2 = np.array([15,20,0,19,21,-10])
arr2.sort()  #inplace function
arr3 = arr2.reshape(3,2) #not inplace
#arr3 = arr2.reshape(2,3) #not inplace
#arr3 = arr2.reshape(6,1) #not inplace
#arr3 = arr2.reshape(1,6) #not inplace
print(arr3)

