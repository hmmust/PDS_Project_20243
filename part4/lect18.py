from sklearn.preprocessing import (OneHotEncoder,
                                   StandardScaler,
                                   Normalizer)
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')
#print(students.columns)
cats = ['Major']
nums = ['Age', 'GPA']

nums_tranformer =  Pipeline(steps=[
    ('nulls',SimpleImputer(strategy="mean")),
    ('normal',StandardScaler()),
])
cats_tranformer =  Pipeline(steps=[
    ('nulls',SimpleImputer(strategy="most_frequent")),
    ('encoding', OneHotEncoder()),
])

processing = ColumnTransformer(transformers=[
    ('nums', nums_tranformer, nums ),
    ('cats', cats_tranformer, cats)
],remainder="passthrough")
new_data = processing.fit_transform(students)
new_students = pd.DataFrame(new_data,
                            columns=processing.get_feature_names_out())
#print(new_students.columns)
new_students.columns= ['Age', 'GPA', 'Major_SE', 'Major_CS',
       'Major_DS', 'Major_DSS', 'Major_IS', 'Id',
       'Name', 'Year']
new_students = new_students.loc[:,['Id','Name','Year','Age','GPA','Major_SE', 'Major_CS',
       'Major_DS', 'Major_DSS', 'Major_IS']]
print(new_students)