import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
students.sort_values(by=['Name'],inplace=True)
students.sort_values(by=['Name'],inplace=True,ascending=False)
students.sort_values(by=['Major','GPA'],inplace=True,ascending=False)
students.sort_values(by=['Major','GPA'],inplace=True,ascending=[True,False])
students.sort_values(by=['Name'],inplace=True,ascending=False)
students.sort_index(inplace=True)
students.sort_index(axis=1,inplace=True)


print(students)







