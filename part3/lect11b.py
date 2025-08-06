import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students.shape)
print(students.values)
print(students.T)