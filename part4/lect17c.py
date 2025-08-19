from sklearn.preprocessing import normalize
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
print(normalize(students.loc[:,['GPA']],axis=0, norm='l2'))