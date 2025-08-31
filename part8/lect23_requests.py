import requests

page= requests.get("http://127.0.0.1:8000/majors")
print(page.json())