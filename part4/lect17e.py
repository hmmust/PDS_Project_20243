from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
students.replace({"DSS":"DS"," SE":"SE"},inplace=True)
encoder = LabelEncoder()
encoder.fit(students.loc[:,['Major']])
#print(encoder.transform(students.loc[:,['Major']]))
students['Major_no']= encoder.transform(students.loc[:,['Major']])
print(students)
