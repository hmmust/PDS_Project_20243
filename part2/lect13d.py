import numpy as np
from numpy import random 

print(random.randint(100)) # 0-100
print(random.randint(50,100)) # 50-100
print(random.randint(low=50,high=100)) # 50-100

print(random.randint(50,100,10)) # 50-100
print(random.randint(50,100,size=10)) # 50-100
print(random.randint(50,100,size=(5,5))) # 50-100
