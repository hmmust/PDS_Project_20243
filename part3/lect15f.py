import datetime
import pandas as pd


students = pd.read_csv('./part3/students.csv')
td= pd.Timedelta(minutes=20)
project_start = datetime.datetime(2025,9,1,8,0)
students['project']=pd.date_range(project_start,
                                  freq=td,
                                  periods=len(students))
print(students)

delay = pd.Timedelta(minutes=15)
students['project'] += delay
print(students)
