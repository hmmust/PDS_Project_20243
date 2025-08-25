import pandas as pd
students = pd.read_csv("./part3/students.csv",chunksize=3)
chucks=[]
for chunk in students:
    chunk.Year.fillna(2019,inplace=True)
    chunk.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
    chunk.Year = chunk.Year.astype(int)
    chucks.append(chunk)

students = pd.concat(chucks,axis=0,ignore_index=True)
print(students)