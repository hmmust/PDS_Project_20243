import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students[0:3])
#loc iloc
print(students[0:3])
print(students.loc[0:2,['Name','Age']])
print(students.iloc[0:2,[1,3]])
print(students.iloc[:,-1])



