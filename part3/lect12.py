import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students[students['GPA']>=3])
print(students[students['Major']=='DS'])
#print(students[(students['Major']=='DS' and students['GPA']>=3)])
print(students.query('Major == "DS" and GPA >3 '))
