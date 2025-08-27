import requests
import pandas as pd
data_page = requests.get("http://raw.githubusercontent.com/hmmust/PDS_Project_20243/refs/heads/main/part5/students.json")

if  data_page: #data_page.status_code == 200:
    print(data_page.status_code)
    print(data_page.json())
    print(type(data_page.json()))
    students = pd.DataFrame(data_page.json())
    print(students)
else:
    print("file not found!")