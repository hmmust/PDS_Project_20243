import numpy as np
from numpy import random 

students = ["Rana","Shahid","Hamzah","Salma","Osama"]

# random choice from students
print(random.choice(students,size=3))

# random symbol
characters = "@#$%^&_-"
print(random.choice(list(characters),size=2)) #exposed to repeating
