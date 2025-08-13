import pandas as pd 
import numpy as np
students = pd.read_csv('./part3/students.csv')
print(students)
#name = "Rama Saed"
#print(name.replace("R","S")) #No problem - string operations not inplace

# all operations on string not in place
print(students.Name.str.replace("R","S"))
students.Name= students.Name.str.replace("R","S").str.lower().str.upper()
#students.Name= students.Name.str.replace("R","S").str.lower().str[0]
print(students.Name.str.len())
print(students.Name.str.cat(sep="-"))
students.Name = [ s.replace(" ","")  for s in students.Name ]
print(students.Name)
