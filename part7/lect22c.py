import requests
import pandas as pd
data_page = requests.post("https://httpbin.org/post",
                          json={"key":"Hossam"})
print(data_page.status_code)
print(data_page.json())

    