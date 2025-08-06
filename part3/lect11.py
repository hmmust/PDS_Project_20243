import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
students2 = pd.read_csv('./part3/students2.csv')
all_students = pd.concat((students,students2))
#all_students = pd.concat((students,students2),
#                         ignore_index=True)
all_students.drop([0,1],inplace=True)
all_students.reset_index(drop=True,inplace=True)
#all_students.set_index('Id',inplace=True)
all_students.drop('Id',axis=1,inplace=True)
