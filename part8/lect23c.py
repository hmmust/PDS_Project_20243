from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()
students = pd.read_csv("../part3/students.csv")

@app.get("/student/{id}")
def student(id):
    studentinfo= json.loads(students[students.Id==int(id)].to_json(orient="records"))
    #print(students[students.Id==int(id)])
    return studentinfo

@app.get("/majors")
def majors():
    return list(students['Major'].unique())