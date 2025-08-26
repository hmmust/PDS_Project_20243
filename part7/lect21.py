import requests

uop_page = requests.get("http://www.uop.edu.jo")
print(uop_page.status_code)
print(uop_page.content)