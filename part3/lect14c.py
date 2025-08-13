import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
students2 = pd.read_csv('./part3/students2.csv')
all_students_rows = pd.concat((students,students2),axis=0)
all_students_cols = pd.concat((students,students2),axis=1)

print(all_students_rows)
print(all_students_cols)
