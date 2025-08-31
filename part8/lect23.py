from fastapi import FastAPI
app = FastAPI()
@app.get("/ahmad")
def ahmad():
    return {"name":"ahmad","age":20}

@app.get("/ahlam")
def ahlam():
    return {"name":"ahlam"}

@app.get("/student/{sname}")
def student(sname):
    return {"name":sname}

@app.get("/studentinfo")
def studentinfo(name,age):
    return {"name":name,"age":age}