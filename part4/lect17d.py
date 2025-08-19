from sklearn.preprocessing import Binarizer
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
bin = Binarizer(threshold=3)
students['GPA_vgood'] = bin.fit_transform(students.loc[:,['GPA']])
#print(bin.fit_transform(students.loc[:,['GPA']]))
print(students)