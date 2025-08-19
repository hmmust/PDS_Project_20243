from sklearn.preprocessing import OneHotEncoder
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
students.replace({"DSS":"DS"," SE":"SE"},inplace=True)
encoder = OneHotEncoder()
encoder.fit(students.loc[:,['Major']])

data =encoder.transform(students.loc[:,['Major']])
col_names = encoder.get_feature_names_out()
new_major = pd.DataFrame(data.toarray(),columns=col_names)

#print(new_major)
students= pd.concat((students,new_major),axis=1)
print(students)