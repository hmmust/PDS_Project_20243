import numpy as np
from numpy import random 

students = np.array(["Rana","Shahid","Hamzah","Salma","Osama"])

#random.shuffle(students) #inplace
print(random.permutation(students)) # not inplace function 
print(students) 

# select random distribution of student on 7-days 2-shifts
print(random.choice(students,size=(7,2),p=[0.2,0.2,0.2,0.2,0.2]))