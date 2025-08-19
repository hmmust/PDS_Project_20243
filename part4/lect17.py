from sklearn.preprocessing import MinMaxScaler
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
print(students.loc[:,'GPA']) # 0-1
scaler = MinMaxScaler(feature_range=(0,1))
scaler.fit(students.loc[:,['GPA']])
print(scaler.transform(np.array([3,3.5,3.6]).reshape(-1,1)))
print(scaler.fit_transform(students.loc[:,['GPA']]))