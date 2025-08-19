from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
scaler = StandardScaler()
print(scaler.fit_transform(students.loc[:,['GPA']]))